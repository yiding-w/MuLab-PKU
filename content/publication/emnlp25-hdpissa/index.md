---
title: 'HD-PiSSA: High-Rank Distributed Orthogonal Adaptation'

# Authors
authors:
  - Y. Wang
  - F. Meng 
  - X. Zhang
  - F. Jiang
  - P. Tang
  - M. Zhang

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''
  - 'Corresponding author'

date: '2025-09-15T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-09-15T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['EMNLP 2025 (Oral)']

# Publication name and optional abbreviated publication name.
publication: 'Proc. The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP-25)'
publication_short: 'EMNLP-25'

abstract: 'Existing parameter-efficient fine-tuning (PEFT) methods for large language models (LLMs), such as LoRA and PiSSA, constrain model updates to low-rank subspaces, limiting their expressiveness and leading to suboptimal performance on complex tasks. To address this, we introduce High-rank Distributed PiSSA (HD-PiSSA), a distributed PEFT approach that initializes orthogonal adapters across different devices and aggregates their delta updates collectively on W for fine-tuning. Unlike Data Parallel LoRA or PiSSA, which maintain identical adapters across all devices, HD-PiSSA assigns different principal components of the pre-trained weights to each GPU, significantly expanding the range of update directions. This results in over 16x higher effective updated ranks than data-parallel LoRA or PiSSA when fine-tuning on 8 GPUs with the same per-device adapter rank. Empirically, we evaluate HD-PiSSA across various challenging downstream tasks, including mathematics, code generation, and multi-task learning. In the multi-task setting, HD-PiSSA achieves average gains of 10.0 absolute points (14.63%) over LoRA and 4.98 points (6.60%) over PiSSA across 12 benchmarks, demonstrating its benefits from the extra optimization flexibility.'

# Summary. An optional shortened abstract.
summary: 'High-rank updates under data parallel fine-tuning.'

tags:
  - Fine-tuning
  - Large Language Models

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2505.18777'
url_code: 'https://github.com/MuLabPKU/HD-PiSSA'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
