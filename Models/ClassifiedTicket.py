from typing import Dict

from pydantic import BaseModel, Field


class ClassifiedTicketModel(BaseModel):
    title: str
    description: str | None = Field(
        max_length=15000
    )
    classification: Dict[str, float]
