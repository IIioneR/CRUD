## About 

When writing this test project I configured / used boilerplate that I become accustumed to at work, and added a few personal preferences.


    1. Having `DB` running as a separate entity
    2. Cool `Makefile` and docker-compose file
    3. isort, flake8 etc.. ( via `make format`)
    4. Adminer ( I like it, because it's light and simple)
    ...

## How to start 

> Consider views the video that I made with a brief overview of the project: _https://www.youtube.com/watch?v=cov_EWYe3D0&feature=youtu.be&ab_channel=%D0%9F%D0%B8%D0%BE%D0%BD%D0%B5%D1%80_

> You can change/configure the `env` variables in `./scripts/env.sh`
Start `db` and `adminer`: with

```bash
$ pip install -r requirements/dev.txt
```

```bash
$ make start_db
```

It will run `Docker` containers described in `./stack.yml`

```bash
$ make run 
```
Then start server for rabbimq and start celery worker
```bash
$ sudo rabbitmq-server
$ celery -A app worker -E -l info
```
Instead of previous way, you can run only docker-compose file
It Will be started all 4 services.(db, server, rabbitmq, celery)
```bash
$ docker-compose build
$ docker-compose up
```
The server should run on http://127.0.0.1:8000/ 

> To apply `autopep8` and `flake8` run:  
```bash
$ make format
```
> Postman collection link _https://www.getpostman.com/collections/5c36f3c5585268a0a059_
