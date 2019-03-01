# Notes on Kubernetes

## What is Kubernetes?
["...container-focused cluster management thing"](http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/)

## Why I care about Kubenetes
* For distributed data analytics using [Dask](http://docs.dask.org/en/latest/) in the cloud
* The basic workflow I'd like to master are
	1. Create a cluster in the cloud
	2. Using Dask, offload data preprocessing on cluster
	3. Scale up/down cluster according to needs
* The services I'll need to do this are
	1. Google Kubernetes Engine for creating the Kubernetes cluster
	2. Helm for package management in Kubernetes

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