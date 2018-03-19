# Notes and useful command in TensorFlow

## Installation

To use Keras, you must first install TensorFlow. If you are using a virtual environment (which you should), you must __deactivate and reactivate__ the virtual environment after installing both Keras and TensorFlow.

### TensorFlow
- If your system currently only have CUDA 8.0 (check with `nvcc --version`), the only compatible version of TensorFlow is 1.4. Install the GPU enabled version (inside your virtual environment) by running `pip install tensorflow-gpu==1.4`
- See this link for tested source configurations: https://www.tensorflow.org/install/install_sources#common_installation_problems
- Deactivate and reactivate virtual environment

### Keras
- Inside the virtual environment, `pip install keras`
- Deactivate and reactivate virtual environment

To test the installation, just import keras. You should see a message stating that it is using the TensorFlow backend.

## Switch between GPU and CPU for training
Set GPU to 0 below for no GPUs (e.g. use CPU only). Set to 1 and TensorFlow will automatically use the GPU.
```
config = tf.ConfigProto(
    device_count = {'GPU': 0}
)
sess = tf.Session(config=config)
```

## Check to see that GPU is available
```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```


