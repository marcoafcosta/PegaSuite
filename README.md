# Pega Suite GPT

Pega Suite is an AI-powered assistant designed to accelerate the adoption and mastery of the Pega platform. It includes curated knowledge packs aligned with the latest platform releases (8.8 through Infinity ’25), covering everything from process modeling to GenAI, deployment automation, and persona-specific guidance.

---

## 📁 Repository Structure

```
PegaSuite/
├── expertise_base_packs/         # Domain knowledge packs (.zip format)
├── role_base_packs/              # Persona-based role packs (.zip format)
├── pega_gpt_knowledge_pack_index.md
├── README.md
├── update_pega_packs.py
├── PegaSuite.png
├── EXTRAS_NO_USE/                # Archived or in-progress experiments
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
gh repo clone marcoafcosta/PegaSuite
cd PegaSuite
```

### 2. Unzip Packs as Needed

You can unzip any `.zip` file under `expertise_base_packs/` or `role_base_packs/` to explore a pack.

```bash
unzip expertise_base_packs/pega_version_alignment.zip -d unpacked/pega_version_alignment/
```

---

## 📦 Knowledge Pack Structure

Each pack (after unzipping) typically contains:

```
pack_name/
├── docs/                    # Concepts, FAQs, templates, tutorials
├── workflows/bpmn/          # BPMN 2.0 models (.bpmn)
├── workflows/pega/          # Pega native XML process files
├── xml/                     # Example rules + schema
├── code/                    # Java or integration examples
```

---

## 🔍 Explore the Full Index

See [`pega_gpt_knowledge_pack_index.md`](./pega_gpt_knowledge_pack_index.md) for a complete list of included expertise and role packs.

---

## 🧭 Highlights in This Release

- 🧠 GenAI & Copilot Enablement
- 🧱 DX API v2 Migration Patterns
- ☁️ Cloud Choice (Kubernetes) + Observability
- 📊 CDH Decisioning + Adaptive Decisioning 2.0
- 🌍 FinOps & Sustainability Packs
- 👥 Role Packs for GenAI Specialists, Cloud FinOps Engineers, Citizen Devs
