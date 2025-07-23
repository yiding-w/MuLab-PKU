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
            <p style="font-weight: bold; font-size: 1.5rem;">
              Welcome to Muhan's Research Lab!
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
      text: 05/2025 Μμ Lab has three papers accepted to ICML 2025.
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
        - title: Lab Group Photo 2024
          content: Our research team working together
          align: center
          background:
            image:
              filename: welcome.jpg
              filters:
                brightness: 0.7
            position: center
            color: '#666'
        - title: Research Activities
          content: Collaborative research environment
          align: center
          background:
            image:
              filename: contact.jpg
              filters:
                brightness: 0.7
            position: center
            color: '#666'
        - title: Team Collaboration
          content: Working on cutting-edge AI research
          align: center
          background:
            image:
              filename: image3.png
              filters:
                brightness: 0.7
            position: center
            color: '#666'
    design:
      slide_height: '400px'
      is_fullscreen: false
      loop: true
      interval: 5000

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
