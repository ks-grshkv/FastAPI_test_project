from fastapi import FastAPI
import random

app = FastAPI()


@app.get('/')
def root():
    return {'example': 'Hi there!',
            'data': 0}


@app.get('/random')
def get_rand():
    result = random.randint(0, 100)
    return {'example': 'Hi there!',
            'number': result}
