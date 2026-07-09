from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Intelligence OS",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Enterprise Intelligence OS",
        "version": "0.1.0"
    }