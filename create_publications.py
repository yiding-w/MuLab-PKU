#!/usr/bin/env python3
"""
批量创建论文条目的Python脚本
根据提供的论文列表自动生成Hugo格式的publication条目
"""

import os
import re
from pathlib import Path

# 论文数据 - 从您提供的列表中提取
papers_2025 = [
    {
        "title": "CLOVER: Cross-Layer Orthogonal Vectors Pruning and Fine-Tuning",
        "authors": ["F. Meng", "P. Tang", "F. Jiang", "admin"],
        "venue": "ICML-25",
        "venue_full": "Proc. International Conference on Machine Learning (ICML-25)",
        "folder": "icml25-clover",
        "tags": ["Model Compression", "Fine-tuning", "Large Language Models"]
    },
    {
        "title": "Griffin: Towards a Graph-Centric Relational Database Foundation Model",
        "authors": ["Y. Wang", "X. Wang", "Q. Gan", "M. Wang", "Q. Yang", "D. Wipf", "admin"],
        "venue": "ICML-25",
        "venue_full": "Proc. International Conference on Machine Learning (ICML-25)",
        "folder": "icml25-griffin",
        "tags": ["Graph Neural Networks", "Database Systems", "Foundation Models"]
    },
    {
        "title": "Geometric Representation Condition Improves Equivariant Molecule Generation",
        "authors": ["Z. Li", "C. Zhou", "X. Wang", "X. Peng", "admin"],
        "venue": "ICML-25",
        "venue_full": "Proc. International Conference on Machine Learning (ICML-25), spotlight presentation (2.6% acceptance rate)",
        "folder": "icml25-molecule-spotlight",
        "tags": ["Molecule Generation", "Equivariant Networks", "Geometric Deep Learning"],
        "featured": True
    },
    {
        "title": "GOFA: A Generative One-For-All Model for Joint Graph Language Modeling",
        "authors": ["L. Kong", "J. Feng", "H. Liu", "C. Huang", "J. Huang", "Y. Chen", "admin"],
        "venue": "ICLR-25",
        "venue_full": "International Conference on Learning Representations (ICLR-25)",
        "folder": "iclr25-gofa",
        "tags": ["Graph Neural Networks", "Language Models", "Multimodal Learning"]
    },
    {
        "title": "Number Cookbook: Number Understanding of Language Models and How to Improve It",
        "authors": ["H. Yang", "Y. Hu", "S. Kang", "Z. Lin", "admin"],
        "venue": "ICLR-25",
        "venue_full": "International Conference on Learning Representations (ICLR-25)",
        "folder": "iclr25-number",
        "tags": ["Language Models", "Numerical Reasoning", "Model Understanding"]
    },
    {
        "title": "On the Completeness of Invariant Geometric Deep Learning Models",
        "authors": ["Z. Li", "X. Wang", "S. Kang", "admin"],
        "venue": "ICLR-25",
        "venue_full": "International Conference on Learning Representations (ICLR-25)",
        "folder": "iclr25-invariant",
        "tags": ["Geometric Deep Learning", "Invariant Networks", "Theory"]
    }
]

papers_2024 = [
    {
        "title": "PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models",
        "authors": ["F. Meng", "Z. Wang", "admin"],
        "venue": "NeurIPS-24",
        "venue_full": "Advances in Neural Information Processing Systems (NeurIPS-24), spotlight presentation (2.08% acceptance rate)",
        "folder": "neurips24-pissa-spotlight",
        "tags": ["Parameter-Efficient Fine-tuning", "Large Language Models", "Singular Value Decomposition"],
        "featured": True
    },
    {
        "title": "Latent Graph Diffusion: A Unified Framework for Generation and Prediction on Graphs",
        "authors": ["C. Zhou", "X. Wang", "admin"],
        "venue": "NeurIPS-24",
        "venue_full": "Advances in Neural Information Processing Systems (NeurIPS-24)",
        "folder": "neurips24-latent-diffusion",
        "tags": ["Graph Generation", "Diffusion Models", "Graph Neural Networks"]
    },
    {
        "title": "Case-Based or Rule-Based: How Do Transformers Do the Math?",
        "authors": ["Y. Hu", "X. Tang", "H. Yang", "admin"],
        "venue": "ICML-24",
        "venue_full": "Proc. International Conference on Machine Learning (ICML-24)",
        "folder": "icml24-transformer-math",
        "tags": ["Transformers", "Mathematical Reasoning", "Interpretability"]
    },
    {
        "title": "One For All: Towards Training One Graph Model For All Classification Tasks",
        "authors": ["H. Liu", "J. Feng", "L. Kong", "N. Liang", "D. Tao", "Y. Chen", "admin"],
        "venue": "ICLR-24",
        "venue_full": "International Conference on Learning Representations (ICLR-24), spotlight presentation (4.96% acceptance rate)",
        "folder": "iclr24-one-for-all-spotlight",
        "tags": ["Graph Neural Networks", "Multi-task Learning", "Universal Models"],
        "featured": True
    }
]

def create_publication_entry(paper, year):
    """创建单个论文条目"""
    folder_path = Path(f"content/publication/{paper['folder']}")
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # 生成作者列表
    authors_yaml = "\n".join([f"  - {author}" for author in paper['authors']])
    
    # 生成标签
    tags_yaml = "\n".join([f"  - {tag}" for tag in paper['tags']])
    
    # 设置日期
    if year == "2025":
        date = "2025-01-01T00:00:00Z" if "ICLR" in paper['venue'] else "2025-05-01T00:00:00Z"
    else:
        date = f"{year}-01-01T00:00:00Z"
    
    # 是否为特色论文
    featured = "true" if paper.get('featured', False) else "false"
    
    content = f"""---
title: '{paper['title']}'

# Authors
authors:
{authors_yaml}

date: '{date}'
doi: ''

publishDate: '{date}'

publication_types: ['paper-conference']

publication: '{paper['venue_full']}'
publication_short: '{paper['venue']}'

abstract: 'Abstract for {paper['title']}. Please update with actual abstract.'

summary: 'Summary for {paper['title']}. Please update with actual summary.'

tags:
{tags_yaml}

featured: {featured}

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: '{paper['title']}'
  focal_point: ''
  preview_only: false

projects: []
slides: ""
---

Please update this entry with:
1. Actual abstract and summary
2. PDF and other resource links
3. Featured image (add featured.jpg to this folder)
4. Citation file (add cite.bib to this folder)
"""
    
    # 写入文件
    with open(folder_path / "index.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✓ Created: {paper['folder']}")

def main():
    """主函数"""
    print("开始批量创建论文条目...")
    print("\n创建2025年论文:")
    for paper in papers_2025:
        create_publication_entry(paper, "2025")
    
    print("\n创建2024年论文:")
    for paper in papers_2024:
        create_publication_entry(paper, "2024")
    
    print(f"\n✅ 完成！共创建了 {len(papers_2025) + len(papers_2024)} 个论文条目")
    print("\n📝 接下来您需要:")
    print("1. 为每个论文更新实际的abstract和summary")
    print("2. 添加PDF链接和其他资源链接") 
    print("3. 为重要论文添加featured.jpg图片")
    print("4. 添加cite.bib引用文件")
    print("5. 继续添加更多年份的论文")

if __name__ == "__main__":
    main()
