from typing import TYPE_CHECKING, Any

from integrify.api import APIClient, APIResponse
from integrify.lsim.handlers import SendSmsHandler
from integrify.lsim import env
from integrify.lsim.schemas.response import SendSmsResponseSchema
from pydantic_extra_types.phone_numbers import PhoneNumber


class LsimClientClass(APIClient):
    """LSIM sorğular üçün baza class"""

    def __init__(self, sync: bool = True):
        super().__init__("LSIM", "https://apps.lsim.az", None, sync)

        self.add_url('send_sms', env.API.SEND_SMS, "POST")
        self.add_handler('send_sms', SendSmsHandler)

    if TYPE_CHECKING:
        def send_sms(
                self,
                mobile: PhoneNumber,
                message: str,
                unicode: bool = False,
                **extra: Any,
        ) -> APIResponse[SendSmsResponseSchema]:
            """SMS göndərmə sorğusu

            **LSIM** /quicksms/v1/smssender

            Example:
            ```python
            from integrify.lsim import LsimRequest

            LsimRequest.send_sms(
                mobile="+99450XXXXXXX",
                message="Hello World"
            )
            ```

            **Cavab formatı: [`SendSmsResponseSchema`][integrify.lsim.schemas.response.SendSmsResponseSchema]**

            Args:
                successMessage:  Əməliyyatı uğurlu keçdiyi haqqında mesaj. Məcburi arqument deyil.
                errorMessage:  Əməliyyatı uğursuz keçdiyi haqqında mesaj. Məcburi arqument deyil.
                obj: Əməliyyatın tranzaksiya ID-si. Numerik dəyər.
                errorCode:  Əməliyyatın uğursuz keçdiyi təqdirdə errorun kodu. Numerik dəyər. Maksimal uzunluq: 1000 simvol. Məcburi arqument deyil.
            """  # noqa: E501


LsimRequest = LsimClientClass(sync=True)
LsimAsyncRequest = LsimClientClass(sync=False)