variable "rg_name" {
  type        = string
  description = "Resource group name. Must be unique in the subscription."
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "owner" {
  type    = string
  default = "student"
}
