# Lab 10A — Your first Lambda

**Time:** 15 minutes
Uses [`lambda_function.py`](./lambda_function.py).

---

## Part A — Create the function (6 min)

1. **Lambda → Create function → Author from scratch**.
2. Name: `class-fn`. Runtime: **Python 3.12**. Create.
3. In the code editor, replace the contents with [`lambda_function.py`](./lambda_function.py).
4. Click **Deploy**.

---

## Part B — Test it (5 min)

1. Click **Test** → create a test event named `hello` with:
   ```json
   { "name": "Amy" }
   ```
2. Save, then **Test** again.
3. The result shows:
   ```json
   {"statusCode": 200, "body": "{\"message\": \"Hello, Amy! This ran on AWS Lambda.\"}"}
   ```

**From the CLI (alternative):**
```bash
aws lambda invoke --function-name class-fn \
  --payload '{"name":"Amy"}' --cli-binary-format raw-in-base64-out out.json
cat out.json
```

---

## Part C — See the logs (4 min)

Lambda automatically logs to CloudWatch:
```bash
aws logs tail /aws/lambda/class-fn --follow
```
Or console → the function → **Monitor → View CloudWatch logs**. Every invocation appears here — this is your bridge into Day 10's monitoring lesson.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| "Handler not found" | Keep the file named `lambda_function.py` and function `lambda_handler`. |
| CLI base64 error | Include `--cli-binary-format raw-in-base64-out`. |
| No logs | Invoke it at least once; logs appear a few seconds later. |

---

## Deliverables

- [ ] `class-fn` created and deployed
- [ ] Test returns the greeting
- [ ] Found the invocation in CloudWatch Logs

➡️ Next: [02 — CloudWatch monitoring](./02-CloudWatch.md)
