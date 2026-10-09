# Day 4 — Networking (VPC)

**Goal:** Understand AWS’s **default VPC**, then build your own network: public and private subnets, route tables, an internet gateway, and a NAT gateway.

| # | Item | Time |
| - | ---- | ---- |
| 01 | [Lesson — What is a VPC?](./01-What-is-a-VPC.md) | 10m |
| 03 | [Lesson — Default VPC demo (console)](./03-Default-VPC-Demo.md) | 15m |
| Lab | [Lab 04 — Default VPC EC2 test](./Lab-04-Default-VPC-Demo.md) | 20m |
| Lab | [Lab 04A — Build a VPC with the wizard](./Lab-04A-Build-a-VPC.md) | 15m |
| 02 | [Lesson — Routing, gateways, SG vs NACL](./02-Routing-and-Security.md) | 10m |
| Lab | [Lab 04B — Public + private subnet test](./Lab-04B-Public-Private-Test.md) | 15m |
| | Recap | 5m |

**Day 4 deliverable:** you can explain the default VPC (`172.31.0.0/16`), then demonstrate a **custom** VPC where a public instance has internet and a private instance reaches out only via NAT.

> **Images:** Lessons and labs use local screenshots and diagrams in [`../images/day-04-vpc/`](../images/day-04-vpc/) (sourced from [KodeKloud AWS Networking Fundamentals](https://kodekloud.com/courses/aws-networking-fundamentals)). See [images README](../images/README.md).

> **Money reminder:** a **NAT Gateway** costs ~$0.045/hour even idle. **Delete it at the end of the day.**

**Go further (optional):** [VPC getting started](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)
