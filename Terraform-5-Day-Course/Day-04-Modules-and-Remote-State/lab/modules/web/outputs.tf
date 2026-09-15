output "website_url" {
  value = azurerm_storage_account.web.primary_web_endpoint
}

output "rg_name" {
  value = azurerm_resource_group.main.name
}
