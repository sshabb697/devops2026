# 02 — A website from storage

**Learning objectives**

- Storage can host a **static website** (HTML files)
- Terraform can upload a file (`azurerm_storage_blob`)

---

## One-sentence idea

The storage account is the house. **index.html** is the welcome mat.

---

## Example idea

Enable `static_website { index_document = "index.html" }` on the storage account.  
Upload `www/index.html`.  
Output the website URL.

No VM. No Kubernetes. Good first “I deployed something.”

---

## Knowledge check

1. Is this a full app server?
2. After apply, where do you click?

<details>
<summary>Answers</summary>

1. No — only static files.  
2. The URL from `terraform output website_url`.

</details>

➡️ Next: [Lab 03B](./Lab-03B-Website.md)
