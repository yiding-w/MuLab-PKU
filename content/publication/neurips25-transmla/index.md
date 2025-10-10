---
title: 'TransMLA: Migrating GQA Models to MLA with Full DeepSeek Compatibility and Speedup'

authors:
  - F. Meng
  - P. Tang
  - Z. Yao
  - X. Sun
  - M. Zhang

author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''
  - 'Corresponding author'

date: '2025-01-01T00:00:00Z'
publishDate: '2025-01-09T00:00:00Z'

publication_types: ['paper-conference']

publication: 'Advances in Neural Information Processing Systems (NeurIPS-25), spotlight presentation'
publication_short: 'NeurIPS-25'

abstract: "In this paper, we present TransMLA, a framework that seamlessly converts any GQA-based pre-trained model into an MLA-based model. Our approach enables direct compatibility with DeepSeek's codebase, allowing these models to fully leverage DeepSeek-specific optimizations such as vLLM and SGlang. By compressing 93% of the KV cache in LLaMA-2-7B, TransMLA achieves a 10.6x inference speedup at an 8K context length while preserving meaningful output quality. Additionally, the model requires only 6 billion tokens for fine-tuning to regain performance on par with the original across multiple benchmarks. TransMLA offers a practical solution for migrating GQA-based models to the MLA structure. When combined with DeepSeek's advanced features, such as FP8 quantization and Multi-Token Prediction, even greater inference acceleration can be realized."

featured: true

url_pdf: 'https://arxiv.org/pdf/2502.07864'
url_code: 'https://github.com/fxmeng/TransMLA'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
projects: []
slides: ""
---