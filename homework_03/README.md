### Домашнее задание "Docker контейнер c веб-приложением"
Build:

```commandline
docker build . -t web
```

Run:

```commandline
docker run -d -p 8080:8000 web
```