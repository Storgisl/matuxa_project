from aiogram.filters import BaseFilter
from aiogram.types import Message

from botik.settings import settings

class IsAdminFilter(BaseFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        if user_id==settings.bots.admin_id:
            return True
        else:
            return False