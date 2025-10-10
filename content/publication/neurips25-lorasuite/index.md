---
title: 'LoRASuite: Efficient LoRA Adaptation Across Large Language Model Upgrades'

authors:
  - Y. Li
  - F. Meng
  - M. Zhang
  - S. Zhu
  - S. Wang
  - M. Xu

author_notes:
  - ''
  - ''
  - 'Corresponding author'
  - ''
  - ''
  - ''

date: '2025-10-09T00:00:00Z'
publishDate: '2025-10-09T00:00:00Z'

publication_types: ['paper-conference']

publication: 'Advances in Neural Information Processing Systems (NeurIPS-25)'
publication_short: 'NeurIPS-25'

abstract: 'As Large Language Models (LLMs) are frequently updated, LoRA weights trained on earlier versions quickly become obsolete. The conventional practice of retraining LoRA weights from scratch on the latest model is costly, time-consuming, and environmentally detrimental, particularly as the diversity of LLMs and downstream tasks expands. This motivates a critical question: "How can we efficiently leverage existing LoRA weights to adapt to newer model versions?" To address this, we propose LoRASuite, a modular approach tailored specifically to various types of LLM updates. First, we compute a transfer matrix utilizing known parameters from both old and new LLMs. Next, we allocate corresponding layers and attention heads based on centered kernel alignment and cosine similarity metrics, respectively. A subsequent small-scale, skillful fine-tuning step ensures numerical stability. Experimental evaluations demonstrate that LoRASuite consistently surpasses small-scale vanilla LoRA methods. Notably, on backbone LLMs such as MiniCPM and Qwen, LoRASuite even exceeds the performance of full-scale LoRA retraining, with average improvements of +1.4 and +6.6 points on math tasks, respectively. Additionally, LoRASuite significantly reduces memory consumption by 5.5 GB and computational time by 78.23%.'

featured: false

url_pdf: 'https://arxiv.org/pdf/2505.13515'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
projects: []
slides: ""
---