from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values

config = dotenv_values(".env")

app = FastAPI()


@app.get("/")
def send_example_message() -> str:
    return "DA LADNO!"


if __name__ == "__main__":
    host = config['HOST_DEV']

    if config['PRODUCTION'].lower() == "true":
        host = config['HOST_PROD']

    uvicorn.run(
        "main:app",
        host=host,
        port=int(config['PORT']),
        reload=config['RELOAD'].lower() == "true"
    )
