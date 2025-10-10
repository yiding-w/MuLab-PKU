---
title: ""

# Use custom layout for grouping by year
type: "widget_page"

# Optional banner image (relative to `assets/media/` folder).
banner:
  caption: ''
  image: ''

# Page sections
sections:
  - block: collection
    content:
      title: "2025"
      subtitle: ""
      text: ""
      filters:
        folders:
          - publication
        date:
          - start: "2025-01-01"
            end: "2025-12-31"
        # Disable all filtering options
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      view: citation
      sort_by: 'Date'
      sort_ascending: false
      # Disable search and filtering UI
      count: false
      search: false
      show_search: false
      filter_button: []
    design:
      columns: '1'
      view: 3
      
  - block: collection
    content:
      title: "2024"
      subtitle: ""
      text: ""
      filters:
        folders:
          - publication
        date:
          - start: "2024-01-01"
            end: "2024-12-31"
        # Disable all filtering options
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      view: citation
      sort_by: 'Date'
      sort_ascending: false
      # Disable search and filtering UI
      count: false
      search: false
      show_search: false
      filter_button: []
    design:
      columns: '1'
      view: 3
---
