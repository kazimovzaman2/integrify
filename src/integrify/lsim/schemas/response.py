from typing import Optional

from pydantic import BaseModel


class SendSmsResponseSchema(BaseModel):
    successMessage: Optional[str] = None
    errorMessage: Optional[str] = None
    obj: int
    errorCode: Optional[int] = None


class CheckBalanceResponseSchema(BaseModel):
    successMessage: Optional[str] = None
    errorMessage: Optional[str] = None
    obj: int
    errorCode: Optional[int] = None