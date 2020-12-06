# Lab4
---
### 1. Ознайомилася з Docker.
---
### 2. Виконала команди:
   - sudo docker -v
   - sudo docker -h
   - sudo docker run docker/whalesay cowsay Docker is fun
   - **Перенаправила вивід в my_work.log:**
       - sudo docker -v > my_work.log 
       - sudo docker -h >> my_work.log 
       - sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log
---
### 3. Ознайомилася з документацією
---
### 4. - Виконала команди:
   - "sudo docker pull python:3.8-slim"
   - "sudo docker images"
   - "sudo docker inspect python:3.8-slim"
   - **Створила файл з іменем Dockerfile;**
   - **Замінила посилання на власний Git репозиторій**
---
### 5. Створила власний репозиторій на Docker Hub
---
### 6. Виконала команди:
   - sudo docker build -t diano4ka/lab4:django .
   - sudo docker images
   - sudo docker push odiano4ka/lab4:django
   - [repo](https://hub.docker.com/repository/docker/diano4ka/lab4)
   - [django image](https://hub.docker.com/layers/128886921/diano4ka/lab4/django/images/sha256-92d70b4fa54be0d51e68cb1f9ad8aef43d3a3daaaa801c05434a5df34e5526eb?context=explore)
---
### 7. Веб-сайт працює
---
### 8. 
   - створила Dockerfile.site
   - Виконала білд імеджа:
       - sudo docker build -f /home/diana/cautious-spoon/lab4/Dockerfile.site  -t diano4ka/lab4:monitoring .
       - sudo docker images
       - sudo docker push diano4ka/lab4:monitoring 
       - [monitoring image](https://hub.docker.com/layers/128888076/diano4ka/lab4/monitoring/images/sha256-3e0bf5962a460a71acfdd0189e835e62a24b63c1ef90bf4bb5dd2ae63dfd00ae?context=explore)
   - Виконала команди:
       - sudo docker run -it --rm -p 8000:8000 diano4ka/lab4:django
       - sudo docker run --net=host -it --rm diano4ka/lab4:monitoring
   - Щоб отримати логи виконала команду:
       - sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log diano4ka/lab4:monitoring
