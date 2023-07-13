from fastapi import FastAPI

app = FastAPI()

# a fastapi running on ip 127.0.0.1 and port 8000


@app.get('/')
def get():
    return {'message': 'request received'}

# uvicorn api:app --reload
