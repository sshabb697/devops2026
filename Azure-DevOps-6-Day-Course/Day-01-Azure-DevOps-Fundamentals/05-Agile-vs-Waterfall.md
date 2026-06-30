# 05 - Agile vs Waterfall

## Overview

Before DevOps, teams needed a way to *manage* software projects. Two dominant approaches are **Waterfall** and **Agile**. Understanding both explains why Agile pairs so naturally with DevOps.

## Waterfall

Waterfall is a **sequential** methodology: each phase must finish before the next begins, like water flowing down steps.

```
Requirements → Design → Implementation → Verification → Maintenance
```

**Characteristics:**
- Heavy upfront planning and documentation.
- Each phase has a defined deliverable and sign-off.
- Little room for change once a phase is complete.
- The customer typically sees the product only at the end.

**Pros:**
- Clear structure and milestones.
- Works for projects with fixed, well-understood requirements.
- Easy to measure progress against the plan.

**Cons:**
- Inflexible — late changes are expensive.
- Risk is discovered late (testing comes near the end).
- Long time before delivering any value.

## Agile

Agile is an **iterative, incremental** approach. Work is delivered in small cycles (iterations/sprints), each producing a potentially shippable increment.

**The Agile Manifesto values:**
1. **Individuals and interactions** over processes and tools
2. **Working software** over comprehensive documentation
3. **Customer collaboration** over contract negotiation
4. **Responding to change** over following a plan

> "That is, while there is value in the items on the right, we value the items on the left more."

**Characteristics:**
- Short iterations (typically 1–4 weeks).
- Continuous customer feedback.
- Embraces changing requirements.
- Cross-functional, self-organizing teams.

**Popular Agile frameworks:** Scrum, Kanban, SAFe, XP (Extreme Programming).

## Side-by-Side Comparison

| Aspect | Waterfall | Agile |
| ------ | --------- | ----- |
| Approach | Sequential | Iterative/incremental |
| Flexibility | Low | High |
| Customer involvement | Mostly at start/end | Continuous |
| Delivery | One big release | Frequent small releases |
| Risk discovery | Late | Early |
| Documentation | Extensive | Just enough |
| Best for | Fixed, stable requirements | Evolving requirements |

## Why Agile + DevOps?

Agile improves *how teams plan and build* software in small increments. DevOps extends that mindset to *delivering and operating* software continuously. Together:

- Agile produces small, frequent increments of working software.
- DevOps automates building, testing, and deploying those increments quickly and safely.

Azure DevOps supports Agile directly through **Azure Boards** (backlogs, sprints, Kanban) — covered on Day 4.

## Summary

- **Waterfall** is linear and plan-heavy; good for stable requirements.
- **Agile** is iterative and adaptive; good for evolving requirements.
- Agile's iterative delivery is a natural fit for DevOps automation.

## Knowledge Check

1. List the phases of the Waterfall model.
2. State two of the four Agile Manifesto values.
3. Why does Agile pair well with DevOps?

➡️ Next: [06 - Scrum](./06-Scrum.md)
