#!/bin/bash

# 批量创建论文条目的脚本
# 用法: 您可以根据这个模板快速创建更多论文条目

echo "正在创建论文条目..."

# 2025年ICLR论文示例
mkdir -p content/publication/iclr25-gofa
cat > content/publication/iclr25-gofa/index.md << 'EOF'
---
title: 'GOFA: A Generative One-For-All Model for Joint Graph Language Modeling'

authors:
  - L. Kong
  - J. Feng
  - H. Liu
  - C. Huang
  - J. Huang
  - Y. Chen
  - admin

date: '2025-01-23T00:00:00Z'
publishDate: '2025-01-23T00:00:00Z'

publication_types: ['paper-conference']

publication: 'International Conference on Learning Representations (ICLR-25)'
publication_short: 'ICLR-25'

abstract: 'GOFA presents a generative one-for-all model that unifies graph and language modeling, enabling joint understanding and generation across graph and text modalities.'

summary: 'A unified generative model for joint graph language modeling accepted at ICLR-25.'

tags:
  - Graph Neural Networks
  - Language Models
  - Multimodal Learning

featured: true

url_pdf: ''
projects: []
slides: ""
---
EOF

mkdir -p content/publication/iclr25-number
cat > content/publication/iclr25-number/index.md << 'EOF'
---
title: 'Number Cookbook: Number Understanding of Language Models and How to Improve It'

authors:
  - H. Yang
  - Y. Hu
  - S. Kang
  - Z. Lin
  - admin

date: '2025-01-23T00:00:00Z'
publishDate: '2025-01-23T00:00:00Z'

publication_types: ['paper-conference']

publication: 'International Conference on Learning Representations (ICLR-25)'
publication_short: 'ICLR-25'

abstract: 'This work systematically studies number understanding in language models and proposes effective methods to improve numerical reasoning capabilities.'

summary: 'Comprehensive study and improvement methods for number understanding in language models.'

tags:
  - Language Models
  - Numerical Reasoning
  - Model Understanding

featured: true

url_pdf: ''
projects: []
slides: ""
---
EOF

echo "论文条目创建完成！"
echo "您可以继续按照这个模板创建更多论文条目。"
echo ""
echo "每个论文需要："
echo "1. 在 content/publication/ 下创建一个文件夹（建议命名格式：venue年份-简短名称）"
echo "2. 在文件夹内创建 index.md 文件"
echo "3. 可选：添加 featured.jpg 作为论文特色图片"
echo "4. 可选：添加 cite.bib 文件包含引用信息"
