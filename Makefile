WORKDIR = apps

run: print docker-run main-run docker-stop

main:
	python $(WORKDIR)/main.py

old:
	python $(WORKDIR)/generate_old_data.py

print:
	echo "Hello World"

docker-run:
	docker-compose up -d

docker-stop: COMPOSE ?= docker-compose
docker-stop:
	$(COMPOSE) stop

docker-stop-all: CONTAINERS ?= $(shell docker ps -q)
docker-stop-all:
	docker stop $(CONTAINERS)
