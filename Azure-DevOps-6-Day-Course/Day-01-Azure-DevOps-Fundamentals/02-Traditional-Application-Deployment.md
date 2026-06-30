# 02 - Traditional Application Deployment

## Overview

Before we study the **DevOps lifecycle**, it helps to see how software was typically built and deployed in many organizations for decades. That "before" picture makes the DevOps approach much easier to understand.

In traditional IT, **Development**, **QA**, and **Operations** often worked as separate departments with different goals, tools, and managers. Software moved between them like a package on a conveyor belt — hand off, wait, hope nothing breaks.

> **Key idea:** DevOps is not magic. It is a deliberate response to real problems that traditional deployment created.

---

## 1. Siloed Teams — "Us vs Them"

Each team optimized for its own success, not for delivering value to users.

```
   BUSINESS / PRODUCT                IT DEPARTMENTS (SILOS)
  ┌──────────────────┐
  │ "We need this    │
  │  feature live    │──────────┐
  │  by Friday!"     │          │
  └──────────────────┘          ▼
                    ┌─────────────────────────────────────────────────────┐
                    │                                                     │
              ┌─────▼─────┐         ┌───────────┐         ┌──────────────┐  │
              │    DEV    │  throw  │    QA     │  throw  │     OPS      │  │
              │           │ ──────► │           │ ──────► │              │  │
              │ Build it  │  over   │ Test it   │  over   │ Run it in    │  │
              │ fast      │  wall   │ (late)    │  wall   │ production   │  │
              └───────────┘         └───────────┘         └──────────────┘  │
                    │                     │                      │          │
              "Not my job               "Works on            "Don't change │
               if it crashes              my machine"           anything!"   │
               in prod"                                                     │
                    └─────────────────────────────────────────────────────┘
                                         ▲
                                         │
                              BLAME GOES BACK DOWN THE LINE
                              when production breaks
```

| Team | Primary goal | Typical mindset |
| ---- | ------------ | --------------- |
| **Development** | Deliver new features | "Move fast — Ops will figure out deployment" |
| **QA** | Find defects before release | "We only get the build two days before go-live" |
| **Operations** | Keep systems stable | "Every release is a risk — freeze changes" |

---

## 2. Traditional Deployment Flow — Manual and Sequential

A typical release followed a long, linear path. Many steps were done **by hand** — copying files, editing configs, running scripts from a checklist.

```
  PLAN (months)          BUILD (weeks)           TEST (weeks)         DEPLOY (days)
 ┌─────────────┐       ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
 │ Requirements│       │ Developers  │       │ QA team     │       │ Ops team    │
 │ Design docs │──────►│ code on     │──────►│ manual test │──────►│ manual      │
 │ Sign-offs   │       │ laptops     │       │ on staging  │       │ install on  │
 │ Change      │       │ Merge to    │       │ Bug reports │       │ production  │
 │ requests    │       │ trunk (rare)│       │ back to Dev │       │ servers     │
 └─────────────┘       └─────────────┘       └─────────────┘       └─────────────┘
       │                     │                     │                     │
       ▼                     ▼                     ▼                     ▼
   Heavy docs            "Works on              Environment          Downtime
   Upfront               my machine"           mismatch             window
                                               (staging ≠ prod)
```

### What deployment night often looked like

```
  FRIDAY 11:00 PM — PRODUCTION DEPLOYMENT WINDOW
  ══════════════════════════════════════════════

  Ops engineer          Dev (on call)           QA (gone home)
       │                     │                      │
       ├─ Stop app           │                      │
       ├─ Copy ZIP by hand   │                      │
       ├─ Edit web.config    ├─ "Which version?"    │
       ├─ Run SQL script     │                      │
       ├─ Restart IIS        ├─ "Try this hotfix"   │
       ├─ ERROR!             │                      │
       └─ Rollback?          └─ "Not sure..."       X  (unavailable)

  Result: 4-hour outage, angry users, post-mortem blame meeting
```

---

## 3. The Release Timeline — "Big Bang" Delivery

Traditional teams bundled many months of work into **one large release**. Risk piled up silently until launch day.

```
  TRADITIONAL RELEASE TIMELINE (example: 6-month cycle)
  ─────────────────────────────────────────────────────

  Month 1    Month 2    Month 3    Month 4    Month 5    Month 6
  ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────► GO LIVE!
  │  Design  │   Dev    │   Dev    │   Dev    │   QA     │  Fix     │
  │  & plan  │          │          │          │          │  bugs    │
  └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
                                                              ▲
                                                              │
                                                    ALL RISK LANDS HERE
                                                    (one big bang)

  User value delivered:        ████████████████████████████████░░  (nothing... then everything)
  Feedback from production:     ──────────────────────────────────►  (too late to pivot)
```

---

## 4. The "Wall of Confusion"

This classic diagram shows what happens when Dev and Ops do not share tools, processes, or responsibility.

```
  DEVELOPMENT SIDE                    THE WALL                    OPERATIONS SIDE
 ┌─────────────────────┐         ┌─────────────┐         ┌─────────────────────┐
 │  IDE, Git (maybe)   │         │             │         │  Monitoring tools   │
 │  Feature branches   │         │   ███████   │         │  Runbooks (paper)   │
 │  Unit tests (some)  │ ──────► │   ███████   │ ──────► │  Manual deploy      │
 │  "Ready to ship!"   │  ZIP /  │   █ WALL █  │  tickets│  "What changed?"    │
 │                     │  email  │   ███████   │         │  "Who approved?"    │
 └─────────────────────┘         └─────────────┘         └─────────────────────┘

         Dev says:                      ▲                 Ops says:
    "It worked in QA!"                  │            "Your code broke prod!"
                                        │
                              NO SHARED VISIBILITY
                         (configs, logs, dependencies)
```

**What crosses the wall:** compiled code, vague instructions, panic at 2 AM.  
**What does *not* cross:** environment parity, automated tests, deployment knowledge, ownership.

---

## 5. Common Challenges — Symptoms Students Should Recognize

| # | Challenge | What happens | Symptom you see |
| - | --------- | -------------- | --------------- |
| 1 | **Siloed teams** | Dev, QA, Ops optimize locally | Finger-pointing after outages |
| 2 | **Manual deployment** | Humans run steps from a checklist | Errors, slow releases, hero culture |
| 3 | **Environment drift** | Staging ≠ Production | "Works on my machine" / "Passed in QA" |
| 4 | **Big-bang releases** | Many changes at once | High change failure rate, scary deploys |
| 5 | **Late testing** | QA starts near the end | Bugs found when fixes are expensive |
| 6 | **Slow feedback** | Users see features months later | Wrong features built; no learning loop |
| 7 | **Knowledge in heads** | Only one person knows how to deploy | Bus factor of 1; vacation = risk |
| 8 | **Change resistance** | Ops fears every release | Change freezes; innovation slows |

---

## 6. Traditional vs DevOps — Side by Side

```
  TRADITIONAL                              DEVOPS
  ───────────                              ──────

  Linear handoffs                          Continuous loop
  ───────────────►                         Plan → Code → Build → Test
  Plan → Dev → QA → Ops                    → Release → Deploy → Operate
                                           → Monitor ──► back to Plan
                                                    ∞

  Large releases (months)                  Small releases (days/hours)
  ████████████████░░                       █ █ █ █ █ █ █ █

  Manual deploy                            Automated pipeline
  [human][human][human]                    [build][test][deploy]

  Ops learns at go-live                    Monitoring from day one
  "Surprise!"                              Feedback drives next sprint

  Blame culture                            Shared ownership
  "Whose fault?"                           "How do we fix the system?"
```

| Dimension | Traditional | DevOps response |
| --------- | ----------- | --------------- |
| **Team structure** | Separate Dev / QA / Ops | Cross-functional teams, shared goals |
| **Release size** | Large, infrequent | Small, frequent |
| **Deployment** | Manual scripts, runbooks | Automated CI/CD pipelines |
| **Testing** | Late, mostly manual | Early, automated ("shift left") |
| **Infrastructure** | Click-ops, snowflake servers | Infrastructure as Code (repeatable) |
| **Feedback** | Slow; after big releases | Fast; metrics and logs in production |
| **Culture** | Throw over the wall | You build it, you run it |

---

## 7. What DevOps Fixes — Challenge → Solution Map

Use this map to connect each pain point to a DevOps practice you will learn in this course.

```
  TRADITIONAL PAIN                    DEVOPS FIX                         YOU WILL SEE
  ───────────────                    ──────────                         ────────────

  Silos & blame          ───────►    Culture + shared ownership         CALMS (Culture)
  Manual, error-prone    ───────►    Automation (CI/CD, IaC)            Azure Pipelines
  "Works on my machine"  ───────►    Same pipeline for all envs         Environments & gates
  Big-bang risk          ───────►    Small batches, frequent deploy     CD / trunk-based flow
  Bugs found too late    ───────►    Automated tests in pipeline        Shift-left testing
  No production insight  ───────►    Monitoring & feedback loops        Monitor → Plan
  Slow delivery          ───────►    Flow + lean practices              DORA metrics
```

### Before and after — one feature request

```
  TRADITIONAL (weeks to months)                DEVOPS (hours to days)
  ─────────────────────────────                ──────────────────────

  Request ──► backlog ──► 6-mo project         Request ──► user story ──► sprint
       ──► manual QA ──► deploy night              ──► CI builds & tests
       ──► hope it works                           ──► CD deploys to staging
                                                    ──► auto checks ──► prod
                                                    ──► monitor ──► learn
```

---

## 8. Instructor Tip — Tell the Story Out Loud

Walk students through this narrative:

1. **Product** asks for a small login improvement.
2. **Dev** finishes in three days — but the release train leaves once per quarter.
3. **QA** gets the build one week before go-live and finds a security issue.
4. **Ops** has never seen this build; production config differs from staging.
5. **Deploy night** fails; rollback takes hours.
6. **Monday meeting:** Dev blames Ops, Ops blames Dev, QA says "we weren't involved early."

Then ask: *Which step would DevOps change first?* (Usually: smaller releases, automated pipeline, shared ownership, environments that match.)

---

## Summary

- Traditional deployment used **siloed teams**, **manual steps**, and **infrequent big releases**.
- The **wall of confusion** between Dev and Ops caused slow delivery, outages, and blame.
- DevOps addresses these challenges with **collaboration**, **automation**, **small batches**, and **fast feedback** — not just new tools.
- The next lesson shows the **DevOps lifecycle** — the continuous loop that replaces the old linear handoffs.

## Knowledge Check

1. Draw (from memory) the three silos and the "wall" between Dev and Ops.
2. Name three symptoms of manual, big-bang deployment.
3. For "environment drift," what DevOps practice helps fix it?
4. Why is it easier to roll back a small release than a big-bang release?

➡️ Next: [03 - DevOps Lifecycle](./03-DevOps-Lifecycle.md)
