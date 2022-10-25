# Connecting to RCC Resources
The information here describes how users can access RCC resources. All users of RCC resources are responsible for knowing and abiding by the RCC User Policy. 

Upon logging in to Midway, you will be connected to either one of two login nodes on the respective system:
```
Midway 2: midway2-login1.rcc.uchicago.edu or midway2-login2.rcc.uchicago.edu
Midway 3: midway3-login1.rcc.uchicago.edu or midway3-login2.rcc.uchicago.edu
```

**NOTE**: The login nodes are *NOT* for computionally intensive work. For running computationally intensive programs, see Running jobs on midway (link).

## Account Credentials
To use resources provided by the Research Computing Center you must have a RCC user account. If you do not already have a RCC acount, see the Getting Started page (link) for more information on obtaining a RCC account.

Your RCC account uses your UChicago CNetID for the username and the corresponding CNetID password for the password:

**NOTE**: If you require password assistance, please see the CNet Password Recovery webpage or contact UChicago IT Services (link).

## Connecting with SSH
Secure Shell (SSH) is a protocol that provides secure command-line access to remote resources such as Midway. By using SSH, you can remotely log in to your Midway account and interact with the Midway high-performance compute clusters.

**NOTE**: SSH key-based authentication is no longer supported. The SSH password-based authentication is currently the only supported method for authentication.

### Mac/Linux User SSH Access
To log in to Midway2 from a Linux or Mac computer, open a terminal and at the command line enter:
=== "Midway2"
    ```
    ssh <CNetID>@midway2.rcc.uchicago.edu
    ```
=== "Midway3"
    ```
    ssh <CNetID>@midway3.rcc.uchicago.edu
    ```

Provide your CNetID password when prompted. Duo two-factor autentication will request you select from the available 2FA options to authenticate to midway2.

Choose from the available two-factor authentication options and finish the authentication process.

#### X11 Forwarding
To enable X11 forwarding when connecting to a Midway system with ssh, the -Y flag should be included:
=== "Midway2"
    ```
    ssh -Y <CNetID>@midway2.rcc.uchicago.edu
    ```
=== "Midway3"
    ```
    ssh -Y <CNetID>@midway3.rcc.uchicago.edu
    ```
**NOTE**: XQuartz is required to enable trusted X11 forwarding on a Mac.

### Windows User SSH Access
<!-- we should stop recommending MobaXterm officially since we can't help troubleshoot using it -->
Windows users running Windows 10’s April 2018 release will have ssh enabled from the Powershell by default. 

All other Windows users will first need to download an ssh client to interact with the remote Unix command line. We recommend the MobaXterm, client, although other options are available. Once the MobaXterm client is installed on your local machine, open the MobaXterm client and click on the Sessions icon at the upper left hand corner of the client. Then perform the following numbered steps, illustrated in the figure below, to establish a connection to Midway2.

Click the SSH tab to expand the SSH login options.

In the Remote host field input:

midway2.rcc.uchicago.edu (to connect to midway2 cluster)

Select the Specify username button and input your CNetID

Proceed to log in by clicking the OK button.

image

Provide your CNetID password when prompted for a password. A Duo two-factor autentication window will then pop up requesting you select from the available 2FA options to authenticate to midway2.

image

Choose from the available two-factor authentication options and finish the authentication process.

## Connecting with ThinLinc
ThinLinc is a remote desktop server used to connect to Midway and obtain a remote graphical user interface (GUI). RCC recommands using ThinLinc to use software that requires a GUI.

To use ThinLinc to connect to Midway, one can either use the web browser version or download and install the ThinLinc Desktop Client. The web browser version does not require any setup, but the performance will be less optimal than the Desktop Client version.

### Using ThinLinc through a web browser
Point your web browser to the following web address:
=== "Midway2"
    ```
    https://midway2.rcc.uchicago.edu.
    ```
=== "Midway3"
    ```
    https://midway3.rcc.uchicago.edu.
    ```

Then proceed to log in with your CNetID and password

When prompted, select the two-factor authentication option and complete the login process.

### Using the ThinLinc Desktop Client
Download and install the appropriate ThinLinc client here:
https://www.cendio.com/thinlinc/download

Open the ThinLinc client and use the following information to set up your connection to Midway:

=== "Midway2"
    ```
    Server: midway2.rcc.uchicago.edu
    Username: CNetID
    Password: CNet password
    ```
=== "Midway3"
    ```
    Server: midway3.rcc.uchicago.edu
    Username: CNetID
    Password: CNet password
    ```

Your client should look similar to this:

image

The default setting for ThinLinc is for the client to open in a fullscreen window that fills “all monitors.” If you would prefer to work with ThinLinc from its own window, click Options from the initial login interface and then Screen to adjust your settings as desired. The following is an example of a setup that places the ThinLinc client in its own window:

image

Optional: You are also able to export local resources via ThinLinc. To do so, click Options from the initial login interface and then Local Devices. To adjust your settings for exporting the local file system, click Details next to Drives.

image

After clicking the ‘Connect’ button a Duo two-factor autentication window will pop up requesting you select from the available 2FA options to authenticate to midway2. Choose from the available options and finish the authentication process.

image

Upon successfully logging in, you will be presented with an IceWM desktop. Select Applications tab in the top left corner to access the terminal, file browser, and other utilities.

image

To copy/paste between Thinlinc webaccess client and your computer, first, you need to open the side toolbar by clicking the handle. After that you click the Clipboard icon. The text field that just open will be synced with the clipboard on the server, so you can copy and paste to and from this text field.

With ThinLinc it is possible to maintain an active session after you have closed your connection to Midway. To disconned from Midway but maintain an active session (e.g. when you log back into the ThinLinc client you will resume your remote session from where you left off), simply close the ThinLinc window. NOTE: You must have End existing session unchecked for this to occur.

To exit ThinLinc and terminate your session completely, simply exit or close the ThinLinc application.

## Remote Visualization on Midway 2
<!-- is this available on Midway 3 as well? -->
RCC provides a mechanism for accessing a GPU-equipped visualization node, which can be used for running 3D and graphics-intensive visualization software packages. This GPU-equipped visualization node can be interactively accessed by issuing the sviz alias command from within a terminal.

Log into Midway2 via ThinLinc. See Connecting with ThinLinc for more information.

Once logged in, open a terminal from the Applications tab at the upper left-hand side of the ThinLinc Desktop, or by right-clicking on the Desktop and selecting ‘Open Terminal’.

image

In the terminal window, issue the command sviz

image

After a few seconds, you will be connected to one of Midway 2’s visualization nodes. If several minutes pass and you are still not connected to the visualization node, issue ‘Ctrl+C’ from the terminal and check the status of the viz partition. You can do so by issuing sinfo -p viz from the terminal. If the status of the node is listed as ‘Alloc’, the node is currently in full use and not available. If the node status is instead ‘Mixed’ then check to see how many other jobs are currently using the viz partition by issuing squeue -p viz.

image

To exit the Visualization node, simply close the terminal window from which it was launched. You can then log out of Midway by selecting Logout from the Applications menu in ThinLinc, or by simply closing the ThinLinc window.

## Other Considerations
If you want to keep a terminal open in between connections, or if you want to have multiple terminals in a single SSH connection, you can use tmux (a terminal multiplexer).

To open a new session, you can run tmux. Once you are in a session, all shortcuts begin with pressing and releasing Ctrl+b. To open a new tab, press Ctrl+b and then c. To switch to another tab press Ctrl+b and then the number of the tab. To close a tab, either exit the shell prompt or press Ctrl+b and then x. To detach from a running session, press Ctrl+b and then d. To connect to an already running session, you can run tmux attach.

You can find more information about using tmux on the tmux wiki.