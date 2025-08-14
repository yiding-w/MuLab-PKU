---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
  
          <div style="flex: 1; min-width: 200px;">
            <img src="logo.png" alt="Logo" style="max-width: 100%; height: auto;">
          </div>
  
          <div style="flex: 2; min-width: 250px;">
            <h2 style="font-weight: bold; font-size: 1.8rem; color: #090a0aff; margin-bottom: 1rem;">
              Welcome to Muhan's Research Lab!
            </h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #4b5563;">
              <strong>Mμ Lab</strong> is dedicated to pursuing principled and transformative research in <strong>artificial intelligence</strong> and <strong>machine learning</strong>. While our current focus spans <strong>graph learning</strong> and <strong>large language models</strong>, our long-term mission is broader: to accelerate the development of <strong>artificial general intelligence (AGI)</strong> and deepen the scientific understanding of intelligence itself. We strive to combine <strong>theoretical rigor</strong> with practical impact, designing algorithms that are not only powerful but also <strong>explainable</strong>, <strong>efficient</strong>, and <strong>generalizable</strong> across diverse dimensions.
              Our research vision is to tackle foundational challenges—spanning <strong>model architectures</strong>, <strong>reasoning</strong>, <strong>memory</strong>, <strong>multi-modal intelligence</strong>, and <strong>AI for science</strong>—that push the boundaries of what machines can achieve. Mμ Lab is a place for creative, passionate, and ambitious researchers who aim to produce work that stands the test of time, advances the science of AI, and benefits society in profound ways.
            </p>
          </div>
  
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['40px', '0', '40px', '0']


  - block: markdown
    content:
      subtitle: ""
      text: |
        <div style="text-align: center; margin-bottom: 3rem;">
          <h2 style="font-size: 2rem; font-weight: 600; color: #1f2937; margin: 0;">Research Interests</h2>
        </div>

        <div style="display: flex; justify-content: space-evenly; align-items: flex-start; gap: 2rem; margin-bottom: 3rem; max-width: 1400px; margin-left: auto; margin-right: auto;">
          <!-- Left Column: Graph Machine Learning -->
          <div style="flex: 1; min-width: 500px; max-width: 700px; padding: 1rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
              <span style="font-size: 2rem; margin-right: 0.8rem;">🔗</span>
              <h3 style="font-weight: 600; font-size: 1.5rem; color: #1f2937; margin: 0;">Graph Machine Learning</h3>
            </div>
            <p style="color: #4b5563; line-height: 1.7;">
              Many real-world problems are inherently graph-structured, such as social networks, biological networks, the World Wide Web, molecules, circuits, brains, road networks, and knowledge graphs. Many machine learning algorithms are also defined on graphs, such as neural networks and graphical models. In this field, we develop algorithms and theories for learning over graphs, and apply them to problems like link prediction, graph classification, graph structure optimization, and knowledge graph reasoning. We are also interested in practical applications of graph neural networks, including brain modeling, drug discovery, circuit design, and healthcare applications.
            </p>
          </div>

          <!-- Divider -->
          <div style="width: 1px; background-color: #d1d5db; margin: 0 2rem;"></div>

          <!-- Right Column: Large Language Models -->
          <div style="flex: 1; min-width: 500px; max-width: 700px; padding: 1rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
              <span style="font-size: 2rem; margin-right: 0.8rem;">🤖</span>
              <h3 style="font-weight: 600; font-size: 1.5rem; color: #1f2937; margin: 0;">Large Language Models</h3>
            </div>
            <p style="color: #4b5563; line-height: 1.7;">
              Compared to machines, humans possess extreme flexibility in handling unseen tasks in a few-shot/zero-shot way, much of which is attributed to human system-II intelligence for complex logical reasoning, task planning, causal reasoning, and inductive generalization. Large language models (LLMs) have shown unprecedented improvement in such abilities, but still face challenges in top human-level tasks, such as scientific innovation, software engineering, long-form writing, and autonomous agents. In this field, we aim to:
            </p>
            <p style="color: #4b5563; line-height: 1.7;">
              <strong>a)</strong> Design next-generation LLM architectures with long-term memory, human-like learning mechanisms, fast training/inference, and superior long-context abilities.  
              <br><br>
              <strong>b)</strong> Improve LLMs' reasoning ability to match or surpass humans in the most complex tasks.  
              <br><br>
              <strong>c)</strong> Explore LLMs' integration with various modalities, such as graphs, code, relational databases (RDB), images, and videos.
            </p>
          </div>
        </div>
    design:
      columns: '2'
      background:
        gradient: false
        color: light
      spacing:
        padding: ['50px', '0', '50px', '0']
  
  - block: markdown
    content:
      title: Latest News
      subtitle: ''
      text: |
        <div style="font-size: 0.95rem; line-height: 1.8;">
          <p><strong>5/1/2025:</strong> Three papers accepted at <strong>ICML-25</strong>! Congrats to Fanxu, Yanbo and Zian! 🎉</p>
          <p><strong>1/23/2025:</strong> Three papers accepted at <strong>ICLR-25</strong>! Congrats to Lecheng, Haotong and Zian! 🎉</p>
          <p><strong>1/20/2025:</strong> Collaborated with RedNote and released <strong>RedStar</strong>, a long-chain-of-thought O1-like model for complex reasoning. <a href="https://arxiv.org/pdf/2501.11284" style="color: #2563eb;">See the preprint</a>.</p>
          <p><strong>12/18/2024:</strong> Released <strong>LIFT</strong>, a new paradigm to address long context problems of LLMs by fine-tuning long input into model parameters. <a href="https://arxiv.org/pdf/2412.13626" style="color: #2563eb;">See the preprint</a>.</p>
          <p><strong>11/7/2024:</strong> Open-sourced <strong>NUPA</strong> studying the Numerical Understanding and Processing Abilities of LLMs with 4 numerical representations and 17 distinct tasks.</p>
          <p><strong>9/26/2024:</strong> Four papers accepted at <strong>NeurIPS-24</strong>! Congrats to Fanxu, Cai, Xiaojuan and Yanbo! 🎉</p>
          <p><strong>7/12/2024:</strong> Released <strong>GOFA</strong>, the Generative One For All model for tackling all tasks on all kinds of graphs.</p>
        </div>
    design:
      columns: '2'
      background:
        gradient: false
        color: light
      spacing:
        padding: ['40px', '0', '40px', '0']
  
  - block: slider
    content:
      title: 'Our Photos'
      subtitle: ''
      slides:
        - title: Barbecue 2024
          align: center
          background:
            image:
              filename: photo1.jpg
              filters:
                brightness: 0.8
            position: center
            color: '#1e40af'
        - title: Party 2025
          align: center
          background:
            image:
              filename: photo2.jpg
              filters:
                brightness: 0.8
            position: center
            color: '#1e40af'
    design:
      slide_height: '800px'
      is_fullscreen: false
      loop: true
      interval: 5000

  - block: markdown
    id: contact
    content:
      title: Contact Us
      subtitle: 'Join Our Research Community'
      text: |
        <div style="font-size: 0.95rem; line-height: 1.8;">
          <p style="font-size: 1rem; margin-bottom: 1.5rem;"><strong>Thank you so much for your interest in our work!</strong> We are actively looking for students and postdocs. MuLab welcomes applicants from diverse backgrounds.</p>
          
          <p><strong>🎓 Prospective PhD Students:</strong> We are always looking for strong PhD students with interests in Graph Machine Learning and Large Language Model Reasoning. I am looking for students who meet at least three criteria: creativity and passion for research, solid math skills, solid coding skills, and good English. <em>Note: Please do not email regarding PhD admission as decisions are made by committee.</em></p>
          
          <p><strong>🎯 PKU Undergraduate and Masters Students:</strong> We are happy to work with masters or undergraduate students at Peking University. We expect some prior experience in ML/AI and a minimum of 10 hours per week commitment. You are especially welcome if you have interdisciplinary backgrounds while being proficient in coding.</p>
          
          <p><strong>🌍 Visiting Students and Researchers:</strong> We take visitors on a rolling basis, and generally prefer visitors to stay for at least 6 months for high-quality collaborative work. Please email Prof. Zhang with your research interests and proposed duration.</p>
          
          <p><strong>📧 How to Apply:</strong> Email <strong>muhan@pku.edu.cn</strong> with subject line: [Application Type] - [Your Name] - [Your Institution]. Due to the large number of applicants, I may not be able to respond to every email. Thank you for understanding!</p>
          
          <p><strong>📍 Location:</strong> I am mainly affiliated with the Institute for AI (人工智能研究院) at the main campus (燕园) of PKU. Your office will be there - no need to go to Changping campus.</p>
        </div>
    design:
      columns: '1'
      background:
        gradient: false
        color: white
      spacing:
        padding: ['40px', '0', '40px', '0']

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
