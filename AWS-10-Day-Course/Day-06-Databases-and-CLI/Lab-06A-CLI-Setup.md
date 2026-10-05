# Lab 06A — Install, configure, and script the CLI

**Time:** 15 minutes

---

## Part A — Install AWS CLI v2 (5 min)

- **Windows:** download and run the MSI from the [install guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
- **macOS:** `brew install awscli` (or the official pkg).
- **Linux:** follow the curl/unzip steps in the install guide.

Verify:
```bash
aws --version          # aws-cli/2.x ...
```

---

## Part B — Create an access key and configure (6 min)

1. **IAM → Users → your admin user → Security credentials → Create access key**.
2. Use case: **Command Line Interface (CLI)**. Create. **Download the .csv** (you only see the secret once).
3. Configure:
   ```bash
   aws configure
   # AWS Access Key ID:     AKIA...
   # AWS Secret Access Key: ****
   # Default region name:   eu-west-1   (your class Region)
   # Default output format: json
   ```
4. Confirm it works:
   ```bash
   aws sts get-caller-identity
   ```
   You should see your Account ID and user ARN.

> **Never** paste these keys into code or Git. If a key leaks, deactivate it in IAM immediately.

---

## Part C — A tiny script (4 min)

List your instances in a clean table:
```bash
aws ec2 describe-instances \
  --query "Reservations[].Instances[].{ID:InstanceId,State:State.Name,Type:InstanceType}" \
  --output table
```

Create an S3 bucket from the CLI (unique name):
```bash
aws s3 mb s3://aws-class-cli-amy-051026
aws s3 ls
```

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `aws` not recognised | Reopen the terminal after install; check PATH. |
| `InvalidClientTokenId` | Wrong/typo'd keys — rerun `aws configure`. |
| Access denied | Your user needs permissions (admin user from Day 2). |

---

## Deliverables

- [ ] AWS CLI v2 installed
- [ ] `aws sts get-caller-identity` returns your identity
- [ ] Ran a `--query` command and created a bucket from the CLI

➡️ Next: [02 — RDS managed databases](./02-RDS-Databases.md)
