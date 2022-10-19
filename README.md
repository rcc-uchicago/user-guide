# rcc-website
Testing for RCC User Guide 2.0

content from current site: https://projects.rcc.uchicago.edu/rcc/midway2/site/   

**Instructions for building site locally:**

1. Install mkdocs material.
```
pip install mkdocs-material 
```
2. clone git repo to local machine and go to folder 
``` 
cd <repo_folder>
```
3. build site
```
mkdocs serve
```

## Current Objective

Migrate all content from current site, source located at /project2/rcc/public_html/midway2, to user guide 2.0: repository `user-guide`, located at https://github.com/rcc-uchicago/user-guide

Things to keep in mind:
- We are focusing just on the midway2/3 section of new user guide for now--other systems will come later
- The objective is to optimize organization of pages/distribution of content
- Priority is migration of content at this point, not extensive re-rewriting within pages
- Content can be moved from one page to another, and page names/section titles can (and should) be changed
- Broken tables/formatting should be fixed 
- Please make note of 1) any content/sections that should be heavily revised 2) differences between midway2 and 3--if we have time, we will add tabs to differentiate between the two



## Content organization plan

nav:
  - Home: 'index.md'
  - "Account and Allocation Management":
    - Overview: account_allocation_management_overview.md
    - Account Management: create_and_manage_accounts.md
    - Allocation Management: request_and_manage_allocations.md
  - "Midway2 and Midway3":
    - Getting Started: midway3_getting_started.md
    - Hardware Overview: midway3_hardware_overview.md
    - Connecting to Midway: midway3_connecting.md
    - "Data Management":
      - Data Transfer: midway23/midway3_data_transfer.md
      - Data Storage: midway23/midway3_data_storage.md
      - File System Permissions: midway23/midway3_file_permissions.md
    - "Running Jobs":
      - Overview: midway23/midway3_jobs_overview.md
      - Job Management: midway23/midway3_job_management.md
      - Interactive Jobs: midway23/midway3_interactive_jobs.md
      - Batch Jobs: midway23/midway3_batch_jobs.md
      - Example Job Submission Scripts: midway23/example_job_scripts.md
    - "Software":
      - Overview: midway3_software_overview.md
      - "Commonly Used Applications":
        - Python and Conda: midway3_python.md
        - Jupyter: midway3_jupyter.md
        - Tensorflow and PyTorch: midway3_tf_pytorch.md
      - List of All Software: midway3_software_list.md
      - Request New Software: midway3_software_requests.md
    - Troubleshooting and FAQ: midway3_troubleshooting.md
  - "MidwayR":
      - Overview: midwayr/midwayR_overview.md
  - "Other Systems":
    - "Beagle3":
      - Overview: other_systems/beagle3_overview.md
    - "DaLI":
      - Overview: other_systems/dali_overview.md
    - "MidwaySSD":
      - Overview: other_systems/midwayssd_overview.md
    - "Skyway":
      - Overview: other_systems/skyway_overview.md
   - "GIS":
      - Overview:  
  - "Facility Policies":
    - facility_policies.md
  - "Tutorials":
    - tutorial_01.md
  - "Help":
    - Frequently Asked Questions: general_faq.md
    - Contact Us: contact_us.md
