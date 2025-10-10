---
title: 'Improving Graph Neural Networks on Multi-node Tasks with the Labeling Trick'

authors:
  - X. Wang
  - P. Li
  - M. Zhang

author_notes:
  - ''
  - ''
  - 'Corresponding author'

date: '2025-01-01T00:00:00Z'
publishDate: '2025-01-01T00:00:00Z'

publication_types: ['article-journal']

publication: 'Journal of Machine Learning Research (JMLR-25)'
publication_short: 'JMLR-25'

abstract: 'In this paper, we study using graph neural networks (GNNs) for \textit{multi-node representation learning}, where a representation for a set of more than one node (such as a link) is to be learned. Existing GNNs are mainly designed to learn single-node representations. When used for multi-node representation learning, a common practice is to directly aggregate the single-node representations obtained by a GNN. In this paper, we show a fundamental limitation of such an approach, namely the inability to capture the dependence among multiple nodes in the node set. A straightforward solution is to distinguish target nodes from others. Formalizing this idea, we propose \text{labeling trick}, which first labels nodes in the graph according to their relationships with the target node set before applying a GNN and then aggregates node representations obtained in the labeled graph for multi-node representations. Besides node sets in graphs, we also extend labeling tricks to posets, subsets and hypergraphs. Experiments verify that the labeling trick technique can boost GNNs on various tasks, including undirected link prediction, directed link prediction, hyperedge prediction, and subgraph prediction. Our work explains the superior performance of previous node-labeling-based methods and establishes a theoretical foundation for using GNNs for multi-node representation learning.'

featured: false

url_pdf: 'https://arxiv.org/pdf/2304.10074'
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