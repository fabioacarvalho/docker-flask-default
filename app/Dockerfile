FROM python:3.12-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia o código da aplicação
COPY . /app/

# Variáveis de ambiente para otimização
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBEFFERED=1

# Instalar dependências do sistema necessárias para o mysqlclient
RUN apk add --no-cache \
    mariadb-dev \
    build-base \
    libffi-dev \
    openssl-dev \
    pkgconfig

# Atualizar o pip e instalar os pacotes Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta do Flask
EXPOSE 5000

# Define o comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--reload"]