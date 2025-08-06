# Cloud Notes API Design Proposal

## Architecture Overview
```mermaid
graph TD
    A[Client] --> B[Cloudflare CDN]
    B --> C[AWS ALB]
    C --> D[ECS Fargate]
    D --> E[Aurora PostgreSQL]
    D --> F[ElastiCache Redis]