from telegram.ext import MessageFilter
from tobrot import AUTH_CHANNEL, OWNER_ID


class CustomFilters:
    class _OwnerFilter(MessageFilter):
        def filter(self, message):
            return message.from_user.id == OWNER_ID

    owner_filter = _OwnerFilter()

    class _AuthorizedUserFilter(MessageFilter):
        def filter(self, message):
            id = message.from_user.id
            return id in AUTH_CHANNEL or id == OWNER_ID

    authorized_user = _AuthorizedUserFilter()

    class _AuthorizedChat(MessageFilter):
        def filter(self, message):
            return message.chat.id in AUTH_CHANNEL

    authorized_chat = _AuthorizedChat()
