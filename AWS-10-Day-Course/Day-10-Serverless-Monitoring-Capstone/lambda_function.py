"""AWS 10-Day Course - Day 10 demo Lambda.

Returns a friendly greeting. Reads an optional 'name' from the event.
"""
import json


def lambda_handler(event, context):
    name = event.get("name", "world") if isinstance(event, dict) else "world"
    body = {"message": f"Hello, {name}! This ran on AWS Lambda."}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
