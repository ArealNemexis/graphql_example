from pydantic import BaseModel
from typing import List


class Campos(BaseModel):
    campos: List[str]
