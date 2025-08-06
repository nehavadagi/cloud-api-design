terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_ecs_cluster" "api_cluster" {
  name = "notes-api-cluster"
}

resource "aws_appautoscaling_target" "api_scaling" {
  service_namespace  = "ecs"
  resource_id        = "service/${aws_ecs_cluster.api_cluster.name}/notes-api"
  scalable_dimension = "ecs:service:DesiredCount"
  min_capacity       = 1
  max_capacity       = 10
}
