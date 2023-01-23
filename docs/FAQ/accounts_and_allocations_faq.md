# Accounts and Allocations FAQ

## Accounts and Access to Midway

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
    You can use your CNetID for authentication after you have left, but IT Services may expire it when you leave. If you have an RCC account, but you still can’t log in, it is likely that password authentication has been disabled by IT Services. Please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"} to request re-enabling access to your account.

??? question "How do I change/reset my password?"
    RCC cannot change or reset your password. Go to the CNet Password Recovery page to change or reset your password.

??? question "What groups am I a member of? "
    To list the groups you are a member of, type ```groups``` on any RCC system.

## Allocations and Service Units

??? question "What is an allocation? "
    An allocation is a specified number of computing and storage resources granted to a PI or an education account. An allocation is necessary to run jobs on RCC systems. See [RCC Allocations](https://rcc.uchicago.edu/accounts-allocations) for more details.

??? question "What is a service unit (SU)? "
    A service unit (SU) is roughly equal to 1 core-hour; for a more precise definition, see [RCC Service Units](https://rcc.uchicago.edu/accounts-allocations/user-guidelines).

??? question "How do I obtain an allocation? "
    The RCC accepts proposals for large (“Research II”) allocations bi-annually. Proposals for medium-sized allocations, special purpose allocations for time-critical research, and allocations for education and outreach may be submitted at any time. See [RCC Allocations](https://rcc.uchicago.edu/accounts-allocations/allocation-service-units) for more information.

??? question "How is compute cluster usage charged to my account? "
    The charge associated with a job on any RCC system is a function of (1) the number of cores allocated to the job, and (2) the elapsed wall-clock time (in hours).

??? question "How do I check the balance of my allocation? "
    The ```rcchelp``` tool is the easiest way to check your account balance. Run


    ``` 
    rcchelp balance  
    ```

??? question "How do I check how my allocation has been used? "
    The ```rcchelp``` tool has several options for summarizing allocation usage. For a summary, run


    ```
    rcchelp usage
    ```
    To see usage per job, run


    ```
    rcchelp usage --byjob
    ```
    If you are the PI, you may use --byuser option to see the individual usage of your group members

    ```
    rcchelp usage --byuser
    ```