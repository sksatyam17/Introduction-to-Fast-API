from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
    return "Hello from StackUp :D Answer is A"
