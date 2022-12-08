# Running Jobs Interactively on MidwaySSD

This section of the documentation describes how to use the MidwaySSD cluster to run an interactive session with either ThinLinc or an ssh connection. Remember that you must connect to MidwaySSD first and can refer to the previous section in this User Guide for more information. <br><br>

An interactive session is run directly on one of the login nodes. This can be helpful when you are debugging code, unit testing to determine your resource allocation needs and completing tasks such as module installation or web scraping that require internet connectivity. The alternative to an interactive session is submission of a batch job to one or more of the compute nodes. This is done using a short batch script and will be explained in the next section of the User Guide. 

## An Interactive Session in ThinLinc

You open an interactive session as soon as you have logged into MidwaySSD via ThinLinc. You can click on the software that you require and run directly on that login node. If you close the ThinLinc tab or your browser window, your interactive session on MidwaySSD will continue to run while you use your local machine. You can access your results, or return to your session by logging in again with your CNetID. Computations run on the login node are not counted in terms of your service hour usage. It should be noted that there are only three login nodes. Jobs that computationally intensive or long running should be completed on a compute node and may be killed by the system monitor. You must remember to disconnect from ThinLinc and end your interactive session when your computation is complete. Failing to do so can result in future login failures. <br><br>

### Example: Launching Stata Interactively in ThinLinc

Once you have logged into MidwaySSD and are connected via ThinLinc, you can select the Stata icon from the desktop. Your screen should look like the image below. You are ready to begin your interactive session in Stata. When you finish your calculations, please exit as you usually would, by selecting exit under the file menu and then closing the window. You will still need to disconnect from the ThinLinc session.<br><br>
![Screenshot showing Stata launch in ThinLinc](images/tl_statalaunch.jpg)
<br><br>