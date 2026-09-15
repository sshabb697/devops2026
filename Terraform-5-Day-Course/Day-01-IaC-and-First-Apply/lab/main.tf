# Change tfclass to YOUR initials so class names do not clash.
resource "azurerm_resource_group" "main" {
  name     = "tfclass-day1-rg"
  location = "eastus"

  tags = {
    course = "terraform-5-day"
    day    = "1"
  }
}
