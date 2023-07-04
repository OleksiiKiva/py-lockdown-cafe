import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You should be vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        current_date = datetime.date.today()
        if expiration_date < current_date:
            raise OutdatedVaccineError("Your vaccine has expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should buy a mask")

        return f"Welcome to {self.name}"