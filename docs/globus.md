# Login to Globus & Browse Your Files

**Globus** is a robust file-sharing and transfer service. This guide explains how to use Globus to browse files you have stored in an RCC Midway 2 and 3 ecosystems. 

## Why Use Globus?

<p align='center'>
<img src='../img/globus/globus-diagram.png'
width='650'</p> 

You can transfer files from your local system to RCC clusters – or between RCC ecosystems – via SSH while connected through a login node. Still, you risk your file transfer being interrupted if your internet connection is unstable. ​A better way to transfer files is to connect to an RCC ecosystem through a data mover node.​ Data mover nodes connect to high-performance storage nodes and ​cost-effective data storage (CDS) nodes just like login nodes, but unlike login nodes, you can close a session anytime while your data transfer is happening in the background.​ Globus and Samba (SMB) are two ways to connect to a data mover node. Here, we cover Globus, which is much faster, more secure, and more stable. 

## Login to Globus


Go to [globus.rcc.uchicago.edu](). Select "University of Chicago" from the drop-down list of existing organizational logins and click "Continue.":

<p align='center'>
<img src='../img/globus/globus-login.png'
width='650'</p>

<center>*The University of Chicago Globus landing page. "University of Chicago" is selected from the drop-down menu.*</center>

Enter your CNetID and password when prompted:

<p align='center'>
<img src='../img/globus/cnet.png'
width='650'</p>

<center>*The University of Chicago CNetID sign-in page.*</center>


## Set Up Your Account

If you are accessing Globus with your University of Chicago login for the first time, you will need to set up your account. If your account is already set up, skip ahead to [Browse Your Files](##browse-your-files).

When you first log in, you will see an option to link your University of Chicago login to an existing Globus account. Click "Link to an existing account" if you have another Globus account. Otherwise, click "Continue":

<p align='center'>
<img src='../img/globus/link-account.png'
width='650'</p>

<center>*A message on the University of Chicago Globus landing page: This is the first time you are accessing Globus with your University of Chicago login. If you have previously used Globus with another login, you can link it to your University of Chicago login. When linked, both logins will be able to access the same Globus account permissions and history.*</center>

If you are accessing Globus with your University of Chicago login for the first time, you will need to agree to the Globus Terms of Service and Privacy Policy:

<p align='center'>
<img src='../img/globus/complete-sign-up.png'
width='650'</p>

<center>*A webpage that says "Complete Your Sign Up." The box indicating the user has agreed to the Terms of Service and Privacy Policy is checked..*</center>

If you are accessing Globus with your University of Chicago login for the first time, you will need to configure your Globus permissions:

<p align='center'>
<img src='../img/globus/globus-permissions.png'
width='650'</p>

<center>*A list of permissions the Globus Web App requests with options to allow or deny.*</center>


## Browse Your Files

Once you have signed in, click the "File Manager" tab in the toolbar on the left of your screen and type "University of Chicago Research Computing Center" into the collection search bar. The RCC manages three Globus collections (also called endpoints):

<p align='center'>
<img src='../img/globus/collection-search.png'
width='650'</p>

<center>*Globus web app opens to the File Manager tab. "University of Chicago Research Computing Center" is typed into the collection search bar.*</center>

:::{.callout-note title="RCC-Managed Globus Collections"}
**DaLI** is a collection within the RCC's Midway2 ecosystem. It provides additional storage for PI's who contributed to the DaLI grant. Selecting the DaLI collection, you land in Midway2's `/dali/` directory. 

**Midway** houses files from the RCC's Midway2 ecosystem. 

**Midway3** houses files from the RCC's Midway3 ecosystem. 

When you select the **Midway** or **Midway3** collection, you land in your Midway2 or Midway3 home directory, `/home/<cnet-id>`, denoted by a `/~/` path. Click "up one folder" to reach the top-level directory to access your scratch space and more.
:::

To see files in different collections at the same time, click the "two panes" icon next to "Panels" in the upper-right corner:

<p align='center'>
<img src='../img/globus/two-panes.png'
width='650'</p>

<center>*Globus File Manager in two-pane mode with Midway2 files in the left pane and Midway3 files in the right pane.*</center>

## Connecting Midway clusters to your personal computer using Globus

See Transfer Files with Globus for help moving files between collections. [This guide](https://www.globus.org/globus-connect-personal) also describes how to make your computer a Globus endpoint so you can move files between your local system and RCC cluster (Midway2 and Midway3). In addition, you might find Globus documentation helpful if you need to schedule transfer files [here](https://docs.globus.org/). 
