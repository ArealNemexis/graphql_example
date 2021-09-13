from pydantic import BaseSettings


class Envs(BaseSettings):
    HOST_MONGO: str = 'localhost'

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


envs = Envs()
