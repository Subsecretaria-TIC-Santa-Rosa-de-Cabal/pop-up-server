from exceptions.fastapi_exceptions import AppError


class UserNotAuthenticated(AppError):
    def __init__(self):
        super().__init__(1000, "User not authenticated", 401)

class InvalidCredentials(AppError):
    def __init__(self):
        super().__init__(1001, "Incorrect access credentials", 403)

class UserBlocked(AppError):
    def __init__(self):
        super().__init__(1002, "User is blocked", 403)

class InvalidUserToken(AppError):
    def __init__(self):
        super().__init__(1003, "Invalid user token", 401)
