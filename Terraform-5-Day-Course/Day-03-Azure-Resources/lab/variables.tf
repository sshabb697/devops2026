variable "prefix" {
  type        = string
  description = "Lowercase letters only, used in Azure names."
}

variable "location" {
  type    = string
  default = "eastus"
}
