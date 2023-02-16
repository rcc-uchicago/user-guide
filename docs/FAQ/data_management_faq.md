# Data Management FAQ

??? question "How much storage space do I have?"
    Use the ```quota``` command to get a summary of your current file system usage and available storage space.

??? question "I'm over quota...what do I do?"
    You can meet user quota (1-4) or group quota (1-6) by following the steps listed below:

    1. Remove unused data to meet quota requirements. If the group quota is exceeded, consider removing former users' directories if they are large. You need to let us know the path to folders you don't have permission to remove and ask PI to respond to this thread with approval.
    
    2. If you are over the file number quota, you can compress many small files into zip or tar archives to reduce the total number of files.  
    
    3. Temporary solution: move files to /scratch with a higher quota limit. Note that /scratch is not backed up, and you should not use it for long-term storage.

    4. Move files to another storage. It could be a local machine or a cloud. See the data transfer section in the new user guide we are working on: https://rcc-uchicago.github.io/user-guide/midway23/midway_data_transfer/

    5. Ask PI to submit a research allocation request to get more storage (If standard research allocation is not enough - special research allocation can give temporary storage of a greater size) https://rcc.uchicago.edu/accounts-allocations/request-allocation

    6. Ask PI to purchase storage via the cluster partnership program: https://rcc.uchicago.edu/support-and-services/cluster-partnership-program  

??? question "Why can't I write files into my home directory?"
    An error writing files typically happens when a user is over-quota. Please ensure that you are under quota both in terms of size and number of files with the `quota` command.


??? question "How do I get my storage quota increased?"

    Additional storage space can be purchased through the [Cluster Partnership Program](https://rcc.uchicago.edu/support-and-services/cluster-partnership-program). You may also request additional storage as part of a [Research II Allocation or Special Allocation](https://rcc.uchicago.edu/accounts-allocations/request-allocation).

??? question "How do I share files with others?"
    The recommended way to share files with members of your group is to store them in the ```/project``` or ```/project2``` directory for your group. Project directories are created for all PI and project accounts. File and directory permissions can be customized to allow access to users within the group, as well as RCC users that do not belong to your group.

??? question "I accidentally deleted or lost a file. How do I restore it?"
    The best way to recover a recently deleted, corrupted or lost file is from a snapshot. See [Data Recovery and Backups](../midway23/midway_data_storage.md#data-recovery-and-backups) for more information.

??? question "How do I request a restore of my files from tape backup?"
    The RCC maintains tape backups of all home and project directories. These tape backups are intended for disaster recovery purposes only. There is no long-term history of files on tape. In most cases, you should use file system snapshots to retrieve recover files. See [Data Recovery and Backups](../midway23/midway_data_storage.md#data-recovery-and-backups) for more information.