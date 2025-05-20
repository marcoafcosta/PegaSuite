# PegaOne GPT

PegaOne is an AI-driven assistant designed to accelerate Pega platform adoption—from initial discovery through ongoing operations. It provides ready-to-use examples, reference artifacts, and troubleshooting guidance tailored to any user role or domain expertise.

## Repository Structure

```
PegaOne/
├── cfg/                             # Configuration files (`pegaone_gpt_config.txt`)
├── docs/                            # Detailed guides and tutorials
├── packs/                           # Knowledge packs (see `pega_gpt_knowledge_pack_index.md` for full list)
│   ├── blueprint_and_discovery/
│   ├── case_management_and_lifecycle/
│   ├── process_modeling_and_bpmn/
│   └── ...                          # 25 total packs, including new areas (accessibility, services, troubleshooting)
├── zipped_packs/                    # ZIP archives of individual packs and master archive
│   ├── master.zip                   # All packs in one archive
│   ├── blueprint_and_discovery.zip
│   └── ...                          # Individual pack archives
├── pega_gpt_knowledge_pack_index.md # Index of all available knowledge packs
├── README.md                        # This file
├── LICENSE                          # Repository license
└── .github/                         # CI/CD workflows and issue templates
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/marcoafcosta/PegaOne.git
cd PegaOne
```

### 2. Download Packs

* To extract all packs at once:

  ```bash
  unzip zipped_packs/master.zip -d packs/
  ```
* Or unzip individual archives:

  ```bash
  unzip zipped_packs/<pack_name>.zip -d packs/
  ```

### 3. Explore Packs

Each pack provides focused guidance, examples, and artifacts for a specific domain area of the Pega Platform.

## Pack Structure

Every knowledge pack follows this layout:

* `docs/`             : Overview, concepts, scenarios, FAQs, and troubleshooting tips
* `workflows/bpmn/`   : BPMN 2.0 process diagrams (`.bpmn` files)
* `workflows/pega/`   : Pega XML process rules (`*_pega.xml` files)
* `xml/`              : Example XML rule definitions with accompanying XSD schema
* `code/`             : Java code snippets and Maven project descriptors (e.g., `pom.xml`)

## Import & Validate

* **BPMN**: Open `.bpmn` files in Camunda Modeler or any BPMN 2.0–compliant tool.
* **XML**: Validate rules against the provided schema:

  ```bash
  xmllint --noout --schema example_schema.xsd <file>.xml
  ```
* **Java**: Build and compile samples using Maven:

  ```bash
  mvn compile
  ```

---

