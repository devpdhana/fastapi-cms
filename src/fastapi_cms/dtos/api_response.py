from typing import Any
from pydantic import BaseModel


class ApiResponse(BaseModel):
    status: int
    data: Any = None
    message: str
