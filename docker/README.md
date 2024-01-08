## Task for @florentin:
You need to write the different steps to deploy the database for someone taking over the repo

```bash
docker compose --env-file ./deployment.env config

docker compose --env-file ./deployment.env up

```

## Build & push the docker image

```bash
cd cosomis/
docker build . -t cosobenin/mis-app:latest
docker push cosobenin/mis-app:latest
```

## Deploying the app

```bash
cd docker/app

# update the deployment.env

# initiate the certificate
sudo ./init-letsencrypt.sh

# check if `/data/certbot/conf` contains the certificates
docker compose --env-file ./deployment.env up

```


ssl_doc: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71


