from exceptions.fastapi_exceptions import AppError


class DeviceDoesNotFound(AppError):
    def __init__(self):
        super().__init__(3000, "Device not found", 400)

class CorruptedDevice(AppError):
    def __init__(self):
        super().__init__(3001, "Device is corrupted", 400)

class DeviceAlreadyExists(AppError):
    def __init__(self):
        super().__init__(3002, "Device already exists", 400)
