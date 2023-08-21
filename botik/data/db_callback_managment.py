from typing import Optional
from aiogram.filters.callback_data import CallbackData

class DbCallbackFactory(CallbackData, prefix="row"):
    action: str
    type: Optional[str] = None