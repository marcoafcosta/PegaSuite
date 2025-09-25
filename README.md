# Pega Suite GPT

Pega Suite is an AI-driven assistant designed to accelerate Pega platform adoption—from initial discovery through ongoing operations. It provides ready-to-use examples, reference artifacts, and troubleshooting guidance tailored to any user role or domain expertise.

Pega Suite is **up-to-date with the Pega 8.8 → 24.x platform**, and fully aligned with **Pega Infinity ’25** feature roadmap, including:
- Constellation UI & DX API v2
- Pega GenAI™ & Copilot capabilities
- Adaptive Decisioning 2.0
- Cloud Choice & Kubernetes deployments
- FinOps & Sustainability optimization
- New roles such as GenAI Specialist & Citizen Developers

---

## 📁 Repository Structure

```
PegaSuite/
├── cfg/
├── docs/
├── packs/
│   ├── constellation_ui_and_dxapi/
│   ├── genai_and_copilot_enablement/
│   ├── pega_version_alignment/
│   ├── pega_marketplace_and_components/
│   ├── business_agility_and_process_fabric/
│   ├── sustainability_and_finops/
│   ├── decisioning_and_next_best_action/
│   ├── ai_ml_and_predictive_analytics/
│   ├── cloud_and_pega_cloud_services/
│   ├── devops_and_deployment_automation/
│   └── roles/
│       ├── ai_genai_specialist/
│       ├── cloud_finops_engineer/
│       └── low_code_citizen_developer/
├── zipped_packs/
│   ├── master.zip
│   ├── constellation_ui_and_dxapi.zip
│   ├── genai_and_copilot_enablement.zip
│   ├── pega_version_alignment.zip
│   ├── pega_marketplace_and_components.zip
│   ├── business_agility_and_process_fabric.zip
│   ├── sustainability_and_finops.zip
│   ├── decisioning_and_next_best_action.zip
│   ├── ai_ml_and_predictive_analytics.zip
│   ├── cloud_and_pega_cloud_services.zip
│   ├── devops_and_deployment_automation.zip
│   ├── roles_ai_genai_specialist.zip
│   ├── roles_cloud_finops_engineer.zip
│   ├── roles_low_code_citizen_developer.zip
├── pega_gpt_knowledge_pack_index.md
├── README.md
├── LICENSE
└── .github/
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
gh repo clone marcoafcosta/PegaSuite
cd PegaSuite
```

### 2. Download Knowledge Packs

To extract all packs at once:

```bash
unzip zipped_packs/master.zip -d packs/
```

Or extract individual archives:

```bash
unzip zipped_packs/<pack_name>.zip -d packs/
```

## 📦 Explore the Packs

Each pack provides focused guidance, templates, and examples for a specific area of the Pega platform (architecture, automation, AI, UI, DevOps, and more).

## 🧱 Pack Folder Layout

Each pack follows this structure:

```
pack_name/
├── docs/
├── workflows/bpmn/
├── workflows/pega/
├── xml/
├── code/
```

## 🧪 Validate or Test

**BPMN** — Open `.bpmn` files in Camunda Modeler  
**XML** — Validate with:

```bash
xmllint --noout --schema example_schema.xsd <file>.xml
```

**Java** — Compile with:

```bash
mvn compile
```

## 🧭 What's New

- ✅ GenAI & Copilot enablement
- ✅ DX API v2 migration
- ✅ Infinity ’25 alignment
- ✅ Cloud Choice deployment
- ✅ FinOps & Sustainability packs
- ✅ Role packs: GenAI Specialist, FinOps Engineer, Citizen Dev
