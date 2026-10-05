# 01 — Serverless with Lambda

**Learning objectives**

- Understand **serverless** and **AWS Lambda**
- Know how Lambda is triggered and billed

---

## One-sentence idea

Lambda runs **your code on demand** without you ever launching or managing a server.

---

## Analogy: a vending machine

An EC2 server is like **hiring a chef** who stands in the kitchen all day (and gets paid) whether anyone orders or not. Lambda is a **vending machine**: it does nothing (and costs nothing) until someone presses a button — then it instantly serves, and goes quiet again.

- **No servers to manage** — AWS provisions compute for each run.
- **Pay per request** + runtime in milliseconds. Idle = free.
- **Scales automatically** — 1 request or 10,000, Lambda just runs more copies.

---

## How Lambda works

```text
Trigger ─▶ Lambda function (your code) ─▶ Result
```

**Triggers** (events that run your function):
- An **API Gateway** HTTP request
- A new file in **S3**
- A message on a queue (SQS) or schedule (EventBridge)
- A manual **invoke**

You just write the **handler** — the function AWS calls:

```python
def lambda_handler(event, context):
    name = event.get("name", "world")
    return {"message": f"Hello, {name}!"}
```

- `event` = the input data from the trigger.
- `context` = runtime info (time left, request id).

---

## When to use Lambda

| Great for | Not ideal for |
| --------- | ------------- |
| Short tasks, glue code, automation | Long-running jobs (>15 min) |
| Event-driven workflows | Apps needing constant warm state |
| Spiky/occasional traffic | Very high steady throughput (cost) |

Classic DevOps use: **auto-cleanup** scripts (e.g. delete unused EBS snapshots on a schedule).

---

## Knowledge check

1. Why might Lambda be cheaper than an EC2 server for an occasional task?
2. What is the `event` argument?

<details>
<summary>Answers</summary>

1. Lambda bills only when it runs (per request + ms); an idle EC2 instance still costs money.
2. The input data passed in by whatever triggered the function.

</details>

➡️ Next: [Lab 10A](./Lab-10A-First-Lambda.md)
