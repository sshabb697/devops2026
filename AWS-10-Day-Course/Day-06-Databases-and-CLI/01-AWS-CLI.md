# 01 — The AWS CLI

**Learning objectives**

- Know what the **AWS CLI** is and why DevOps lives in it
- Understand credentials, region, and output format

---

## One-sentence idea

The AWS CLI lets you do **everything the console does, by typing commands** — so you can script and automate it.

---

## Why the CLI matters

Clicking in the console is fine for learning. But DevOps needs tasks that are **repeatable, fast, and automatable**:

- Launch 10 servers with one command.
- Put AWS steps inside a CI/CD pipeline.
- Script nightly backups or cleanups.

The CLI (and its cousin, the SDKs) is how automation talks to AWS.

---

## The command shape

```bash
aws <service> <action> [options]

aws s3 ls
aws ec2 describe-instances
aws iam create-user --user-name dev-amy
```

- `service` = `s3`, `ec2`, `iam`, `rds`, …
- `action` = `ls`, `describe-instances`, `create-user`, …

---

## Configuring it

`aws configure` stores four things in `~/.aws/`:

| Prompt | Example | What it is |
| ------ | ------- | ---------- |
| Access Key ID | `AKIA...` | Your username for the API |
| Secret Access Key | `wJal...` | Your password for the API (**secret!**) |
| Default region | `eu-west-1` | Where commands run |
| Output format | `json` | How results print (json/table/text) |

> **Security:** access keys are long-lived secrets. Never commit them to Git. On an EC2 server, use an **IAM role** instead (Day 2) — no keys on disk.

---

## Handy output tricks

```bash
aws ec2 describe-instances --output table
aws ec2 describe-instances \
  --query "Reservations[].Instances[].InstanceId" --output text
```

`--query` uses **JMESPath** to pull out just the fields you want.

---

## Knowledge check

1. Why use the CLI instead of the console?
2. Where should an EC2 app get its credentials from — access keys or a role?

<details>
<summary>Answers</summary>

1. It's scriptable, repeatable, fast, and can run inside automation/CI-CD.
2. An IAM role attached to the instance — no long-lived secrets stored on disk.

</details>

➡️ Next: [Lab 06A](./Lab-06A-CLI-Setup.md)
