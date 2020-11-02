variable "aws_account_id" {}
variable "aws_profile" {}
variable "aws_region" {}

variable "bucket_prefix" {
  default = "config"
}

variable "bucket_key_prefix" {
  default = "config"
}

variable "sns_topic_arn" {
  default = "arn:aws:sns:eu-west-1:889199313043:okulagin-sns-ireland"
}

variable "tags" {
  default = {
    "owner"   = "okulagin"
    "project" = "intra"
    "client"  = "Internal"
  }
}
