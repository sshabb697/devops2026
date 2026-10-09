# Day 4 — Networking (VPC)

**Goal:** Default VPC, custom VPC (public/private/NAT), **VPC peering**, and **Application Load Balancers**.

## Core path (~60 min)

| # | Item | Time |
| - | ---- | ---- |
| 01 | [Lesson — What is a VPC?](./01-What-is-a-VPC.md) | 10m |
| 03 | [Lesson — Default VPC demo](./03-Default-VPC-Demo.md) | 15m |
| Lab | [Lab 04 — Default VPC EC2](./Lab-04-Default-VPC-Demo.md) | 20m |
| Lab | [Lab 04A — Build VPC (wizard)](./Lab-04A-Build-a-VPC.md) | 15m |
| 02 | [Lesson — Routing & SG vs NACL](./02-Routing-and-Security.md) | 10m |
| Lab | [Lab 04B — Public + private test](./Lab-04B-Public-Private-Test.md) | 15m |

## Extension path (+90–120 min, or Day 4 part 2)

| # | Item | Time |
| - | ---- | ---- |
| 04 | [Lesson — VPC peering](./04-VPC-Peering.md) | 15m |
| Lab | [Lab 04C — VPC peering (step-by-step)](./Lab-04C-VPC-Peering.md) | 45–60m |
| 05 | [Lesson — Elastic Load Balancing](./05-Elastic-Load-Balancing.md) | 15m |
| Lab | [Lab 04D — ALB (step-by-step)](./Lab-04D-Application-Load-Balancer.md) | 45–60m |

**Core deliverable:** Explain default VPC (`172.31.0.0/16`) and a **custom** VPC with public internet + private outbound via NAT.

**Extension deliverable:** Peering between `10.1.0.0/16` and `10.2.0.0/16` with routes; **ALB** serving two healthy web targets.

> **Images:** [`../images/day-04-vpc/`](../images/day-04-vpc/) (KodeKloud console/diagrams + local SVG for peering). Index: [images README](../images/README.md).

> **Money:** Delete **NAT Gateway**, **ALB**, and extra EC2 when done. Peering has no hourly fee; ALB and NAT do.

**Go further:** [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/) · [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/)
