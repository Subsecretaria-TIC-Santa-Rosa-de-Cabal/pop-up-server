from exceptions.fastapi_exceptions import AppError


class DependencyDeviceCountMustBeZero(AppError):
    def __init__(self):
        super().__init__(2000, "Dependency device count must be zero to disable", 400)
