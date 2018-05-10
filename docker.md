# Useful Docker commands

1. Active docker containers: `docker ps`
2. Open multiple terminals on a docker container: `docker exec -it <container name> bash`
	- You can get container name from `docker ps`

3. How to get access to data in the host from inside a container
	- `docker run -it -v /path/in/host:/path/in/container <docker image name>`
		- This gives access to the data in the host (found in /Users/s6215054/Desktop/courses/python-spark-datascience), which can be found in /home/jovyan/work in the container
