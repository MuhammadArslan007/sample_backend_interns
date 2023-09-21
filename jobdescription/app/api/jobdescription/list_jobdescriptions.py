
from fastapi import APIRouter
from api.jobdescription import database_config
from api.jobdescription.models import job_descriptions

router = APIRouter()

@router.get("/")
async def list_job_descriptions():
    query = job_descriptions.select()
    job_descriptions_list = await database_config.database.fetch_all(query)
    return job_descriptions_list
