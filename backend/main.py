from fastapi import FastAPI


app = FastAPI(title="REACLYST API")


@app.get("/")
def root():
    return {
        "project": "REACLYST",
        "status": "running",
        "message": "REACLYST API is online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }