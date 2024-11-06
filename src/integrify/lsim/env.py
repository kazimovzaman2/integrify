import os
from enum import Enum
from typing import Literal
from warnings import warn

VERSION = '1.0.3'

LSIM_BASE_URL = os.getenv("LSIM_BASE_URL", "")
LSIM_LOGIN = os.getenv("LSIM_LOGIN", "")
LSIM_PASSWORD = os.getenv("LSIM_PASSWORD", "")
LSIM_SENDER = os.getenv("LSIM_SENDER", "")

if not LSIM_BASE_URL or not LSIM_LOGIN or not LSIM_PASSWORD or not LSIM_SENDER:
    warn(
        "LSIM_BASE_URL/LSIM_LOGIN/LSIM_PASSWORD/LSIM_SENDER mühit dəyişənlərinə dəyər verməsəniz "
        "sorğular çalışmayacaq!"
    )


class API(str, Enum):
    SEND_SMS: Literal["/quicksms/v1/send"] = "/quicksms/v1/send"


__all__ = [
    "VERSION",
    "LSIM_BASE_URL",
    "LSIM_LOGIN",
    "LSIM_PASSWORD",
    "LSIM_SENDER",
    "API",
]
