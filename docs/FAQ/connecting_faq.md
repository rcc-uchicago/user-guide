# Connecting to Midway FAQ

??? question "Why is ThinLinc spontaneously disconnecting?"
    Occasional ThinLinc instability is a known issue. First, wait 30 minutes to an hour and try again. If you are still having connection issues, try removing the following lines (or any similar) from the file `~/.bashrc` in your home directory (Unnecessary Anaconda configurations have been known to cause ThinLinc trouble):
    ```
        __conda_setup="$('/software/python-anaconda-2020.02-el7-x86_64/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/software/python-anaconda-2020.02-el7-x86_64/etc/profile.d/conda.sh" ]; then
            . "/software/python-anaconda-2020.02-el7-x86_64/etc/profile.d/conda.sh"
        else
            export PATH="/software/python-anaconda-2020.02-el7-x86_64/bin:$PATH"
        fi
    fi
    unset __conda_setup
    ```

    If the problem still persists, please contact the RCC help desk.


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
    In compliance with University security guidelines, 2FA is required with limited exceptions. If you believe you have a justifiable need for SSH key pairs, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"} and describe your situation. Once your justification is received, it will be reviewed by the RCC security team and we will follow up with you as soon as possible.   

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
    Finally, please make sure your RCC account has not expired.