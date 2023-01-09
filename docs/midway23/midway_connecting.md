# Connecting to Midway
The information here describes how users can connect to Midway to access RCC resources. All users are responsible for knowing and abiding by the [RCC User Policy](../user_policy.md). 

## Account Credentials
To connect to Midway, you must have a RCC user account ([request an account](https://rcc.uchicago.edu/accounts-allocations/request-account){:target="_blank"}).

Your RCC account uses your UChicago CNetID for the username and the corresponding CNetID password for the password:

```
Username: CNetID
Password: CNetID password
```

## Login Nodes

When we say "connect to Midway," what we're really saying is connect to one of Midway's **login nodes**. The login nodes are physical parts of the Midway cluster that are connected to the internet and serve as the "foyer" to the system. You connect to the login nodes to manage data, download and install packages, and submit jobs to the compute nodes, as the diagram below depicts.  

![Midway Node Diagram](img/connecting/midway_node_diagram.jpg)

Upon logging in to Midway, you will automatically be connected to one of several login nodes.

???+ warning
    The login nodes are *NOT* for computionally intensive work. For running computationally intensive programs, see [Running Jobs on Midway](/midway23/midway_jobs_overview).  

## Summary of Connection Methods
There are two main ways to connect to Midway, detailed below. This table provides a high level summary of the two:  

|  <div style="width:200px">Connection Method</div> | Description |
| ----------- | ----------- |
| [Secure Shell (SSH)](#connecting-with-ssh) | Command-line (Terminal or Powershell) access to the cluster. Good for users with command-line programming  experience, and is typically the most stable.  |
| [ThinLinc](#connecting-with-thinlinc) | Provides a graphical user interface (GUI), and thus is more "user friendly" and minimizes need for command-line interaction. Typically less stable than SSH. |



## Connecting with SSH
Secure Shell (SSH) is a protocol that provides secure command-line access to remote resources such as Midway.

Step 1: Open an SSH client
=== "Mac or Linux Computers"

     Open a Terminal or iTerm2 window.

=== "Windows Computers"
    
    Open a Powershell window.
    ???+ note
        Windows users running a version of Windows older than Windows 10’s April 2018 release will have to download an ssh client to connect via SSH. We recommend the MobaXterm, client, although other options are available.

Step 2: At the command line enter:
=== "Midway2"
    ```
    ssh <CNetID>@midway2.rcc.uchicago.edu
    ```
===+ "Midway3"
    ```
    ssh <CNetID>@midway3.rcc.uchicago.edu
    ```

Step 3: Provide your CNetID password when prompted. Duo two-factor autentication will request you select from the available 2FA options to authenticate to Midway.

```
Duo two-factor authentication for user

Enter a passcode or select one of the following options:

1) receive a push code on your Duo app,
2) Receive authentication through your phone number, and
3) get an SMS code.

Passcode or option (1-3):
```
??? note
    SSH key-based authentication is no longer supported. The SSH password-based authentication is currently the only supported method for authentication.

Step 4: Choose from the available two-factor authentication options and finish the authentication process.


### X11 Forwarding
X11 forwarding is a mechanism that allows you to forward a remote application's display to your local machine. To enable X11 forwarding when connecting to a Midway system with SSH, the -Y flag should be included:
=== "Midway2"
    ```
    ssh -Y <CNetID>@midway2.rcc.uchicago.edu
    ```
===+ "Midway3"
    ```
    ssh -Y <CNetID>@midway3.rcc.uchicago.edu
    ```

???+ note
    XQuartz is required to enable trusted X11 forwarding on a Mac.

## Connecting with ThinLinc
ThinLinc is a remote desktop server used to connect to Midway and obtain a remote graphical user interface (GUI). We recommend using ThinLinc to use software that requires a GUI.

### ThinLinc Web Browser   
Point your web browser to the following web address:
=== "Midway2"
    ```
    https://midway2.rcc.uchicago.edu.
    ```
    You will land on this page:
    ![Midway 2 ThinLinc Web](img/connecting/midway2_thinlinc_web.png){ width=500 }
===+ "Midway3"
    ```
    https://midway3.rcc.uchicago.edu.
    ```
    You will land on this page:
    ![Midway 3 ThinLinc Web](img/connecting/midway3_thinlinc_web.png){ width=500 }

Proceed to log in with your CNetID and password.

Duo two-factor autentication will request you select from the available 2FA options to authenticate to Midway.

```
Duo two-factor authentication for user

Enter a passcode or select one of the following options:

1) receive a push code on your Duo app,
2) Receive authentication through your phone number, and
3) get an SMS code.

Passcode or option (1-3):
```

### ThinLinc Desktop Client
Download and install the appropriate ThinLinc client here:
https://www.cendio.com/thinlinc/download

Open the ThinLinc client and use the following information to set up your connection to Midway:

=== "Midway2"
    ```
    Server: midway2.rcc.uchicago.edu
    Username: CNetID
    Password: CNetID password
    ```
    Your client should look similar to this:
    ![Midway 2 ThinLinc Client](img/connecting/midway2_thinlinc_client.png){ width=500 }

===+ "Midway3"
    ```
    Server: midway3.rcc.uchicago.edu
    Username: CNetID
    Password: CNetID password
    ```
    Your client should look similar to this:
    ![Midway 3 ThinLinc Client](img/connecting/midway3_thinlinc_client.png){ width=500 }
    

ThinLinc will default to open in a fullscreen window that fills `all monitors`. To change this use `Options` from the initial login interface. 

After clicking the `Connect` button, Duo two-factor autentication will request you select from the available 2FA options to authenticate to Midway.

```
Duo two-factor authentication for user

Enter a passcode or select one of the following options:

1) receive a push code on your Duo app,
2) Receive authentication through your phone number, and
3) get an SMS code.

Passcode or option (1-3):
```

### The ThinLinc Interface

Upon successfully logging in, you will be presented with an IceWM desktop. Select Applications tab in the top left corner to access the terminal, file browser, and other utilities.

![ThinLinc Desktop](img/connecting/thinlinc-desktop.png){ width=500 }

To copy/paste between Thinlinc webaccess client and your computer, open the side toolbar by clicking the purple handle. Click the Clipboard icon. The text field that just open will be synced with the clipboard on the server, so you can copy and paste to and from this text field.

With ThinLinc it is possible to maintain an active session after you have closed your connection to Midway. To disconnect from Midway but maintain an active session, simply close the ThinLinc window. **You must have "End existing session" unchecked for this to occur.**

To exit ThinLinc and terminate your session completely, simply exit or close the ThinLinc application.

<!-- Deprecated??

## Remote Visualization on Midway2

RCC provides a mechanism for accessing a GPU-equipped visualization node, which can be used for running 3D and graphics-intensive visualization software packages. 

First log into Midway via ThinLinc.

Once logged in, open a terminal and in the terminal window, issue the command `sviz`

![sviz terminal](img/connecting/sviz-terminal.png){ width=500 }

To exit the Visualization node, simply close the terminal window from which it was launched. You can then log out of Midway by selecting Logout from the Applications menu in ThinLinc, or by simply closing the ThinLinc window.
-->