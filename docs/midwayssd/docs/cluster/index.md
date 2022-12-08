## MidwaySSD Cluster Overview

This section of the documentation provides an overview of how the MidwaySSD cluster is organized.

## Partitions

The MidwaySSD cluster consists of 21 Intel Caslake based nodes. The nodes are accessible thourgh the partition `ssd`. This partition includes all 21 nodes and is accessible to PI groups affiliated with the Division of Social Sciences (SSD). Three login nodes are designated for interactive sessions. The remaining 18 nodes are compute nodes.


## Slurm Quality of Service (QOS)

The fair-share use of the MidwaySSD resources is managed through the Slurm scheduler Quality of Service (QOS) settings. The quality of service defines the type of resources that a job can request and whether the job is a production or debug run. The resource settings for each QOS are defined as follows:


<h3>QOS Name: MidwaySSD</h3>  (default if no QOS specified)
<table>
  <tr style="font-weight:bold">
   <td colspan="2"> </td> <td colspan="4" style="text-align:center">Per User Settings</td> 
  </tr>
  <tr>
    <td style="text-align:center">Max Wall Time</td>
    <td style="text-align:center"> QOS Priority </td>
    <td style="text-align:center"> Max Running Jobs </td>
    <td style="text-align:center"> Max Jobs Submit </td>
    <td style="text-align:center"> Max CPUs  </td>
    
  </tr>
  <tr>
    <td style="text-align:center"> 1-36:00:00 </td>
    <td style="text-align:center"> 10000 </td>
    <td style="text-align:center"> 28  </td>
    <td style="text-align:center"> 28 </td>
    <td style="text-align:center"> 320 </td>

  </tr>
</table>