from fastapi import FastAPI


app = FastAPI()

@app.post('/signup')
async def get_root():
    return {'message' : 'Hello World'}