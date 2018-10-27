#!/usr/bin/env bash

docker-compose up --no-start
docker-compose start

sleep 10

docker cp signals/21B_tag_views_dataset.csv mysql:/21B_tag_views_dataset.csv
docker cp script/load_data.sql mysql:/load_data.sql
docker cp script/extract_data.sql mysql:/extract_data.sql

docker exec -it mysql /bin/bash -c "mysql -uroot -proot -e 'CREATE DATABASE IF NOT EXISTS test_21b;'"
docker exec -it mysql /bin/bash -c "mysql -uroot -proot test_21b < /load_data.sql"

docker exec -it mysql /bin/bash -c "mysql -uroot -proot test_21b < /extract_data.sql"
docker cp mysql:/var/lib/mysql-files/extract_data.csv extract_data.csv
docker cp extract_data.csv solr:/extract_data.csv

docker exec -it solr /bin/bash -c "bin/post -c tag_user_view /extract_data.csv"