import os
from enum import Enum
from typing import Literal
from warnings import warn

VERSION = '1.0.3'

LSIM_LOGIN: str = os.getenv("LSIM_LOGIN", "")
LSIM_PASSWORD: str = os.getenv("LSIM_PASSWORD", "")
LSIM_SENDER: str = os.getenv("LSIM_SENDER", "")

if not LSIM_LOGIN or not LSIM_PASSWORD or not LSIM_SENDER:
    warn(
        "LSIM_LOGIN/LSIM_PASSWORD/LSIM_SENDER mühit dəyişənlərinə dəyər verməsəniz "
        "sorğular çalışmayacaq!"
    )


class API(str, Enum):
    SEND_SMS: Literal["/quicksms/v1/smssender"] = "/quicksms/v1/smssender"


__all__ = [
    "VERSION",
    "LSIM_LOGIN",
    "LSIM_PASSWORD",
    "LSIM_SENDER",
    "API",
]
