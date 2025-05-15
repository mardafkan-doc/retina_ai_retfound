FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git gdown

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN gdown --id 160tgvEj0vtMwbyN8joOiUEAGumhB4Hl1 -O RETFound_oct_weights.pth

COPY . .

CMD ["python", "main.py"]