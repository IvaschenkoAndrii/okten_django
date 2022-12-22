from datetime import timedelta
from enum import Enum


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RECOVERY = ('recovery', timedelta(minutes=15))

    def __init__(self, token_type, exp_time):
        self.exp_time = exp_time
        self.token_type = token_type