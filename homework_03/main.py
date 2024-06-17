from fastapi import FastAPI, status

app = FastAPI()


@app.get("/ping/", status_code=status.HTTP_200_OK, tags=["ping"])
def get_ping() -> dict[str, str]:
    return {"message": "pong"}
