---
title: 'Compliance-to-Code: Enhancing Financial Compliance Checking via Code Generation'
authors:
  - admin
author_notes:
  - ''
date: '2025-05-19T00:00:00Z'
doi: ''
publishDate: '2025-01-01T00:00:00Z'
publication_types: ['paper-conference']
publication: In *arXiv preprint*
publication_short: In *arXiv*
abstract: Regulatory compliance has become a cornerstone of corporate governance, ensuring adherence to systematic legal frameworks. At its core, financial regulations often comprise highly intricate provisions, layered logical structures, and numerous exceptions, which inevitably result in labor-intensive or comprehension challenges. To mitigate this, recent Regulatory Technology (RegTech) and Large Language Models (LLMs) have gained significant attention in automating the conversion of regulatory text into executable compliance logic. However, their performance remains suboptimal particularly when applied to Chinese-language financial regulations, due to three key limitations - (1) incomplete domain-specific knowledge representation, (2) insufficient hierarchical reasoning capabilities, and (3) failure to maintain temporal and logical coherence. To fill these gaps, we present Compliance-to-Code, the first large-scale Chinese dataset dedicated to financial regulatory compliance. Covering 1,159 annotated clauses from 361 regulations across ten categories, each clause is modularly structured with four logical elements—subject, condition, constraint, and contextual information—along with regulation relations. We provide deterministic Python code mappings, detailed code reasoning, and code explanations to facilitate automated auditing. To demonstrate utility, we present FinCheck - a pipeline for regulation structuring, code generation, and report generation.
summary: The first large-scale Chinese dataset for financial regulatory compliance with automated checking pipeline.
tags:
  - Financial Compliance
  - Code Generation
  - Large Language Models
featured: true
links:
  - name: ArXiv
    url: https://arxiv.org/abs/2505.19804
url_pdf: 'https://arxiv.org/pdf/2505.19804.pdf'
url_code: 'https://github.com/AlexJJJChen/Compliance-to-Code'
url_dataset: 'https://huggingface.co/datasets/GPS-Lab/Compliance-to-Code'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
image:
  caption: 'Compliance-to-Code Framework'
  focal_point: ''
  preview_only: false
projects: []
slides: ""
---

## Overview

This paper presents the **Compliance-to-Code** dataset and **FinCheck** compliance checking pipeline, addressing key challenges in Chinese financial regulatory compliance automation.

## Key Contributions

1. **Compliance-to-Code Dataset**: The first large-scale dataset dedicated to Chinese financial regulatory compliance, featuring:
   - 1,159 annotated clauses from 361 regulations across ten categories
   - Each clause modularly structured with four logical elements: subject, condition, constraint, and contextual information
   - 307 executable Python compliance automation tasks with detailed reasoning

2. **FinCheck Pipeline**: An end-to-end automated compliance checking system comprising:
   - Structure Predictor: Parses natural language regulations into Compliance Units (CUs)
   - Code Generator: Translates CU structures into executable Python code
   - Information Retriever: Fetches relevant company data
   - Report Generator: Produces user-friendly compliance assessments

3. **Comprehensive Evaluation**: Establishes strong benchmarks on regulation structuring and code generation tasks, with GLM-4-9B-0414 achieving best performance on regulation structuring and Qwen3-8B performing best on compliance code generation.

## Technical Innovations

- **Modular Compliance Unit Design**: Decomposes complex regulatory clauses into minimal actionable units amenable to computational assessment
- **Multi-layered Relation Annotation**: Annotates logical relations between compliance units to support advanced compositional reasoning  
- **Code Generation Templates**: Creates Python automation tasks based on 68 distinct logic patterns, simulating realistic compliance scenarios

## Results

Experimental evaluation demonstrates significant performance improvements on Chinese financial compliance automation tasks, providing crucial support for RegTech applications in Chinese financial markets.

*This research not only provides a valuable new resource and strong benchmark results but also opens new avenues for developing safer, more scalable, and reliable RegTech solutions.*