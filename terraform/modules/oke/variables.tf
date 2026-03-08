variable "compartment_id" {}
variable "vcn_id" {}
variable "subnet_id" {}
variable "availability_domain" {}
variable "node_image" {}

variable "tenancy_ocid" {
  description = "OCI Tenancy OCID"
  type        = string
}