# Lab 03B — Static website

**Time:** 50 minutes  
Same `lab/` folder. Files already include website settings.

If 03A already applied, just:

```bash
terraform apply
terraform output website_url
```

Open the URL in a browser. You should see **Hello from Terraform**.

Change a word in `www/index.html` and apply again. Refresh the browser (wait a few seconds).

---

## End of day

Keep this stack if Day 4 will use it. Otherwise:

```bash
terraform destroy
```

---

## Deliverables

- [ ] Browser shows your HTML
- [ ] You changed HTML and re-applied

➡️ **Day 4:** [Modules and remote state](../Day-04-Modules-and-Remote-State/README.md)
