from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=False, strict=True, validation_error_cause=True)


class DefaultResponse(Base):
    status: int
    message: str
    details: Optional[dict[Any, Any]] = Field(default=None)

    model_config = ConfigDict()
