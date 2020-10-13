# Chatbot

## Index

- [Challenge](docs/challenge.md) 
- [API V1 doc](docs/api/v1/chatbot.md) 
- [How it was developed](docs/how-developed.md) 
- [Next steps](docs/next-steps.md) 

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 

## How to run the app?
```bash
docker-compose up
```
This command will expose the app under `http://localhost:8000/`

Also, the first time, `docker-compose` will run the migrations and run the crond service.

## How to enter to the container?
After the previous step.

```bash
docker-compose exec app sh
```

## How to run tests?
Once inside the container:
```bash
python manage.py tests
```

## How to run flake8?
Once inside the container:
```bash
flake8
```

## How to run the django commands?
Once inside the container:
```bash
python manage.py [command_name]
```

## How to create a super user?
Once inside the container:
```bash
python manage.py createsuperuser
```

Now you can access via `http://localhost:8000/admin/`

## How to expose the local web server using ngrok?
```bash
ngrok http 8000
```

## What chatbot are you connected to?
You can find the chatbot here: `https://chats.landbot.io/v2/H-667499-R96SNE0MY6FFSL60/index.html`

## Code climate
