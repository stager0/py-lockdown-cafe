from datetime import date
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        expiration_data = visitor["vaccine"].get("expiration_date")
        if expiration_data is None or expiration_data < date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
