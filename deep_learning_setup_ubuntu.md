# Deep learning on Ubuntu using NVIDIA GPUs

If you have nothing else to do on a weekend and you are a glutton for punishment, consider installing Linux, GPU drivers, and all the associated libraries to set your PC up for deep learning. These are just some high level notes I made while suffering through this experience. They assume a clean installation of Ubuntu (16.04.3 LTS).

There are three broad tasks you need to do to prepare your machine for deep learning. These are

1. Install a driver for your GPU
    - One way to do this is by executing `sudo apt-get install nvidia-375`
    - This will install version 375 of the driver (make sure this driver is compatible with the GPU in your system!)
    - In my case, I was working with a GeForce GTX 1080 8gb

2. Install CUDA and cuDNN libraries
    + CUDA is an API developed by Nvidia to implement parallel processing on CUDA-enabled GPUs. cuDNN is a library that uses CUDA for deep learning.
    + Make sure the version of CUDA and cuDNN that you download is compatible with the deep learning framework you are using! I use TensorFlow. At the time I installed these libraries, the most recent versions compatible with TensorFlow is CUDA 8.0 (any of the version of cuDNN compatible with CUDA 8.0 should work). More recent versions of CUDA might also work but they require building TensorFlow from source
    + There are many good resources on the internet for instructions on how to install these libraries. I include some below.
    + Note also that installing cuDNN requires a developer account with NVIDIA, which is easy enough to sign up for.

3. Install Anaconda
    - Anaconda is a Python distribution that streamlines package management for Python. It is especially useful for making it easy to create virtual environments in which you can conduct all your deep learning experiments without the danger of conflicting package dependencies. Anaconda is not the only way to manage virtual environments (there's virtualenv and a thing called Docker), but it is the easiest
    - If you have version 2 of python installed on your system (check using `python --version` command), you can download it by executing this command: `wget http://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh`
    - You then need to give the shell script access permission: `chmod +x Anaconda2-4.3.1-Linux-x86_64.sh`
    - Run it and follow instructions: `./Anaconda2-4.3.1-Linux-x86_64.sh`

4. Install the GPU version of TensorFlow
    - Execute `pip install tensorflow-gpu`
    - To check if the installation was successful, open the python interpreter and try to import TensorFlow: `import tensorflow as tf`
    - To check that TensorFlow detects your GPU:

    ```
    from tensorflow.python.client import device_lib
    print(device_lib.list_local_devices)
    ```
    - You should see a list containing information on your CPU and available GPU

### Set up summary (commands used to check)
1. Operating system: Ubuntu 16.04.3 LTS (`lsb_release -a`)
2. GPU: Gigabyte GeForce 1080 8gb (`nvidia-smi`)
3. Driver version: 384.111 (`nvidia-smi`)
4. CUDA version: release 8.0, V8.0.61 (`nvcc -V`)
5. cuDNN version: 6 (`cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2`)
6. TensorFlow version: tensorflow-gpu 1.4.1 (`pip list | grep tensorflow`)

### Notes
- If you are having trouble with finding the correct kernel source path when installing CUDA using the run file, it might help to just install the GPU driver first separately from the CUDA library. After installing the driver, just select no when asked to install the GPU driver in the installation procedure for CUDA.
- If your getting the "ImportError: libcudnn.so.6: cannot open shared object file: No such file or directory" error when importing TensorFlow, then you need to download version 6 of cuDNN (specifically, the version 6 that is also compatible with the CUDA version you installed)

### Some useful commands
- Check version of graphics card driver: `nvidia-smi`
- Check version of CUDA installed (requires nvidia-cuda-toolkit): `nvcc --version`
- Uploading files from my local machine to host
    + `scp localfile <username>@<ip address>:~/remotefolder`
- Check version of tensorflow installed without importing it: `pip list | grep tensorflow`
- How to monitor GPU utilization
    + `watch -n 5 nvidia-smi -a --display=utilization`
- Monitor GPU temperature
    + `watch -n 5 nvidia-smi -q -d temperature`

### Good references
1. http://tuatini.me/part-1-how-to-setup-your-own-environment-for-deep-learning/
2. http://www.python36.com/install-tensorflow141-gpu/
3. http://deeplearning.lipingyang.org/2017/01/18/install-gpu-tensorflow-ubuntu-16-04/
4. NVIDIA's documentations

