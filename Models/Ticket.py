from pydantic import BaseModel, Field, field_validator, computed_field


class TicketModel(BaseModel):
    title: str
    description: str | None = Field(
        max_length = 15000
    )
    candidates: list[str]

    @field_validator('candidates')
    @classmethod
    def candidates_must_be_unique_and_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise ValueError('candidates must not be empty')

        if len(set(v)) != len(v):
            raise ValueError('candidates must be unique')

        return v