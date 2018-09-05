# Linux

Notes from the book "The Linux Programming Interface" by Michael Kerrisk.

See the docker_fun repository for Dockerfile that builds a simple Ubuntu image with basic tools

## 1. History
What is Linux?
* The kernel for the UNIX system developed by the GNU project. The kernel was written by a really smart Finnish guy named Linus Torvalds

What is POSIX?
* POSIX is an abbreviation of Portable Operating System Interface. There are a wide variety of UNIX implementations, which made porting applications across systems very difficult. POSIX is a set of standards developed to alleviate this problem. The macOS, for example, is a POSIX compliant operating system.

## 2. Fundamental Concepts

What is an operating system?
* The software managing a computer's resource and all of the accompanying software tools such as the command-line interpreter, gui, file utilies, and editors

What is a kernel? How is it different from an operating system?
* The part of the operating system that focuses on the management and allocation of the computer's resources (CPU, RAM, and devices)
* More precisely, the kernel performs process scheduling, memory management, file system provision, creation and termination of processes, device access, networking, and provision of system call API (i.e. processes can request kernel to perform task using kernel entry points called _system calls_).

What are processes?
* Processes (e.g. a running Python program) can be thought of as workers. The kernel is the manager. Processes doesn't know when it will be terminated, or when other processes will be scheduled for the CPU. All signal delivery is mediated by the kernel. 
* Processes operate in isolation. Processes can't create new processes or end its own existence. These things are all mediated by the kernel, which maintains data structures about all running processes


What is a shell?
