# Week 1 - Setting up.

## Setting up docker.
We will be utilizing Docker heavily throughout the course to simulate a production enviroment.  You can install it on your local machine or an AWS instance by following the instructions on the Docker website.

### For windows
https://docs.docker.com/docker-for-windows/

### For Mac
https://docs.docker.com/docker-for-mac/

### For Ubuntu Users
https://docs.docker.com/engine/installation/linux/ubuntu/

### Setting up python
While most of our development will be tested with containers you will still need python installed on your local system for utilization of tools like docker-compose (more on that in a minute) and your editor tools.
The best guidline you can find for setting up python on your various systems is the Appendix "Setting up your System" in *How to Tango With Django*.


### Docker Compose
Along with just docker we will also be utilizing docker-compose.  Docker compose allow a very simple local orchestration of containers, simulating a production enviroment.  You can install docker-compose easily by using pip which was covered in the book while installing python. We're going to assume we're all using python3 for this course.
`pip3 install docker-compose`

Additional instructions if needed can be found at https://docs.docker.com/compose/install/

### MySQL tools
I'll mostly be using mysql cli tools to connect to our database in the class.  However for those of you that like visual tools and queues I suggest downloading the MySQL Workbench at https://dev.mysql.com/downloads/workbench/
You can run our mysql instance by going to the root directory in a terminal and typing `docker-compose up mysql`.  This will launch only the mysql container.  If you want to launch a container to serve your django application you will want to `docker-compose up` this will build a python container with django and mount the local folder into the container.  We'll now do some work so we can actually serve our first file from the container.

### Git
You can install git by following the official instructions. https://git-scm.com/book/en/v2/Getting-Started-Installing-Git  I then suggest you also be signed up for GitHub and fork this repository for your submissions by following these instructions https://help.github.com/articles/fork-a-repo/ I will go over git alot more in the synchronous session.

### Setting up your django project
There are two ways to do this.  If you want to do as much local development as you can outside of containers `pip3 install django==1.9` to add django to your local python install (also good anyway for IDE support). My preferred way is to run `docker-compose run django bash` which will drop you into a container's bash and have your development folder mounted there. This way you get an easy connection to your mysql server and can run all of your admin tasks easily.  We can now follow along with the book starting at chapter 3.2.  Create your own project and follow along to the end of chatper 3.  Complete the assignment by creating your own fork of this repository and adding the files that you create to your fork.  I also request you when you're done you tag the final commit with `git tag week1` and then do a `git push origin --tags` so it's easy for me to follow where you are and how well you have done.

NOTE: If you want to run your project in a container for sering run `docker-compose run -p 8000:8000 django bash` or ad a command to the docker-compose.yaml to do it for you. https://docs.docker.com/compose/compose-file/#command


### IDE
If you want to use a full fledged IDE I recommend PyCharm EDU for the class.  You can configure it with docker by following instructions at https://blog.jetbrains.com/pycharm/2017/03/docker-compose-getting-flask-up-and-running/  I use Vim or Emacs for all of my coding.


