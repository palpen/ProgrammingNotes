# Notes on Kubernetes

## What is Kubernetes?
["...container-focused cluster management thing"](http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/)

## FAQs
* What lives inside a pod? Containers (e.g. Docker)
* How many containers can live in a pod? Any number, but usually just two
* Where do pods live? In a node
* What is a node? A physical or virtual machine (e.g. in GCP, a VM instance)
* How many pods can live in a node? Any number, but constrained by number of cores and memory available in the node



## Resources to Learn
* [A few things I've learned about Kubernetes by Julia Evans](https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/)
	* Contains good references for beginners
	* See section on "__Kubernetes from the ground up__"
* [Kubernetes BootCamp](https://kubernetesbootcamp.github.io/kubernetes-bootcamp/)
* [The Illustrated Childrens Guide to Kubernetes](https://cdn.chrisshort.net/The-Illustrated-Childrens-Guide-to-Kubernetes.pdf)