terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.117"
    }
  }
}

provider "azurerm" {
  features {}
  # If init pulls azurerm 4.x and apply asks for subscription_id, uncomment:
  # subscription_id = "00000000-0000-0000-0000-000000000000"
}
