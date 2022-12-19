??? question "How do I become an RCC user? "
    RCC user account requests should be submitted via our online application forms. See [RCC Account Request](https://rcc.uchicago.edu/accounts-allocations/request-account) for more information.

??? question "How do I access RCC systems? "
    There are various ways to access RCC systems.

    To access RCC systems interactively, use ThinLinc or an SSH client. See [Connecting to RCC Resources](../../midway23/midway_connecting) for details.

    To access files stored on RCC systems, use scp, Globus Online or SAMBA. See [Data Transfer](../../midway23/midway_data_transfer/) for details.

??? question "How do I request access to a PI’s account if I already have an account on Midway? "
    Please submit a [User Account Request](https://rcc.uchicago.edu/accounts-allocations/general-user-account-request) and provide your CNetID and the PI Account name (typically pi- followed by the CNetID of the PI). The PI will receive an automated email requesting authorization for this request.

??? question "What is my RCC username and password? "
    RCC uses the University of Chicago CNetIDs for user credentials. Once your RCC account is created, your RCC username and password will be the same as your CNetID credentials.

??? question "Can an external collaborator get a CNetID so they can log in to RCC? "
    RCC can create CNetIDs for external collaborators. See [RCC Account Request](https://rcc.uchicago.edu/accounts-allocations/request-account) for more information.

??? question "What should I do if I left the university and my CNetID password no longer works?"
    You can use your CNetID for authentication after you have left, but IT Services may expire it when you leave. If you have an RCC account, but you still can’t log in, it is likely that password authentication has been disabled by IT Services. Please contact help@rcc.uchicago.edu to request re-enabling access to your account.

??? question "How do I change/reset my password?"
    RCC cannot change or reset your password. Go to the CNet Password Recovery page to change or reset your password.

??? question "What groups am I a member of? "
    To list the groups you are a member of, type ```groups``` on any RCC system.

??? question "How do I access the data visualization lab in the Zar room of Crerar Library? "
    The Zar room and its visualization equipment can be reserved for events, classes, or visualization work by contacting RCC at help@rcc.uchicago.edu. More information regarding RCC’s visualization facilities can be found on RCC's [Data Visualization](https://rcc.uchicago.edu/resources/visualization) page.

??? question "What login shells are supported and how do I change my default shell? "
    RCC supports the following shells:
    ```
    /bin/bash
    /bin/tcsh
    /bin/zsh
    ```
    Use this command to change your default shell:
    ``` 
    chsh -s /path/to/shell 
    ```

    It may take up to 30 minutes for that change to take effect.

??? question "Is remote access with Mosh supported? "
    Yes. To use Mosh, first log in to Midway via SSH, and add the command module load mosh to your ```~/.bashrc``` (or ```~/.zshenv``` if you use zsh). Then, you can log in by entering the following command in a terminal window:

    === "Midway2"
        ``` 
        mosh <CNetID>@midway2.rcc.uchicago.edu 
        ```
    === "Midway3"
        ```
        mosh <CNetID>@midway3.rcc.uchicago.edu
        ```
??? question "Is SSH key authentication allowed on RCC machines? "
    No, SSH key authentication is not allowed.

??? question "Why am I getting “ssh_exchange_identification: read: Connection reset by peer” when I try to log in via SSH? "
    You can get this error if you incorrectly enter your password too many times. This is a security measure that is in place to limit the ability for malicious users to use brute force SSH attacks against our systems.

    After 3 failed password entry attempts, an IP address will be blocked for 4 hours.

    While you wait for the block to be lifted, you should still be able to access the RCC system using ThinLinc.

??? question "Why am I getting prompted for YubiKey when I try to log in via SSH? "
    There are few reasons to get that error message. Please enroll in two factor authentication if you have not done already by visiting https://2fa.rcc.uchicago.edu. Please make sure you run:
    === "Midway2"
        ``` 
        ssh -Y CNetID@midway2.rcc.uchicago.edu 
        ```
    === "Midway3"
        ```
        ssh -Y CNetID@midway3.rcc.uchicago.edu
        ```
    Finally, please make sure your RCC account has not been expired.

??? question "How do I cite RCC in my publications and talks? "
    Citations and acknowledgements help RCC demonstrate the importance of computational resources and support staff in research at the University of Chicago. We ask that an acknolwedgment be given to the RCC in any presentation or publication of results that were made possible by RCC resources. Please reference the RCC as “The University of Chicago Research Computing Center” in citations and acknowledgements. Here are a few examples of suggested text:

    *"This work was completed in part with resources provided by the University of Chicago Research Computing Center."*

    *"We are grateful for the support of the University of Chicago Research Computing Center for assistance with the calculations carried out in this work."*

    *"We acknowledge the University of Chicago Research Computing Center for support of this work."*

    If you cite or acknowledge the RCC in your work, please notify the RCC by sending an email to info@rcc.uchicago.edu.