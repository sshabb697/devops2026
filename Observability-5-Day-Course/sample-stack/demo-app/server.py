"""Small observable checkout service with no third-party dependencies."""
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import time
from urllib.parse import parse_qs, urlparse

REQUESTS = defaultdict(int)
LATENCY_BUCKETS = (0.05, 0.1, 0.25, 0.5, 1.0, 2.0)
LATENCY_COUNTS = defaultdict(lambda: [0] * len(LATENCY_BUCKETS))
LATENCY_SUMS = defaultdict(float)
LATENCY_TOTALS = defaultdict(int)
LOG_PATH = "/logs/app.log"
SERVICE = "checkout-api"
VERSION = os.getenv("APP_VERSION", "1.0.0")


def log(level, message, **fields):
    event = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "level": level,
        "service": SERVICE,
        "version": VERSION,
        "message": message,
        **fields,
    }
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, separators=(",", ":")) + "\n")


def observe(route, status, duration):
    REQUESTS[(route, status)] += 1
    LATENCY_TOTALS[route] += 1
    LATENCY_SUMS[route] += duration
    for index, bucket in enumerate(LATENCY_BUCKETS):
        if duration <= bucket:
            LATENCY_COUNTS[route][index] += 1


def metrics():
    lines = [
        "# HELP demo_http_requests_total HTTP requests handled by route and status",
        "# TYPE demo_http_requests_total counter",
    ]
    for (route, status), count in sorted(REQUESTS.items()):
        lines.append(
            f'demo_http_requests_total{{route="{route}",status="{status}"}} {count}'
        )

    lines.extend(
        [
            "# HELP demo_http_request_duration_seconds HTTP request duration by route",
            "# TYPE demo_http_request_duration_seconds histogram",
        ]
    )
    for route in sorted(LATENCY_TOTALS):
        for bucket, count in zip(LATENCY_BUCKETS, LATENCY_COUNTS[route]):
            lines.append(
                'demo_http_request_duration_seconds_bucket'
                f'{{route="{route}",le="{bucket}"}} {count}'
            )
        lines.append(
            'demo_http_request_duration_seconds_bucket'
            f'{{route="{route}",le="+Inf"}} {LATENCY_TOTALS[route]}'
        )
        lines.append(
            f'demo_http_request_duration_seconds_sum{{route="{route}"}} '
            f"{LATENCY_SUMS[route]:.6f}"
        )
        lines.append(
            f'demo_http_request_duration_seconds_count{{route="{route}"}} '
            f"{LATENCY_TOTALS[route]}"
        )

    lines.extend(
        [
            "# HELP demo_build_info Build information for the demo app",
            "# TYPE demo_build_info gauge",
            f'demo_build_info{{service="{SERVICE}",version="{VERSION}"}} 1',
            "# HELP demo_up 1 when the process is running",
            "# TYPE demo_up gauge",
            "demo_up 1",
        ]
    )
    return "\n".join(lines) + "\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/metrics":
            self._send(200, "text/plain; version=0.0.4", metrics().encode())
            return
        if parsed.path == "/health":
            self._send(200, "application/json", b'{"status":"healthy"}\n')
            return

        route = parsed.path if parsed.path in ("/", "/checkout", "/error") else "/not-found"
        status = 200
        message = "request completed"
        body = b"hello observability\n"
        started = time.perf_counter()

        if route == "/checkout":
            query = parse_qs(parsed.query)
            delay_ms = min(int(query.get("delay_ms", ["0"])[0]), 2000)
            if delay_ms > 0:
                time.sleep(delay_ms / 1000)
            if query.get("fail", ["false"])[0].lower() == "true":
                status = 503
                message = "checkout dependency unavailable"
                body = b"checkout unavailable\n"
            else:
                message = "checkout completed"
                body = b"checkout complete\n"
        elif route == "/error":
            status = 500
            message = "payment timeout"
            body = b"payment timeout\n"
        elif route == "/not-found":
            status = 404
            message = "route not found"
            body = b"not found\n"

        duration = time.perf_counter() - started
        observe(route, status, duration)
        log(
            "ERROR" if status >= 500 else "INFO",
            message,
            method="GET",
            route=route,
            status=status,
            duration_ms=round(duration * 1000, 2),
        )
        self._send(status, "text/plain", body)

    def _send(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    log("INFO", "service started", port=8080)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
