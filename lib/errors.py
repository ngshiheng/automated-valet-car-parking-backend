class VehicleNotFoundError(BaseException):
    """
    Raised when Vehicle object is not found.
    """

    def __init__(self, number_plate: str):
        self.message = f"Vehicle with number plate ({number_plate}) not found!"
        super().__init__(self.message)
