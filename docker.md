# Useful Docker commands

1. Active docker containers: `docker ps`
2. Open multiple terminals on a docker container: `docker exec -it <container name> bash`
	- You can get container name from `docker ps`

3. How to get access to data in the host from inside a container
	- `docker run -it -v /path/in/host:/path/in/container <docker image name>`
		- This gives access to the data in the host (found in /Users/s6215054/Desktop/courses/python-spark-datascience), which can be found in /home/jovyan/work in the container

4. How to set own name for docker container
	- `docker run --name <MY_CUSTOM_NAME> <DOCKER_IMAGE>`

# Notes on Docker

- the -it options run docker in interactive mode (i.e. it takes you inside and container and do stuff in it). Alternatively, you can run it in detached mode by using the -d option