from pydantic import BaseModel as BaseSchema

class Path(BaseSchema):
    source: str
    destination: str
