# ML1
This is first Machine Learning Project 

To add a file
```
git add <file_name>
```
To cheak the url
```
git remote -v
```
To create a version or commit
```
git commit -m "<message>"

To setup CI/CD pipeline in heroku we need 3 information
1. Heroku_Email= akshaykadama9@gmail.com
2.Heroku_API_Key= 676bf7ea-84d8-4076-b323-06b6d0229f1e
3.Heroku_app_name= ml-regression-app99

Build docker image
```
docker build -t <image name>:<tagname>


To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 ba94806bcf01
```
To cheak running container in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
