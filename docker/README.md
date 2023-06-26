## Deploying from  compose

```bash
docker compose --env-file ./deployment.env config

docker compose --env-file ./deployment.env up

```

## Build & push the docker image

```bash
cd cosomis/
docker login # using cosobenin dockerhub account
docker build . -t cosobenin/mis-app:latest
docker push cosobenin/mis-app:latest
```

## Deploying the app

```bash
cd docker/app

# update the deployment.env -> .env

docker compose --env-file ./deployment.env up
```



