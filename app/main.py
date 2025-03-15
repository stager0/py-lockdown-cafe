import datetime


class OutdatedVaccineError(Exception):
    pass


class NotVaccinatedError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        actuel_data = visitor["vaccine"].get["expiration_date"]
