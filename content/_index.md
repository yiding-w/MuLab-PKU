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
              We are dedicated to <strong>revealing the intelligence behind graphs and reasoning</strong>. Our research focuses on graph machine learning and large language model reasoning, pushing the boundaries of AI to understand complex structured data and human-like reasoning abilities.
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
        - title: Team Building 2024
          align: center
          background:
            image:
              filename: photo1.jpg
              filters:
                brightness: 0.8
            position: center
            color: '#1e40af'
        - title: Team Building 2025
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
      title: Prospective Students
      subtitle: 'Join Our Research Group'
      text: |
        <div style="font-size: 1rem; line-height: 1.7; color: #374151;">
          <p>I am looking for <strong>highly motivated PhD/undergraduate students</strong> who are interested in doing graph ML research with me. Please shoot me an email if you meet at least three of the following criteria:</p>
          
          <ul style="margin: 1.5rem 0; padding-left: 1.5rem;">
            <li><strong>Creativity and passion for research</strong></li>
            <li><strong>Solid math skills</strong></li> 
            <li><strong>Solid coding skills</strong></li>
            <li><strong>Good English</strong> (writing and speaking)</li>
          </ul>
          
          <p>I will do my best to provide support for your success, including <strong>detailed guidance</strong>, <strong>plenty of computation resources</strong>, and <strong>research freedom for senior PhDs</strong>.</p>
          
          <p>You are especially welcome if you have <strong>interdisciplinary backgrounds</strong> (such as maths/physics/chemistry/biology) while proficient in coding. For students in Peking University, you can schedule one-on-one chats with me at my office.</p>
          
          <div style="background: #fef3c7; padding: 1rem; border-radius: 0.5rem; margin: 1.5rem 0; border-left: 4px solid #f59e0b;">
            <p style="margin: 0;"><strong>📧 Note:</strong> Due to the large number of applicants, the competition is intense every year and I may not be able to respond to every email. Hope you understand!</p>
          </div>
          
          <p><strong>For potential PhD students:</strong> I am mainly affiliated with the <strong>Institute for AI (人工智能研究院)</strong>, which is based in the main campus (燕园) of PKU. Your office will also be there and you don't need to go to the Changping (昌平) campus.</p>
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
