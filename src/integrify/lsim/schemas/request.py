from integrify.lsim import env
from integrify.schemas import PayloadBaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class SendSmsRequestSchema(PayloadBaseModel):
    mobile: PhoneNumber
    message: str
    unicode: bool = False


