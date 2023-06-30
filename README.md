# 🎩 Just a simple test task 
Simple django proj. dockerized

## 🖥️ Technologies 
![Python](https://img.shields.io/badge/-Python-blue?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-yellow?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-blue?style=for-the-badge&logo=docker&logoColor=white)
![Django](https://img.shields.io/badge/-Django-green?style=for-the-badge&logo=django&logoColor=white)


## 📝 Requirements

- Python 3.7+
- Django 4.2.1+
- PostgreSQL

## 🛠 Before installation
1. Clone the project repository

```bash
git clone https://github.com/Anatolii-Poznyak/new_test_task.git
cd new_test_task
```
2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Create .env file based on .env.sample file and set variables.

```bash
cp .env.sample .env
```

- If you want to use Docker, set `POSTGRES_HOST=db` 
- Also set your superuser credentials in `.env`

## 🐳 Run with DOCKER
- DOCKER should be installed

```shell
  docker-compose up
```
- The server will run on 127.0.0.1:8000
- superuser and fake_data will be created and loaded automatically via custom migrations 


## 📚 Additional info
- To enter the container => `docker compose exec app sh` or `docker exec -it <your container name> /bin/bash`
- Containers list => `docker ps`
- Fake data is generated by `fake_data.py` command
