from fastapi import FastAPI

app = FastAPI(title="Gazzela API") 

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gazzela API! 🏃💨"}