---
title: 'KnowMT-Bench: Benchmarking Knowledge-Intensive Long-Form Question Answering in Multi-Turn Dialogues'
authors:
  - Junhao Chen
  - Yu Huang
  - admin
  - Rui Yao
  - Hanqian Li
  - Hanyu Zhang
  - Jungang Li
  - Jian Chen
  - Bowen Wang
  - Xuming Hu
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''
  - ''
date: '2024-09-26T00:00:00Z'
doi: '10.48550/arXiv.2509.21856'
publishDate: '2024-09-26T00:00:00Z'
publication_types: ['paper-conference']
publication: In *arXiv preprint*
publication_short: In *arXiv*
abstract: 'Multi-Turn Long-Form Question Answering (MT-LFQA) is a key application paradigm of Large Language Models (LLMs) in knowledge-intensive domains. However, existing benchmarks are limited to single-turn dialogue, while multi-turn dialogue benchmarks typically assess other orthogonal capabilities rather than knowledge-intensive factuality. To bridge this critical gap, we introduce KnowMT-Bench, the "first-ever" benchmark designed to systematically evaluate MT-LFQA for LLMs across knowledge-intensive fields, including medicine, finance, and law. To faithfully assess the model''s real-world performance, KnowMT-Bench employs a dynamic evaluation setting where models generate their own multi-turn dialogue histories given logically progressive question sequences. The factual capability and information delivery efficiency of the "final-turn" answer are then evaluated using a human-validated automated pipeline. Our experiments reveal that multi-turn contexts degrade performance: factual capability declines due to the contextual noise from self-generated histories, while information efficiency drops as models become more verbose with increasing dialogue length. We then investigate mitigation strategies, demonstrating that retrieval-augmented generation (RAG) can effectively alleviate and even reverse this factual degradation. These findings underscore the importance of our benchmark in evaluating and enhancing the conversational factual capabilities of LLMs in real-world knowledge-intensive applications.'
summary: First-ever benchmark for evaluating multi-turn long-form question answering in knowledge-intensive domains.
tags:
  - Large Language Models
  - Multi-Turn Dialogue
  - Knowledge-Intensive QA
  - Benchmark
  - RAG
featured: true
links:
  - name: ArXiv
    url: https://arxiv.org/abs/2509.21856
url_pdf: 'https://arxiv.org/pdf/2509.21856.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
image:
  caption: 'KnowMT-Bench: Multi-Turn Knowledge-Intensive QA Framework'
  focal_point: ''
  preview_only: false
projects: []
slides: ""
---

## Abstract

Multi-Turn Long-Form Question Answering (MT-LFQA) is a key application paradigm of Large Language Models (LLMs) in knowledge-intensive domains. However, existing benchmarks are limited to single-turn dialogue, while multi-turn dialogue benchmarks typically assess other orthogonal capabilities rather than knowledge-intensive factuality.

This paper introduces **KnowMT-Bench**, the first-ever benchmark designed to systematically evaluate MT-LFQA for LLMs across knowledge-intensive fields, including medicine, finance, and law.

## Key Contributions

- **首个多轮对话知识密集型基准**: 填补了现有基准在多轮对话场景下知识密集型问答评估的空白
- **动态评估设置**: 模型需要基于逻辑递进的问题序列生成自己的多轮对话历史
- **全面的评估维度**: 评估最终轮次答案的事实能力和信息传递效率
- **人工验证的自动化管道**: 确保评估结果的可靠性

## Methodology

### 基准设计
- **领域覆盖**: 医学、金融、法律等知识密集型领域
- **评估方式**: 动态生成多轮对话历史，评估最终答案质量
- **评估指标**: 事实准确性和信息传递效率

### 主要发现
1. **性能退化现象**: 多轮上下文会导致模型性能下降
2. **事实能力下降**: 自生成历史引入的上下文噪声影响事实准确性
3. **信息效率降低**: 随着对话长度增加，模型变得更加冗长

### 缓解策略
- **检索增强生成(RAG)**: 能够有效缓解甚至逆转事实退化问题
- **上下文管理**: 优化多轮对话中的信息传递效率

## Impact

该基准对于评估和增强LLM在现实世界知识密集型应用中的对话事实能力具有重要意义，为相关研究和应用提供了标准化的评估工具。