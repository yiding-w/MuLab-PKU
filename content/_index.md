---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: feature
    content:
      title:
      subtitle:
      features:
        - icon:
          icon_pack: ""
          title: "**Welcome to Muhan's Research Lab!**"
          description: ""
          image:
            filename: logo.png
            alt_text: Lab logo
          image_position: left
    design:
      columns: "2"
      spacing:
        padding: ["40px", "0", "40px", "0"]
  
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
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

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
