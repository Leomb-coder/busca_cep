import psycopg2
import os



def get_connection():
    try:
        # Se a variavel DB_HOST da .env for localhost (banco rodando na máquina): faça a conexão com o banco de dados
        if os.getenv('DB_HOST') == 'localhost':
            # Usa as variaveis da .env para criar a conxão com o banco de dados
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                sslmode='disable',
                channel_binding='disable'
            )
            return conn
        else:
            # Se o DB_HOST não for localhost (banco na nuvem) crie a conexão com o banco na nuvem
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                sslmode=os.getenv('DB_SSLMODE'),
                channel_binding=os.getenv('DB_CHANNEL_BINDING')
            )
            return conn

    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None