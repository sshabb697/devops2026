# 01 — What is IaC? CloudFormation

**Learning objectives**

- Understand **Infrastructure as Code (IaC)**
- Know what a **CloudFormation** template and stack are

---

## One-sentence idea

IaC means you **write down your infrastructure in a file** and a tool builds it for you — exactly the same way, every time.

---

## Why IaC beats clicking

Clicking in the console is fine once. But:

- Can you rebuild it **identically** next week? Next region?
- Can a teammate **review** the change before it happens?
- Can you **delete** everything cleanly in one go?

With IaC the answer is yes. The file is the single source of truth, lives in Git, and is **repeatable**.

| Clicking (manual) | IaC (automated) |
| ----------------- | --------------- |
| Hard to repeat | Identical every time |
| No history | Tracked in Git |
| Easy to forget resources | Delete the whole stack at once |
| No peer review | Review the file in a PR |

---

## CloudFormation = AWS's native IaC

You write a **template** (YAML or JSON) describing resources. CloudFormation creates them as a **stack** — and deletes them all together when you delete the stack.

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: aws-class-cfn-amy-051026
```

- **Template** = the recipe.
- **Stack** = the running result of one template.
- Change the template → CloudFormation works out the **difference** and updates only what changed (a *change set*).

---

## Key template sections

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:   # inputs you pass in (e.g. instance type)
Resources:    # the stuff to create (required)
Outputs:      # values to show after (e.g. the bucket name)
```

---

## Knowledge check

1. Give two advantages of IaC over clicking in the console.
2. What's the difference between a template and a stack?

<details>
<summary>Answers</summary>

1. Repeatable/identical builds, Git history, peer review, one-command cleanup (any two).
2. A template is the file (recipe); a stack is the set of live resources created from it.

</details>

➡️ Next: [Lab 07A](./Lab-07A-CloudFormation-Stack.md)
