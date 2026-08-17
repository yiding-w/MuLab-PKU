---
title: 'Round-trip Reinforcement Learning: Self-Consistent Training for Better Chemical LLMs'
authors: [L. Kong, X. Wang, Y. Chen, M. Zhang]
date: '2026-10-06T00:00:00Z'
publishDate: '2026-10-06T00:00:00Z'
publication_types: ['paper-conference']
publication: 'Proc. Conference on Language Modeling (COLM-26)'
publication_short: 'COLM-26'
abstract: "Large Language Models (LLMs) are emerging as versatile foundation models for computational chemistry, handling bidirectional tasks like reaction prediction and retrosynthesis. However, these models often lack round-trip consistency. For instance, a state-of-the-art chemical LLM may successfully caption a molecule, yet be unable to accurately reconstruct the original structure from its own generated text. This inconsistency suggests that models are learning unidirectional memorization rather than flexible mastery. Indeed, recent work has demonstrated a strong correlation between a model's round-trip consistency and its performance on the primary tasks. This strong correlation reframes consistency into a direct target for model improvement. We therefore introduce Round-Trip Reinforcement Learning (RTRL), a novel framework that trains a model to improve its consistency by using the success of a round-trip transformation as a reward signal. We further propose an iterative variant where forward and reverse mappings alternately train each other in a self-improvement loop, a process that is highly data-efficient and notably effective with the massive amount of unlabelled data common in chemistry. Experiments demonstrate that RTRL significantly boosts performance and consistency over strong baselines across supervised, self-supervised, and synthetic data regimes. This work shows that round-trip consistency is not just a desirable property but a trainable objective, offering a new path toward more robust and reliable foundation models."
featured: false
url_pdf: 'https://arxiv.org/pdf/2510.01527'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
projects: []
slides: ''
---
