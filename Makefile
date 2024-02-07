up:
	@docker-compose up -d

down:
	@docker-compose down

build:
	@docker build . -t celery-demo:latest

logs:
	@docker-compose logs -f

ps:
	@docker-compose ps

restart:
	@docker-compose restart
