---
title: 'CLOVER: Cross-Layer Orthogonal Vectors Pruning and Fine-Tuning'

# Authors
authors:
  - F. Meng
  - P. Tang  
  - F. Jiang
  - M. Zhang

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - 'Corresponding author'

date: '2025-05-01T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-05-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: 'Proc. International Conference on Machine Learning (ICML-25)'
publication_short: 'ICML-25'

abstract: 'Decoder-only models generate tokens autoregressively by caching key/value vectors, but as the cache grows, inference becomes memory-bound. To address this issue, we introduce CLOVER (Cross-Layer Orthogonal Vectors), a novel approach that treats pairs of attention layers as a set of low-rank decompositions. CLOVER applies Singular Value Decomposition (SVD) to the \( Q \)-\( K \) and \( V \)-\( O \) pairs within each attention head. The resulting singular values can either guide pruning or serve as trainable parameters for efficient fine-tuning of all orthogonal vectors. After pruning or fine-tuning, these values are reintegrated into the model without increasing its parameter count. We apply CLOVER to various models, including GPT-2 XL, DeepSeek-V2-Lite, Whisper-Large-v3, Stable Diffusion XL, and LLaMA-3.2-11B-Vision. Our results demonstrate that CLOVER significantly improves pruning efficiency. For instance, the perplexity of pruning 70\% of the \( Q \)-\( K \) pairs in GPT-2 XL is similar to that of pruning just 8\% with vanilla methods. Fine-tuning the singular values further results in a full-rank update, outperforming state-of-the-art methods (LoRA, DoRA, HiRA, and PiSSA) by 7.6\%, 5.5\%, 3.8\%, and 0.7\%, respectively, on eight commonsense tasks for LLaMA-2 7B.'


# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2411.17426'
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
