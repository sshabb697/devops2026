module "web" {
  source   = "./modules/web"
  prefix   = var.prefix
  location = var.location
}
