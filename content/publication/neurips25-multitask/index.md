---
title: 'Beyond Single-Task: Robust Multi-Task Length Generalization for LLMs'

authors:
  - Y. Hu
  - S. Kang
  - H. Yang
  - H. Xu
  - M. Zhang

author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - 'Corresponding author'

date: '2025-10-09T00:00:00Z'
publishDate: '2025-10-09T00:00:00Z'

publication_types: ['paper-conference']

publication: 'Advances in Neural Information Processing Systems (NeurIPS-25)'
publication_short: 'NeurIPS-25'

abstract: 'Length generalization, the ability to solve problems longer than those seen during training, remains a critical challenge for large language models (LLMs). Previous work modifies positional encodings (PEs) and data formats to improve length generalization on specific symbolic tasks such as addition and sorting. However, these approaches are fundamentally limited to special tasks, often degrading general language performance. Furthermore, they are typically evaluated on small transformers trained from scratch on single tasks and can cause performance drop when applied during post-training stage of practical LLMs with general capabilities. Hu et al., (2024) proposed Rule-Following Fine-Tuning (RFFT) to improve length generalization in the post-training stage of LLMs. Despite its compatibility with practical models and strong performance, RFFT is proposed for single tasks too, requiring re-training for each individual task with extensive examples. In this paper, we study length generalization in multi-task settings and propose Meta Rule-Following Fine-Tuning (Meta-RFFT), the first framework enabling robust cross-task length generalization. As our first contribution, we construct a large length generalization dataset containing 86 tasks spanning code execution, number processing, symbolic and logical reasoning tasks, beyond the common addition or multiplication tasks. Secondly, we show that cross-task length generalization is possible with Meta-RFFT. After training on a large number of tasks and instances, the models achieve remarkable length generalization ability on unseen tasks with minimal fine-tuning or one-shot prompting. For example, after fine-tuning on 1 to 5 digit addition, our 32B model achieves 95% accuracy on 30 digit addition, significantly outperforming the state-of-the-art reasoning models (DeepSeek-R1-671B: 72%), despite never seeing this task during RF-pretraining.'

featured: false

url_pdf: 'https://arxiv.org/pdf/2502.11525'
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