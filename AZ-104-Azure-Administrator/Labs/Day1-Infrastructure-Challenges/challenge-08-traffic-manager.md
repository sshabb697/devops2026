# Challenge 08 (Optional) — Traffic Manager

**Time:** 45–60 minutes  
**You will learn:** Use **Azure Traffic Manager** (DNS-based) to distribute traffic across endpoints in different regions.

> Traffic Manager does **not** replace a regional Load Balancer. It answers DNS with the best endpoint IP based on routing method (Performance, Priority, Weighted, Geographic).

## Target idea

```
  Client → DNS (Traffic Manager)
              ├── Endpoint Region A  (Public IP / web app)
              └── Endpoint Region B  (Public IP / web app)
```

---

## Part A — Create two regional endpoints (25 min)

Use **App Service** (cheaper/simpler) or two small VMs with web servers.

### App Service path (recommended)

1. Create App Service `app-d1-tm-<yourname>-a` in **Region A** (e.g. East US) — Free/B1.
2. Create App Service `app-d1-tm-<yourname>-b` in **Region B** (e.g. West Europe) — Free/B1.
3. In each app’s **Configuration** or default page, note the URL: `https://....azurewebsites.net`.

Optional: use Kudu/console to customize the home page text with the region name so you can see which endpoint answered.

### VM path

Deploy one small web VM + public IP in Region A and one in Region B (reuse Challenge 06 install steps). Note each public IP.

---

## Part B — Create Traffic Manager profile (15 min)

1. **+ Create a resource → Traffic Manager profile → Create**.

| Field | Value |
| ----- | ----- |
| Name | `tm-d1-<yourname>` (becomes `tm-d1-<yourname>.trafficmanager.net`) |
| Routing method | **Performance** (or Priority for active/passive) |
| Resource group | `rg-d1-<yourname>-tm` (new) |
| Location of RG | Any (TM is global; RG still needs a region) |

2. Open the profile → **Endpoints → Add**.

**Endpoint 1**

| Field | Value |
| ----- | ----- |
| Type | Azure endpoint |
| Name | `endpoint-a` |
| Target resource type | App Service **or** Public IP address |
| Target | Your Region A resource |
| Priority / Weight | As required by routing method |

**Endpoint 2** — same for Region B (`endpoint-b`).

3. Wait until monitoring status shows **Online** (can take a few minutes).

---

## Part C — Test

1. Copy the Traffic Manager DNS name: `http://tm-d1-<yourname>.trafficmanager.net` (or https if endpoints support it).
2. Browse / `curl` several times.
3. Stop or stop the App Service / VM in one region → after probes fail, TM should stop sending traffic there (for Priority/Performance with health checks).

✅ **Checkpoint:** DNS name resolves and reaches a healthy endpoint.

---

## Part D — Compare with Load Balancer

| | Load Balancer | Traffic Manager |
|--|---------------|-----------------|
| Layer | Network (L4) | DNS |
| Scope | Usually one region | Multi-region |
| Returns | Packets to backends | IP/hostname of endpoint |

---

## Deliverables

- [ ] Two endpoints in different regions  
- [ ] Traffic Manager profile with both endpoints Online  
- [ ] Tested via `*.trafficmanager.net`  
- [ ] Can explain LB vs Traffic Manager  

## Cleanup

```bash
az group delete -n rg-d1-<yourname>-tm --yes --no-wait
# also delete regional app/VM RGs you created for this challenge
```

➡️ Next (optional): [Challenge 09 — Automation & Cost](./challenge-09-automation-cost.md)
