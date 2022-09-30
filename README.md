# rcc-website
Testing for RCC User Guide 2.0

A) link to view new site: https://projects.rcc.uchicago.edu/rcc/rcc-user-guide/site/

B) content from current site: https://projects.rcc.uchicago.edu/rcc/midway2/site/   
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

Migrate all content from current site (see link B), source located at /project2/rcc/public_html/midway2, to user guide 2.0, link A, repository rcc-user-guide, located on midway2 at /project2/rcc/public_html/rcc-user-guide

Things to keep in mind:
- we are focusing just on the midway2/3 section of new user guide for now--other systems will come later
- objective is to optimize organization of pages/distribution of content
- priority is migration of content at this point, not extensive re-rewriting within pages
- content can be moved from one page to another, and page names/section titles can (and should) be changed
- broken tables/formatting should be fixed 
- please note 1) any content/sections that should be heavily revised 2) differences between midway2 and 3--if we have time, we will add tabs to differentiate between the two



## Content organization plan

nav:
  - Home: 'index.md'
  - "Account and Allocation Management":
    - account_allocation_management_overview.md
    - create_and_manage_accounts.md
    - request_and_manage_allocations.md
  - "Midway2 and Midway3":
    - Getting Started: midway3_getting_started.md
    - Hardware Overview: midway3_hardware_overview.md
    - Connecting to Midway: midway3_connecting.md
    - "Data Management":
      - Data Transfer: midway3_data_transfer.md
      - Data Storage: midway3_data_storage.md
    - "Running Jobs":
      - Overview: midway3_jobs_overview.md
      - Job Management: midway3_job_management.md
      - Interactive Jobs: midway3_interactive_jobs.md
      - Batch Jobs: midway3_batch_jobs.md
      - Example Job Submission Scripts: example_job_scripts.md
    - "Software":
      - Overview: midway3_software_overview.md
      - "Commonly Used Applications":
        - Python and Conda: midway3_python.md
        - Jupyter: midway3_jupyter.md
      - List of All Software: midway3_software_list.md
      - Request New Software: midway3_software_requests.md
    - Troubleshooting and FAQ: midway3_troubleshooting.md
  - "MidwayR":
      - midwayR_getting_started.md
  - "Other Systems":
    - "Beagle3":
      - beagle3_hardware.md
    - "DaLI":
      - dali_hardware.md
    - "MidwaySSD":
      - midwayssd_hardware.md
    - "Skyway":
      - skyway_hardware.md
  - "Facility Policies":
    - facility_policies.md
  - "Tutorials":
    - tutorial_01.md
  - "Help":
    - Frequently Asked Questions: general_faq.md
    - Contact Us: contact_us.md
