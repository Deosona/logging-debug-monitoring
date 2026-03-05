from pydantic import BaseModel

class LogMessage(BaseModel):
    message: str
    level: str = "info"
