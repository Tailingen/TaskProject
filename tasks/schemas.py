from pydantic import BaseModel, Field

class TaskAddSchema(BaseModel):
    text: str = Field(min_length=2, max_length=255)
    status: bool = False