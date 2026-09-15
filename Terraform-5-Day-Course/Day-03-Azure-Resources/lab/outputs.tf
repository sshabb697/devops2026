output "rg_name" {
  value = azurerm_resource_group.main.name
}

output "storage_name" {
  value = azurerm_storage_account.web.name
}

output "website_url" {
  value = azurerm_storage_account.web.primary_web_endpoint
}
