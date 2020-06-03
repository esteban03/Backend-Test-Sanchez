import abc


class NotifierInterface(abc.ABC):
    """
    Object to create implementations to notify.
    Example: slack, email, twitter, etc.
    """

    @abc.abstractmethod
    def send_message(self, message):
        pass
