# Cloud Ops / Kubernetes Pack

## Purpose
End-to-end operational guidance for running Pega on Kubernetes—either self-managed or via Pega Cloud services.

## Audience
Platform Engineers · DevOps · SREs · Cloud Architects

## Learning Outcomes
- Size and scale clusters for Pega workloads  
- Deploy using the official Helm charts  
- Automate CI/CD with GitHub Actions & Deployment Manager  
- Monitor health and performance  
- Execute zero-downtime upgrades and disaster-recovery drills

## Modules
See `modules/` for detailed content:
1. Kubernetes Fundamentals for Pega  
2. Helm Chart Deep Dive  
3. Sizing & Scaling  
4. CI/CD Pipelines  
5. Observability & Alerting  
6. Backup & Disaster Recovery  
7. Security & Secrets Management  
8. Upgrade / Blue-Green Strategies  
9. Troubleshooting Cheat-Sheet

## Assets
- Mermaid diagrams (`/assets/diagrams/`)  
- Sample YAML & Terraform (`/assets/code-samples/`)  
- Performance-tuning checklist  
- Video walk-throughs

## Prerequisites
- Basic Pega deployment knowledge  
- Kubernetes 101

## Contribution Guide
1. Fork → branch → PR.  
2. Follow the doc template in `.github/CONTRIBUTING.md`.  
3. Run `npm run lint:md` before committing.

## Maintainers
@cloud-ops-lead · @devops-sme
