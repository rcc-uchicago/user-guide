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