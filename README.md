# ServingMLFastCelery
Working example for serving a ML model using FastAPI and Celery, from [this article](https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db). This for includes a docker-compose taken from [here](https://github.com/RTae/yolor_trt) and modified to use only Redis and drops RabbitMQ used in the original example

## Docker
Run `docker-compose build` then `docker-compose up` then navigate to [http://localhost:8000/docs](http://localhost:8000/docs)

Build the app seperately:
```
docker build -t ml-app .
```
Note there are many requirements, so I had to unpin a bunch of these to successfully build.