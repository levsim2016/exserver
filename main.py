from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def send_example_message() -> str:
    return "Это тестовое сообщение! Привет Олег!"
