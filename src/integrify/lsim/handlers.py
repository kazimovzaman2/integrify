import json
import hashlib
from typing import Type, Any

from integrify.api import APIPayloadHandler, ResponseType
from integrify.lsim import env
from integrify.lsim.schemas.request import SendSmsRequestSchema
from integrify.lsim.schemas.response import SendSmsResponseSchema, CheckBalanceResponseSchema
from integrify.schemas import PayloadBaseModel


class BasePayloadHandler(APIPayloadHandler):
    def __init__(self, req_model: Optional[Type[PayloadBaseModel]] = None, resp_model: Optional[Type[ResponseType]] = None):
        super().__init__(req_model, resp_model)

    @property
    def headers(self):
        """Sorğunun header-ləri"""
        return {
            "Content-Type": "application/json"
        }

    def post_handle_payload(self, data: Any):
        return json.dumps(data)


class SendSmsHandler(BasePayloadHandler):

    def __init__(self):
        super().__init__(
            req_model=SendSmsRequestSchema,
            resp_model=SendSmsResponseSchema
        )

    def _prepare_key(self, message, mobile):
        return hashlib.md5(
            (
                hashlib.md5(env.LSIM_PASSWORD.encode()).hexdigest()
                + env.LSIM_LOGIN
                + message
                + mobile
                + env.LSIM_SENDER
            ).encode()
        ).hexdigest()

    def handle_payload(self, mobile, message, *args, unicode=False, **kwargs):
        return {
            "login": env.LSIM_LOGIN,
            "key": self._prepare_key(message, mobile),
            "msisdn": mobile,
            "text": message,
            "sender": env.LSIM_SENDER,
            "unicode": unicode
        }


class CheckBalanceHandler(BasePayloadHandler):

    def __init__(self):
        super().__init__(resp_model=CheckBalanceResponseSchema)

    def _prepare_key(self, message, mobile):
        return hashlib.md5(
            (
                hashlib.md5(env.LSIM_PASSWORD.encode()).hexdigest()
                + env.LSIM_LOGIN
            ).encode()
        ).hexdigest()


    def handle_payload(self, *args, **kwargs):
        return {
            "login": env.LSIM_LOGIN,
            "key": self._prepare_key(message, mobile)
        }
