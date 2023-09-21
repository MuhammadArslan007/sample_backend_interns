
from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

# Job Descriptions table definition
job_descriptions = Table(
    "job_descriptions",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String(255), index=True),
    Column("description", String(1000)),
)

