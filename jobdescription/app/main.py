
from fastapi import FastAPI
from api.jobdescription import database_config
from api.jobdescription.models import metadata, job_descriptions
from api.jobdescription.jobdescription import router as job_description_router
from api.jobdescription.list_jobdescriptions import router as list_jobdescriptions_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Create tables if they don't exist
    metadata.create_all(bind=database_config.engine)
    await database_config.database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database_config.database.disconnect()

app.include_router(job_description_router, prefix="/api/v1/jobdescription", tags=["jobdescription"])
app.include_router(list_jobdescriptions_router, prefix="/api/v1/listjobdescription", tags=["listjobdescriptions"])
# app.include_router(edit_jobdescription_router, prefix="/api/v1/editjobdescription", tags=["editjobdescription"])
# app.include_router(delete_jobdescription_router, prefix="/api/v1/deletejobdescription", tags=["deletejobdescription"])
