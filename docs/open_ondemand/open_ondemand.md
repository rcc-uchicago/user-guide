# Welcome to Open OnDemand at RCC UChicago

## Introduction

Open OnDemand (OOD) is a web-based portal that provides seamless, user-friendly access to High-Performance Computing (HPC) resources at the Research Computing Center (RCC), University of Chicago. With OOD, you can manage files, submit and monitor jobs, and launch interactive applications such as Jupyter, RStudio, and graphical desktop sessions—all from your web browser, without needing to use the command line.

**Key Features of Open OnDemand:**
- **Web-based Access:** No need for SSH or VPN—access the cluster securely from anywhere using your browser.
- **File Management:** Upload, download, move, and edit files directly in your home or project directories.
- **Job Management:** Submit, monitor, and manage batch jobs using the Slurm scheduler with intuitive interfaces like Job Composer.
- **Interactive Apps:** Launch interactive sessions (e.g., Jupyter, RStudio, Linux Desktop) that run on compute nodes, with easy resource selection.
- **Terminal Access:** Open a shell session to the cluster directly in your browser.
- **Project Organization:** Organize your work with project management tools.

## Why Use Open OnDemand?

Open OnDemand is designed to lower the barrier to HPC usage for both new and experienced users. It provides:
- A consistent, graphical interface for common HPC tasks.
- The ability to work with files and jobs without learning Linux commands.
- Access to powerful interactive applications and remote desktops.
- A platform that supports both research and teaching needs.

## Getting Started

1. **Log in:** Visit [https://midway3-ondemand.rcc.uchicago.edu](https://midway3-ondemand.rcc.uchicago.edu) and log in with your CNetID and password.
2. **Dashboard:** After logging in, you'll see the OOD dashboard, which provides access to all features.
3. **Navigation:** Use the top menu to access Files, Jobs, Clusters (terminal), Interactive Apps, and Projects.

## Typical Workflow

- **Manage Files:** Use the Files app to upload data, organize directories, and edit scripts.
- **Submit Jobs:** Use Job Composer to create and submit batch jobs, or monitor running jobs via Active Jobs.
- **Launch Interactive Apps:** Start a Jupyter Notebook, RStudio Server, or a full Linux desktop session for interactive work.
- **Monitor and Manage:** Track your jobs and sessions, and clean up resources when finished.

## Additional Resources

- For a detailed walkthrough of each feature, see the sections below.
- For troubleshooting, best practices, and advanced usage, refer to the [official Open OnDemand documentation](https://openondemand.org/) and [RCC User Guide](https://rcc.uchicago.edu/support-and-services/user-guides/).

## Accessing Open OnDemand

To access the RCC Open OnDemand service:

1.  Open a web browser (Chrome, Firefox, Safari, or Edge are recommended).
2.  Navigate to: `https://midway3-ondemand.rcc.uchicago.edu`.

![login screen](images/login_ondemand_screen.jpeg)
<div class="caption">Figure: Login screen</div>
3.  You will be prompted to log in with your CNetID and password.

## The Open OnDemand Dashboard

After logging in, you will see the Open OnDemand dashboard. This is your main portal for accessing HPC resources.

![OOD Dashboard showing commonly used apps](images/dashboard_commonly_used_apps.png)
<div class="caption">Figure: OOD Dashboard showing commonly used apps</div>

Key components include:

* **Files**: Manage your files and directories in your home directory and other accessible storage locations on Midway. You can upload, download, copy, move, rename, and delete files and folders.

  ![OOD File Manager with Upload dialog](images/file_manager_upload.jpg)
  <div class="caption">Figure: OOD File Manager with Upload dialog</div>

* **Jobs**:
    * **Active Jobs**: View and manage your currently running and queued jobs on the Slurm scheduler.
    * **Job Composer**: Create and submit new batch jobs using predefined templates or by writing your own submission scripts.

      ![OOD Job Composer interface](images/job_composer_overview.png)
      <div class="caption">Figure: OOD Job Composer interface</div>

      ![OOD Job Composer showing job details and script contents](images/job_composer_job_details.png)
      <div class="caption">Figure: OOD Job Composer showing job details and script contents</div>

* **Clusters**: Access shell (terminal) access to the Midway3 cluster directly from your browser.
* **Interactive Apps**: Launch interactive graphical applications or server-based applications like Jupyter Notebooks, RStudio Server, and full Linux Desktop environments.

  ![OOD All Apps listing](images/all_apps_page.jpg)
  <div class="caption">Figure: OOD All Apps listing</div>

* **Projects**: Manage your research projects, potentially including data and job organization.

  ![OOD Project Manager interface](images/project_manager.png)
  <div class="caption">Figure: OOD Project Manager interface</div>

## Using Interactive Apps

One of the most powerful features of Open OnDemand is the ability to launch interactive applications that run on the compute nodes of the Midway3 cluster.

**General Steps to Launch an Interactive App:**

1.  From the OOD dashboard, click on "Interactive Apps" in the top menu.

    ![OOD Interactive Apps Dropdown Menu](images/interactive_apps_menu.png)
    <div class="caption">Figure: OOD Interactive Apps Dropdown Menu</div>

2.  A dropdown list of available applications will appear (e.g., "Midway3 Desktop," "Jupyter Server," "RStudio Server," "QGIS Desktop").
3.  Select the application you wish to use.
4.  You will be presented with a form to specify the resources for your session:
    * **Account**: Your Slurm account/allocation (if applicable).
    * **Partition**: The Slurm partition to run the job on. For this testing phase, a dedicated partition `ondemand` is available.
    * **Number of hours**: How long you need the session.
    * **Number of CPU cores**: The number of processor cores.
    * **Memory**: The amount of memory (RAM) required.
    * Other application-specific options may also be available.
5.  Once you have filled out the form, click "Launch."
6.  Your job will be submitted to the Slurm scheduler. You will see its status in the "My Interactive Sessions" section of the dashboard.
7.  When the job starts and resources are allocated (this may take some time depending on cluster load), a "Connect" button will appear. Click this button to open your interactive session in a new browser tab.
    * For VNC-based apps (like Desktops or QGIS), you may be provided with a VNC password.
8.  When you are finished with your session, explicitly **close the application and then delete your interactive session** from the "My Interactive Sessions" page to free up resources.

## Important Information

**Key Points:**

**Key Points for Testers:**

* **Dedicated Testing Environment**:
    * A dedicated Slurm partition named `ondemand` has been created specifically for this testing phase.
    * This partition utilizes a selection of `cascadelake` nodes from Midway3: `midway3-0[001-002,008-019,022-038]`.
    * When launching interactive apps, please select the `ondemand` partition where appropriate and available in the application's form.
* **VNC Support**: VNC-dependent packages have been installed on these designated `ondemand` nodes to support interactive graphical applications.
* **Focus Areas for Testing**:
    * Overall usability and intuitiveness of the Open OnDemand interface.
    * Functionality of file management (upload, download, navigation).
    * Job submission and monitoring through the "Jobs" menu.
    * Launching and using available "Interactive Apps."
    * Stability and performance of interactive sessions.
    * Clarity of instructions and error messages.

## Managing Your Sessions and Files

* **Interactive Sessions**: Always remember to explicitly **delete** your interactive sessions from the "My Interactive Sessions" page when you are finished. Simply closing the browser tab does not terminate the job on the cluster.
* **File Management**: Be mindful of your storage quotas. Data generated within Open OnDemand sessions is stored in your standard RCC home or project directories.

## Getting Help

For questions, issues, or assistance:

* Refer to the [RCC User Guide](https://rcc.uchicago.edu/support-and-services/user-guides/) (Link to the main RCC user guide).
* Contact RCC Support: `help@rcc.uchicago.edu`

We appreciate your help in making Open OnDemand a valuable resource for the RCC UChicago community!


