# Notes on Docker

# Concepts
* "A Docker __image__ is an executable package that includes everything needed to run an application---the code, a runtime, libraries, environment variables, and config files"
* A __container__ is a runtime instance of an image (an image with state or a user process). Use `docker ps` to see a list of running containers
* "__containers__ runs natively on Linux and shares the kernel of the host machine with other containers"
* A __virtual machine__ on the other hand runs a full-blown guest operating system with virtual access to the host computer's resources through a hypervisor. VMs demand more resource than what is needed by a given application that can be run in a container.

# Getting Started

1. Run bash in a container in interactive mode:
Say you have the `ubuntu` image (check with `docker image`). To access bash in its container in interactive mode, run
```bash
docker run -i -t ubuntu bash
```

# Useful Docker commands

1. List active docker containers: `docker ps`
2. Open multiple terminals on a docker container: `docker exec -it <container name> bash`
	- You can get container name from `docker ps`
3. How to get access to data in the host from inside a container
	- `docker run -it -v /path/in/host:/path/in/container <docker image name>`
		- This gives access to the data in the host (found in /Users/s6215054/Desktop/courses/python-spark-datascience), which can be found in /home/jovyan/work in the container

4. How to set own name for docker container
	- `docker run --name <MY_CUSTOM_NAME> <DOCKER_IMAGE>`
5. How to exit docker container in interactive mode
	- Just type `exit`
6. Delete image by image id: `docker rmi <IMAGE ID>`
7. List all images: `docker images`
8. List all containers: `docker ps`
9. Kill an active container: `docker kill <CONTAINER ID>`

# Dockerfile

# Additional Notes and Features

- the -it options run docker in interactive mode (i.e. it takes you inside and container and do stuff in it). Alternatively, you can run it in detached mode by using the -d option
