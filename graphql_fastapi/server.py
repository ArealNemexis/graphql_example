import uvicorn
from graphql_fastapi.config import envs
if __name__ == '__main__':
    uvicorn.run('graphql_fastapi:app')
