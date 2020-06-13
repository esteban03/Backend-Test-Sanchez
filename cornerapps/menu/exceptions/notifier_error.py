class NotifierError(Exception):

    def __init__(self):
        message = 'Could not notify'
        super().__init__(message)
