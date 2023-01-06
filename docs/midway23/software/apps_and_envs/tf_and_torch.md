# Tensorflow and PyTorch

To use Tensorflow or PyTorch on Midway's GPU nodes, you may use an existing installation of either package provided as an Anaconda environment (see Python and Jupyter Notebook page), or install them into your own personal environment. 

Importantly, you must use an existing installation of CUDA and/or CuDNN, which you will first load via `module load cuda` or `module load cudnn` (which automatically loads cuda).

With the CUDA module/s loaded, and being connected to a GPU node, you should be able to import either Tensorflow and PyTorch and check GPU engagment with the following steps: 

## GPU Enagement
Here are a few quick tips on how to make sure you're actually using a GPU.

### Checking in terminal

 Before you even run your script, it can be useful to check to ensure 

 NVIDIA has a built in System Management Interface that makes this simple with one command:
```
 nvidia-smi
```

You should see details about the device, if it is detected.


### Tensorflow
Here's how to check if tensorflow sees your GPU/s.
```
import tensorflow as tf
```
The one-liner:
```
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```
For more info:
```
gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.get_device_details(gpus[0])
```

### PyTorch
And here's how to check with PyTorch
```
import torch
torch.cuda.device_count()
torch.cuda.get_device_name()
```