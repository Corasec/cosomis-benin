## Task for @florentin:
You need to write the different steps to deploy the database for someone
taking over the repo

```bash
docker compose --env-file ./deployment.env config

docker compose --env-file ./deployment.env up

```



## Build & push docker image

```bash
cd cosomis/
docker build . -t cosobenin/mis-app:latest
docker push cosobenin/mis-app:latest
```
ssl doc: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71


