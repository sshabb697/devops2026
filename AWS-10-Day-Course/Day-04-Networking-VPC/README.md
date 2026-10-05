# Day 4 — Networking (VPC)

**Goal:** Build your own private network in AWS: a VPC with a public and a private subnet, route tables, an internet gateway, and a NAT gateway.

| # | Item | Time |
| - | ---- | ---- |
| 01 | [Lesson — What is a VPC?](./01-What-is-a-VPC.md) | 10m |
| Lab | [Lab 04A — Build a VPC with the wizard](./Lab-04A-Build-a-VPC.md) | 15m |
| 02 | [Lesson — Routing, gateways, SG vs NACL](./02-Routing-and-Security.md) | 10m |
| Lab | [Lab 04B — Public + private subnet test](./Lab-04B-Public-Private-Test.md) | 15m |
| | Recap | 10m |

**Day 4 deliverable:** a working custom VPC where a public instance has internet and a private instance reaches out only via NAT.

> **Money reminder:** a **NAT Gateway** costs ~$0.045/hour even idle. **Delete it at the end of the day.**

**Go further (optional):** [VPC getting started](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)
