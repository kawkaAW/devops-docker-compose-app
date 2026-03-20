Devops Docker Compose App

Simple devops project demonstrating: Docker, Docker Compose, Flask API, PostgreSQL, Enviroment variables, persistent volumes

Stack: Python - flask, docker, docker compose, postgresql.|

Run project: bash
docker compose up --build

This project uses GitHub Actions for continuous integration. On every push 'main', the Docekr image built automatically.

Pipeline: 
-build docker file
-run container
-test application endpoint
-stop and remove container

[![CI Pipeline](https://github.com/kawkaAW/devops-docker-compose-app/actions/workflows/ci.yml/badge.svg)](https://github.com/kawkaAW/devops-docker-compose-app/actions/workflows/ci.yml)