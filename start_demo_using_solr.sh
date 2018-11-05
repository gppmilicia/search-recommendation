#!/usr/bin/env bash

docker-compose up --no-start
docker-compose start

# Just to be sure that service are started
sleep 10

# Create database
docker exec -it mysql-test-mil /bin/bash -c "mysql -uroot -proot -e 'CREATE DATABASE IF NOT EXISTS test_21b;'"
# Create table and load signals data to DB
docker exec -it mysql-test-mil /bin/bash -c "mysql -uroot -proot test_21b < /script/load_data.sql"

# Extract data grouped by tag_id
docker exec -it mysql-test-mil /bin/bash -c "rm -f /var/lib/mysql-files/extract_data.csv || true"
docker exec -it mysql-test-mil /bin/bash -c "mysql -uroot -proot test_21b < /script/extract_data.sql"
docker cp mysql-test-mil:/var/lib/mysql-files/extract_data.csv extract_data.csv

# Index extracted data to solr
docker cp extract_data.csv solr-test-mil:/extract_data.csv
docker exec -it solr-test-mil /bin/bash -c "bin/post -c tag_user_view /extract_data.csv"

echo -e "\nTo see the recommendation, go to:"
echo -e "\n\thttp://localhost:8983/solr/tag_user_view/mlt?q=ff0d3fb21c00bc33f71187a2beec389e9eff5332"
echo -e "\n"