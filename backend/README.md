# Bet App Backend

## Install the dependencies
```bash
pip install -r requirements.txt
```

### Start the api in development mode
```bash
fastapi dev src/main.py
```

### Build docker image
```bash
docker build -t bet-api .
```

### Run docker container
```bash
docker run -d -p 3000:80 --env-file .env bet-api
```