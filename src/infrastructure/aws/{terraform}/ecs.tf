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

# DESIGN ONLY - Not for deployment
resource "aws_ecs_cluster" "design_proof" {
  name = "notes-api-cluster"  # Theoretical resource
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
  tags = {
    Purpose = "Academic design exercise - CMP9785M"
  }
}

# Theoretical output (reference in Design Doc p.7)
output "cluster_name" {
  value = aws_ecs_cluster.design_proof.name
}