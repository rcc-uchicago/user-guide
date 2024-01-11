# Transfer Files with Globus

**Globus** is a robust file-sharing and transfer service. Globus calls a collection of files an endpoint. The RCC has several Globus endpoints. This guide explains how to make your computer a Globus endpoint and transfer files between Globus endpoints. Put another way, this guide explains how to move files between your local system (i.e., your computer, lab computers, etc.) and the RCC's Midway 2 and 3 ecosystems. 

Note that this guide focuses on transferring files through the [Globus Web App]('globus.rcc.uchicago.edu'). Advanced users can access additional functionality by using the [Globus command line interface (CLI)]('https://docs.globus.org/cli/'), a standalone app that you can install on your computer and then use to access Globus.

## Make Your Computer a Globus Endpoint

Follow the instructions in the [Globus documentation]('https://docs.globus.org/globus-connect-personal/install/') to install Globus Connect Personal and make your computer a Globus endpoint (also called a collection). When Globus Connect Personal asks you to authenticate (Step 4), log in with your UChicago CNetID. 

Once your computer is a Globus endpoint, you will be able to access files stored on your local system, as well as files stored in the RCC's ecosystems, from [globus.rcc.uchicago.edu]('globus.rcc.uchicago.edu'). To access your locally stored files, click the "File Manager" tab in the toolbar on the left of your screen and type the name you gave your personal endpoint into the collection search bar: 

<p align='center'>
<img src='../figs/personal-endpoint.png'
width='650'
alt='Globus web app open to the File Manager tab. "Your Personal Endpoint Name" is typed into the collection search bar.'/>
</p>

## Manually Transfer Files

To see files in different collections at the same time, click the "two panes" icon next to "Panels" in the upper-right corner:

<p align='center'>
<img src='../figs/two-panes.png'
width='650'
alt='Globus web app File Manager open in two-pane mode.'/>
</p>

To transfer files between collections, open the source directory (where the files are currently) in one pane of the File Manager and the destination directory (where you want to move the files) in the other. Select the files you want to transfer from the source directory and drag and drop them into the destination directory or click the blue "Start" button above the source directory:

<p align='center'>
<img src='../figs/manual-transfer.png'
width='650'
alt='Globus web app File Manager open in two-pane mode with the "Start" button highlighted.'/>
</p>

You can customize your transfer with the "Transfer & Timer Options" drop-down menu at the center top of your screen. You can also use this menu to schedule transfers (see below). Advanced users can access additional file transfer functionality by using the [Globus command line interface (CLI)]('https://docs.globus.org/cli/').

## Schedule a File Transfer

To schedule a one-time or recurring file transfer, open the File Manager with your source directory in one pane and your destination directory in the other, as you would for a manual file transfer (see above). Select the files you want to transfer in the source directory, then click "Transfer & Timer Options" at the center top of your screen:

<p align='center'>
<img src='../figs/auto-transfer.png'
width='650'
alt='Globus web app File Manager open in two-pane mode with the "Transfer & Timer Options" highlighted.'/>
</p>

Specify the date and time you would like your transfer to occur with the "Schedule Start" option at the bottom of the menu. If you are scheduling a recurring transfer, this will be the date and time of the first occurrence. Use MM/DD/YYYY for the date and 12-hour time. For example, 12/15/2023, 1:30 PM:

<p align='center'>
<img src='../figs/schedule-start.png'
width='650'
alt='"Schedule Start" option set to 12/15/2023 1:30 PM.'/>
</p>

Use the "Repeat" option at the bottom of the menu to schedule a recurring file transfer. Specify how frequently you would like the transfer to occur and, optionally when you would like the transfer to stop. For example, you could schedule a transfer to happen every other day for a year:

<p align='center'>
<img src='../figs/recurring-transfer.png'
width='650'
alt='A recurring file transfer. "Repeat" is set today, "every" is set to 2 days, and the end is set to by date 12/15/2024, 01:30 PM.'/>
</p>
