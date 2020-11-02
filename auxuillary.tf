provider "aws" {
  region = "eu-west-1"
}


resource "aws_instance" "small" {
  ami = "ami-0bb3fad3c0286ebd5"
  instance_type = "t2.nano"

  dynamic "ebs_block_device" {
    for_each = ["/dev/sdf","/dev/sdg","/dev/sdh"]
    content {
      device_name = ebs_block_device.value
      delete_on_termination = true
      volume_size = 11
    }
  }

  lifecycle {
    ignore_changes = all
  }


}

