# Começamos com uma imagem oficial do Python 3.9
FROM python:3.9

# Definimos a pasta de trabalho dentro do contentor
WORKDIR /app

# Copiamos o ficheiro de dependências para dentro do contentor
COPY ./requirements.txt /app/requirements.txt

# Instalamos as dependências
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiamos o resto do código da nossa aplicação para dentro do contentor
COPY . /app

# O comando que será executado quando o contentor iniciar.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]