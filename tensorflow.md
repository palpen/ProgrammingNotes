# Notes and useful command in TensorFlow

## Switch between GPU and CPU for training
Set GPU to 0 below for no GPUs (e.g. use CPU only). Set to 1 and TensorFlow will automatically use the GPU.
```
config = tf.ConfigProto(
    device_count = {'GPU': 0}
)
sess = tf.Session(config=config)
```


