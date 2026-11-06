from fastapi import FastAPI

from fastapi_cms.routes.ticket_router import router as ticket_router

app = FastAPI()

app.include_router(router=ticket_router)


@app.get("/health")
def health_check():
    return {"status": "Server running"}
