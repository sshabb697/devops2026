"""Tiny demo app: writes a log line and exposes Prometheus /metrics. No extra libraries."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

REQUESTS = 0
LOG_PATH = "/logs/app.log"


def log(level, message):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {level} demo-app {message}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(line)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUESTS
        REQUESTS += 1
        if self.path.startswith("/metrics"):
            body = (
                "# HELP demo_requests_total HTTP requests handled by the demo app\n"
                "# TYPE demo_requests_total counter\n"
                f"demo_requests_total {REQUESTS}\n"
                "# HELP demo_up 1 when the process is running\n"
                "# TYPE demo_up gauge\n"
                "demo_up 1\n"
            )
            self._send(200, "text/plain; version=0.0.4", body.encode())
            log("INFO", f"metrics scrape count={REQUESTS}")
            return
        if self.path.startswith("/error"):
            log("ERROR", "payment timeout")
            self._send(500, "text/plain", b"payment timeout\n")
            return
        log("INFO", f"hello path={self.path}")
        self._send(200, "text/plain", b"hello observability\n")

    def _send(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    log("INFO", "started")
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
