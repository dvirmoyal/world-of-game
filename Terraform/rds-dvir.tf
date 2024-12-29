provider "aws" {
  region = "us-east-1"
}

resource "aws_db_instance" "my-app-rds" {
  allocated_storage    = 20
  db_subnet_group_name = "dvir-db-subnet-group"
  engine              = "mysql"
  engine_version      = "8.0"
  identifier          = "my-app-rds"
  db_name = "worldofgame"
  instance_class      = "db.t3.micro"
  password            = "rootroot"
  skip_final_snapshot = true
  storage_encrypted   = true
  publicly_accessible = false
  username           = "root"
  apply_immediately  = true
  vpc_security_group_ids = ["sg-0ae3c0a261913799a"]
}