# Search Recommendation
#### These are two small example of recommendation engine based on collaborative filtering

## Requirements
 - Python 3
 - Docker
 - Docker-compose

# Method 1

## Start recommendation engine with Solr
``` bash
 ./start_demo_using_solr.sh
```
 - If you use docker-machine, you need also to add in `/etc/hosts` the line below:
``` bash
 docker-containers-ip-addr  solr mysql
```

## Example of usage
 - 1) Go to: [Recommendation-Engine](http://localhost:8983/solr/tag_user_view/mlt?q=ff0d3fb21c00bc33f71187a2beec389e9eff5332)
 - 2) Change de tag_id to see different result

## Stop recommendation engine
``` bash
 ./stop_demo_using_solr.sh
```

# Method 2

## Start recommendation engine with Python
##### You need a lot of time to calculate similar tags!!!
``` bash
 ./start_demo_using_solr.sh
```

## Contributor
 - Giuseppe Milicia 
