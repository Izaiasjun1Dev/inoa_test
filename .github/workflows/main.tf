
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "app-invest-server" {
  ami             = "ami-09e67e426f25ce0d7"
  instance_type   = "t2.micro"
  key_name        = "terraform-aws"

  vpc_security_group_ids = ["sg-d05ed2ce"]

  tags = {
    Name = "app-server"
  }
}

resource "aws_security_group" "acesso_ssh" {
  name = "acesso_ssh"
  description = "acesso_ssh"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "acesso_ssh"
  }
}
