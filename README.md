# PegaOne GPT

PegaOne is an AI-driven assistant designed to accelerate Pega platform adoption, from initial discovery through ongoing operations. It provides ready-to-use examples, reference artifacts, and troubleshooting guidance tailored to any user role or domain expertise.

## Repository Structure
PegaOne/
├── cfg/                       # Configuration files (pegaone_gpt_config.txt)
├── docs/                      # Detailed guides and tutorials
├── packs/                     # Expertise-area and role-based knowledge pack folders
│   ├── blueprint_and_discovery/
│   ├── case_management_and_lifecycle/
│   ├── process_modeling_and_bpmn/
│   └── ... (other 20 areas)
├── zipped_packs/              # Compiled ZIP archives of packs
│   ├── blueprint_and_discovery.zip
│   ├── case_management_and_lifecycle.zip
│   └── ...
├── PegaOneExpertise_packs.zip # Master archive (all packs)
├── README.md                  # This file
├── LICENSE
└── .github/                   # CI/CD workflows and issue templates

## Getting Started

1. **Clone the repository**
    ```
      bash
      git clone https://github.com/marcoafcosta/PegaOne.git
      cd PegaOne
    ```

2. **Download Packs**

Unzip PegaOneExpertise_packs.zip or individual zips in zipped_packs/.

3. **Explore Packs**

## Each pack contains:

docs/: Overview, concepts, scenarios, FAQ, troubleshooting.

workflows/bpmn/: BPMN 2.0 diagrams (.bpmn).

workflows/pega/: Pega XML process rules (_pega.xml).

xml/: Example XML rules with example_schema.xsd.

code/: Java code samples (pom.xml required for Maven builds).

4. **Import & Validate**

BPMN: Open .bpmn files in Camunda Modeler.

XML: Validate with xmllint --noout --schema example_schema.xsd file.xml.

Java: Build with Maven (mvn compile).


