# Notes and useful command in TensorFlow

## Installation
- If your system currently only have CUDA 8.0 (check with `nvcc --version`), the only compatible version of Tensorflow is 1.4. Install the GPU enabled version (inside your virtual environment) by running `pip install tensorflow-gpu==1.4`
- See this link for tested source configurations: https://www.tensorflow.org/install/install_sources#common_installation_problems

## Switch between GPU and CPU for training
Set GPU to 0 below for no GPUs (e.g. use CPU only). Set to 1 and TensorFlow will automatically use the GPU.
```
config = tf.ConfigProto(
    device_count = {'GPU': 0}
)
sess = tf.Session(config=config)
```


