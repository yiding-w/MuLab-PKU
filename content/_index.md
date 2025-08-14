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
            Mμ Lab is dedicated to pursuing principled and transformative research in artificial intelligence and machine learning. While our current focus spans graph learning and large language models, our long-term mission is broader: to accelerate the development of artificial general intelligence (AGI) and deepen the scientific understanding of intelligence itself. We strive to combine theoretical rigor with practical impact, designing algorithms that are not only powerful but also explainable, efficient, and generalizable across diverse dimensions.
            </p>
          </div>
  
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['40px', '0', '40px', '0']
  
  - block: markdown
    content:
      title: Latest News
      subtitle: ''
      text: |
        <div style="font-size: 0.95rem; line-height: 1.8;">
          <p><strong>5/1/2025:</strong> Three papers accepted at <strong>ICML-25</strong>! Congrats to Fanxu, Yanbo and Zian! 🎉</p>
          <p><strong>1/23/2025:</strong> Three papers accepted at <strong>ICLR-25</strong>! Congrats to Lecheng, Haotong and Zian! 🎉</p>
          <p><strong>1/20/2025:</strong> Collaborated with RedNote and released <strong>RedStar</strong>, a long-chain-of-thought O1-like model for complex reasoning. <a href="#" style="color: #2563eb;">See the preprint</a>.</p>
          <p><strong>12/18/2024:</strong> Released <strong>LIFT</strong>, a new paradigm to address long context problems of LLMs by fine-tuning long input into model parameters. <a href="#" style="color: #2563eb;">See the preprint</a>.</p>
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
