
IMPORTANT NOTE:
- Keep in mind that this is kinda old code that uses deprecated features.
	If in doubt, it was tested with:
	- python's scikit==0.17.2
	- python's elasticsearch==7.9.1
	- docker's elasticsearch==7.9.2

Installation:
1. ElasticSearch
	Can be easily installed with Docker.
	DockerHub: https://hub.docker.com/_/elasticsearch/?tab=description
	Example command:
	//$ docker network create elasticnetwork
	//$ docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.9.2
	Or without private network (we want to access this container from outside):
	//$ docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.9.2
	It seems that my architecture was incompatible with machine learning. I had to disable it:
	$ docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "xpack.ml.enabled=false" -e "discovery.type=single-node" elasticsearch:7.9.2

2. CollectorAssistant ImageMatch
	First, we want to run in venv
	$ ???? create venv ?????
	$ ???? activate venv ???
	Now, we can install Python dependencies.
	$ pip install -r requirements.txt
	And run the server
	$ python main.py
	Bam tam tarampam pam