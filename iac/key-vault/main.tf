terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.26"
    }
  }

  backend "azurerm" {
  }
}

provider "azurerm" {
  features {}
}

variable "app_name" {
  default   = "ca-t-dbx"
  type      = string
  sensitive = false
}

variable "env" {
  default   = "demo"
  sensitive = false
}

variable "location" {
  default   = "East US 2"
  sensitive = false
  type      = string
}

variable "tags" {
  type = map(string)

  default = {
    environment = "demo"
    workload    = "crypto-analytics"
  }
}

variable "admin_user_principal_name" {
  type        = string
  sensitive   = true
  description = "The user principal name of the admin for the app."
  default     = "mikeg@ish-star.com"
}

locals {
  loc    = lower(replace(var.location, " ", ""))
  a_name = replace(var.app_name, "-", "")
}

data "azurerm_client_config" "current" {}

data "azurerm_resource_group" "rg" {
  name = "dbx-demo-eastus2"
}

data "azuread_user" "admin" {
  user_principal_name = var.admin_user_principal_name
}