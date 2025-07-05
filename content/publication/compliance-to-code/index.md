---
title: "Compliance-to-Code: Enhancing Financial Compliance Checking via Code Generation"
authors:
- admin
- Jian Chen
- Rui Yao
- Xuming Hu
- Peilin Zhou
- Weihua Qiu
- Simin Zhang
- Chucheng Dong
- Zhiyao Li
- Qipeng Xie
- Zixuan Yuan
date: "2025-05-26T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-05-26T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "arXiv preprint"
publication_short: "arXiv"

abstract: "Regulatory compliance is crucial for corporate governance, but financial regulations are often intricate and challenging to interpret. While Large Language Models (LLMs) show promise in automating the conversion of regulatory text to compliance logic, they face limitations with Chinese financial regulations, including incomplete domain knowledge and insufficient reasoning. To address this, we introduce Compliance-to-Code, the first large-scale Chinese dataset for financial regulatory compliance. It contains 1,159 annotated clauses from 361 regulations, structured into logical elements with Python code mappings and detailed reasoning. We also present FinCheck, a pipeline for regulation structuring, code generation, and report generation, demonstrating the dataset's utility."

# Summary. An optional shortened abstract.
summary: "We introduce Compliance-to-Code, the first large-scale Chinese dataset for financial regulatory compliance, with 1,159 annotated clauses from 361 regulations and a pipeline for automated compliance checking."

tags:
- Large Language Models
- Financial Compliance
- Code Generation
- Knowledge Graph

featured: true

links:
- name: Website
  url: https://siyuanli-sven.github.io/compliance-to-code-poster.html
url_pdf: https://arxiv.org/pdf/2505.19804
url_code: 'https://github.com/AlexJJJChen/Compliance-to-Code'
url_dataset: 'https://huggingface.co/datasets/GPS-Lab/Compliance-to-Code'
url_poster: 'https://siyuanli-sven.github.io/compliance-to-code-poster.html'
url_project: 'https://github.com/AlexJJJChen/Compliance-to-Code'
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Compliance-to-Code Project'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- compliance-to-code

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

## Overview

The **Compliance-to-Code** dataset is constructed from 361 authoritative Chinese financial regulations, primarily from the Beijing Stock Exchange (BSE), covering ten core thematic areas. It includes 1,159 annotated Compliance Units (CUs) and 307 executable compliance automation tasks in Python.

## Data Distribution

**Overall Statistics:**
- **Regulations Analyzed:** 361
- **Annotated Clauses (Compliance Units):** 1,159
- **Inter-Unit Relations Annotated:** 864
- **Executable Python Automation Tasks:** 307 (Simple: 70.03%, Medium: 11.07%, Difficult: 18.89%)
- **Average COT Reasoning Steps per Task:** 8
- **Average Tokens per COT Reasoning Step:** 2145

## Key Contributions

1. We propose **Compliance-to-Code**, the first large-scale Chinese financial regulation dataset tailored for code-based compliance reasoning.
2. We develop **FinCheck**, an end-to-end pipeline that leverages the Compliance-to-Code dataset for automated compliance checking.
3. We conduct a comprehensive evaluation of recent LLMs for regulation structuring and code generation tasks, showing that structured decomposition and explicit reasoning are crucial for effective compliance code generation. 