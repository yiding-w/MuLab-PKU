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
            <h2 style="font-weight: bold; font-size: 1.8rem; color: #2563eb; margin-bottom: 1rem;">
              Welcome to Muhan 's Research Lab!
            </h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #4b5563;">
              We are dedicated to <strong>revealing the intelligence behind graphs and reasoning</strong>. Our research focuses on graph machine learning and large language model reasoning, pushing the boundaries of AI to understand complex structured data and human-like reasoning abilities.
            </p>
            <p style="font-size: 1rem; line-height: 1.5; color: #6b7280; margin-top: 1rem;">
              Led by Dr. Muhan Zhang, Assistant Professor at the Institute for Artificial Intelligence, Peking University, our lab develops cutting-edge algorithms and theories for learning over graphs and improving LLMs' reasoning capabilities.
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
      title: Our Lab
      subtitle: ''
      slides:
        - title: Graph Machine Learning
          content: Developing algorithms and theories for learning over graphs - from social networks to molecules and circuits
          align: center
          background:
            image:
              filename: welcome.jpg
              filters:
                brightness: 0.6
            position: center
            color: '#1e40af'
        - title: LLM Reasoning
          content: Understanding and improving large language models' reasoning abilities with human-like flexibility and reliability
          align: center
          background:
            image:
              filename: contact.jpg
              filters:
                brightness: 0.6
            position: center
            color: '#1e40af'
        - title: Research Excellence
          content: Leading research in AI with 10,000+ citations and recognition as top 2% scientist worldwide
          align: center
          background:
            image:
              filename: image3.png
              filters:
                brightness: 0.6
            position: center
            color: '#1e40af'
    design:
      slide_height: '400px'
      is_fullscreen: false
      loop: true
      interval: 5000


  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '1'
---
