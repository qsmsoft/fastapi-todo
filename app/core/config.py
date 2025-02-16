import os

import redis
from dotenv import load_dotenv

load_dotenv()

class Configs:
    @staticmethod
    def database_url() -> str:
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')

        return f'postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    @staticmethod
    def redis_connector() -> redis.Redis:
        redis_host = os.getenv('REDIS_HOST')
        redis_port = int(os.getenv('REDIS_PORT'))
        redis_db = int(os.getenv('REDIS_DB'))
        redis_decode_responses = os.getenv('REDIS_DECODE_RESPONSES')

        return redis.Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=redis_decode_responses)

    @staticmethod
    def jwt_config() -> dict:
        secret_key = os.getenv('SECRET_KEY')
        algorithm = os.getenv('ALGORITHM')
        access_token_expire_minutes = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

        return {
            'secret_key': secret_key,
            'algorithm': algorithm,
            'access_token_expire_minutes': access_token_expire_minutes
        }