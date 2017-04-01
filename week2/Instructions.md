#  Week 2: Templates, Database and Views

### Review Chapters 4, 5 and 6
Read through chapters 4, 5 and 6 doing the exercies at the end of each chapter. Once you have completed those those commit the code and tag it as week2.1

### Using mysql instead of sqlite
We will go over this in the synchronous session but I want you to replicate it as tag week2.2
Update the Dockerfile to install the MySQL development headers.
`apt-get install libmysqlclient-dev`

Update the requirements.txt file in the repository to add the Python MySQL driver.
`mysqlclient`
Note that for python 2.7 it is `MySQL-python` but the original maintainer never commited to python 3 support so the project was forked and updated.

Rebuild the docker container in one of the following ways.
1. `docker-compose build`
2. Remove existing django containers by using `docker ps -a` to get the names or hashes and `docker rm` to delete the container. Then use `docker images` to find hte image name and `docker rmi` to remove it.  Then you just have to `docker-compose up` to build the image anew.

Once the containers are running bash into the django container and use the mysql client to create the new data base.
Update settings.py so it looks like this.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rango',
        'USER': 'root',
        'PASSWORD': 'unsecure',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

Now apply your migrations and test your generation scripts out on the MySQL database.  The data in the database will persist in the MySQL container until you rm the container instance.
Tag your changes as week2.2 and push the code and tags to your fork.
