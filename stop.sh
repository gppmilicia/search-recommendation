#!/usr/bin/env bash

docker-compose down
rm -f extract_data.csv

#docker volume rm $(docker volume ls -qf dangling=true)
#docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
#docker rm $(docker ps -qa --no-trunc --filter "status=exited")
#yes | docker system prune