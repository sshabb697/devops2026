terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "eu-west-1"
}

variable "bucket_name" {
  type        = string
  description = "Globally unique S3 bucket name (add initials + date)."
}

resource "aws_s3_bucket" "demo" {
  bucket = var.bucket_name
  tags = {
    Project = "aws-class"
  }
}

resource "aws_s3_bucket_versioning" "demo" {
  bucket = aws_s3_bucket.demo.id
  versioning_configuration {
    status = "Enabled"
  }
}

output "bucket_arn" {
  value = aws_s3_bucket.demo.arn
}
