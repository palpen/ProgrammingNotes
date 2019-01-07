# Notes on Google Cloud Platform Services

## Useful commands using the Google Cloud SDK
* Listing all VM instances:
    * `gcloud compute instances list`
* Starting an existing instance:
    * `gcloud compute instances start <INSTANCE NAME>`
* SSH into an instance:
    * `gcloud compute ssh <INSTANCE NAME>`
* Shutting down an instance:
    * `gcloud compute instances stop <INSTANCE NAME>`
* Copying a file to or from an instance
    * TO: `gcloud compute scp <LOCAL_FILE_PATH> <INSTANCE_NAME>:~/`
    * FROM: `gcloud compute scp <INSTANCE_NAME>:~/ <LOCAL_FILE_PATH>`

### To do after setting up a new VM Instance
  * First, run `sudo apt update && sudo apt upgrade`
  * git: `sudo apt-get install git`
  * tmux: `sudo apt install tmux`

## Google Cloud Storage (gsutil)
* Copy from gcs storage
   * gsutil -m cp -r dir gs://mybucket .
   * -m is for multithreading, cp is to copy, -r is for recursive copy if copying a directory
