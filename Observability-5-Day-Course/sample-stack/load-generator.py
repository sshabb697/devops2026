"""Generate repeatable healthy or failing traffic for the observability labs."""
import argparse
import time
from urllib.error import HTTPError
from urllib.request import urlopen


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://demo-app:8080")
    parser.add_argument("--requests", type=int, default=40)
    parser.add_argument("--error-every", type=int, default=0)
    parser.add_argument("--delay-ms", type=int, default=0)
    parser.add_argument("--interval-ms", type=int, default=100)
    return parser.parse_args()


def main():
    args = parse_args()
    successes = 0
    failures = 0

    for request_number in range(1, args.requests + 1):
        should_fail = args.error_every > 0 and request_number % args.error_every == 0
        query = f"delay_ms={args.delay_ms}&fail={str(should_fail).lower()}"
        try:
            with urlopen(f"{args.base_url}/checkout?{query}", timeout=5) as response:
                successes += response.status < 500
        except HTTPError as error:
            failures += error.code >= 500
        time.sleep(args.interval_ms / 1000)

    print(f"Traffic complete: {successes} successful, {failures} failed")


if __name__ == "__main__":
    main()
