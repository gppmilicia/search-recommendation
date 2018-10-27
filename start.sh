#!/usr/bin/env bash

docker-compose up --no-start
docker-compose start

sleep 10

docker cp signals/21B_tag_views_dataset.csv mysql:/21B_tag_views_dataset.csv
docker cp script/load_data.sql mysql:/load_data.sql

docker exec -it mysql /bin/bash -c "mysql -uroot -proot -e 'CREATE DATABASE IF NOT EXISTS test_21b;'"
docker exec -it mysql /bin/bash -c "mysql -uroot -proot test_21b < /load_data.sql"

