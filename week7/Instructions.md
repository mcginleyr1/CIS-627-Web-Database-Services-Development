# Week 7
# Reading
Read chatpers 18 and 19. Do the exercises and tag this as Week7.1.

# Deployment
## Stand alone server
You can use docker with an init scrip (init.d, systemd, etc) to run a container on any server.  The general concept of this is that it's minizing your base image.  Do some research and figure out what you think would be the best way to orchestrate containers on bare servers and reply to the discussion question.  I'll put my two cents and experience in.

## Kubernetes
Kubernetes is a reimplmentation and expansion of Google's Borg (https://research.google.com/pubs/pub43438.html).  It allows for orchetration, high availablity of service and many other features.  This is what I use to deploy production systems on docker currently.  Do some research and respond to the discussion thread on kubernetes. http://kubernetes.io/

## Mesos
We're not going to look at this one too much. Mesos is an orchestration system that was orginally designed before containers existed. It utilizes technologies like zookeeper, hadoop, and many others to create a cluster enviroment.  To really make Mesos Work in a timely fashion you need to pay for tooling call DC/OS (data center operating system) from Mesosphere. Feel free to look into it a bit, some much larger organization prefer this and can afford the cost of the tooling (roughyly 100k per year starting price.)

