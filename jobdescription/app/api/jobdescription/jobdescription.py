
from fastapi import APIRouter, Form
from . import database_config
from .models import job_descriptions

router = APIRouter()

@router.post("/")
async def create_job_description(title: str = Form(...), description: str = Form(...)):
    async with database_config.database.transaction():
        query = job_descriptions.insert().values(title=title, description=description)
        last_record_id = await database_config.database.execute(query)

    return {"message": "Job description created successfully", "job_id": last_record_id}
