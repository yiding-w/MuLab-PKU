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
      title: ""
      subtitle: ""
      text: |
        <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; align-items: start; max-width: 1200px; margin: 0 auto;">
          
          <!-- 左侧标题区域 -->
          <div style="position: sticky; top: 2rem;">
            <h2 style="font-size: 2.5rem; font-weight: bold; color: #1f2937; margin: 0; line-height: 1.2;">Contact Us</h2>
            <p style="font-size: 1.1rem; color: #6b7280; margin-top: 1rem; line-height: 1.6;">Join Our Research Community</p>
          </div>
          
          <!-- 右侧内容区域 -->
          <div style="font-size: 1rem; line-height: 1.7; color: #374151;">
            <p style="font-size: 1.1rem; color: #1f2937; margin-bottom: 2rem;"><strong>Thank you so much for your interest in our work!</strong></p>
            
            <p style="margin-bottom: 2rem;">We are actively looking for students and postdocs. MuLab welcomes applicants from diverse backgrounds. Students with backgrounds that are underrepresented or underserved in AI/ML are especially encouraged to apply.</p>
            
            <!-- Prospective PhD Students -->
            <div style="margin-bottom: 3rem;">
              <h3 style="color: #2563eb; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🎓</span>
                Prospective PhD Students
              </h3>
              <p style="margin-bottom: 1rem;">We are always looking for strong PhD students with interests in <strong>Graph Machine Learning</strong> and <strong>Large Language Model Reasoning</strong>. Please do not email me regarding PhD admission as admission decisions are made by a committee.</p>
              <p style="margin-bottom: 1rem;">If you are an admitted or current PhD student at PKU, please email Prof. Zhang directly. I am looking for students who meet at least three of the following criteria:</p>
              <ul style="margin: 1rem 0 1rem 1.5rem; padding: 0;">
                <li style="margin-bottom: 0.5rem;">Creativity and passion for research</li>
                <li style="margin-bottom: 0.5rem;">Solid math skills</li>
                <li style="margin-bottom: 0.5rem;">Solid coding skills</li>
                <li style="margin-bottom: 0.5rem;">Good English (writing and speaking)</li>
              </ul>
              <p><strong>Location:</strong> I am mainly affiliated with the <strong>Institute for AI (人工智能研究院)</strong> at the main campus (燕园) of PKU. Your office will be there - no need to go to Changping campus.</p>
            </div>
            
            <!-- Prospective Postdocs -->
            <div style="margin-bottom: 3rem;">
              <h3 style="color: #2563eb; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🔬</span>
                Prospective Postdocs
              </h3>
              <p>We are currently looking for 1-2 postdocs. Applicants are expected to have a strong publication record in top-tier graph ML, NLP, and/or machine learning conferences. Please email Prof. Zhang with your CV and research statement.</p>
            </div>
            
            <!-- PKU Students -->
            <div style="margin-bottom: 3rem;">
              <h3 style="color: #2563eb; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🎯</span>
                PKU Undergraduate and Masters Students
              </h3>
              <p style="margin-bottom: 1rem;">We are happy to work with masters or undergraduate students at Peking University. We expect applicants to have some prior experience in ML/AI (prior research experience is not required), and a minimum of 10 hours per week commitment to research.</p>
              <p>You are especially welcome if you have <strong>interdisciplinary backgrounds</strong> (such as maths/physics/chemistry/biology) while being proficient in coding. For PKU students, you can schedule one-on-one chats with me at my office.</p>
            </div>
            
            <!-- Visiting Students -->
            <div style="margin-bottom: 3rem;">
              <h3 style="color: #2563eb; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🌍</span>
                Visiting Students and Researchers
              </h3>
              <p>We take visitors on a rolling basis, and generally prefer visitors to stay for at least 6 months for high-quality collaborative work. If you are interested in visiting our research lab, please email Prof. Zhang with your research interests and proposed duration.</p>
            </div>
            
            <!-- Application Process -->
            <div style="background: #f8fafc; padding: 2rem; border-radius: 0.5rem; margin-bottom: 2rem; border-left: 4px solid #3b82f6;">
              <h4 style="color: #1f2937; margin-top: 0; margin-bottom: 1rem; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">📧</span>
                Application Process
              </h4>
              <p style="margin-bottom: 0.5rem;"><strong>Email:</strong> muhan@pku.edu.cn</p>
              <p style="margin-bottom: 1rem;"><strong>Subject Line:</strong> [Application Type] - [Your Name] - [Your Institution]</p>
              <p style="margin: 0; color: #6b7280; font-size: 0.9rem;"><strong>Note:</strong> Due to the large number of applicants, competition is intense every year and I may not be able to respond to every email. Thank you for understanding!</p>
            </div>
            
            <!-- What We Offer -->
            <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 0.5rem; border-left: 4px solid #0ea5e9;">
              <p style="margin: 0;"><strong>What we offer:</strong> Detailed guidance, abundant computation resources, research freedom for senior students, and a collaborative environment dedicated to <em>revealing the intelligence behind graphs and reasoning</em>.</p>
            </div>
          </div>
        </div>
        
        <!-- 响应式设计 -->
        <style>
        @media (max-width: 768px) {
          div[style*="grid-template-columns: 1fr 2fr"] {
            grid-template-columns: 1fr !important;
            gap: 1.5rem !important;
          }
          div[style*="position: sticky"] {
            position: static !important;
          }
        }
        </style>
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
