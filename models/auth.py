from dataclasses import dataclass

@dataclass
class AuthModel:
    refresh: str
    access: str

    def __init__(self, json: dict):
        self.json.update(json)

    @property
    def json(self):
        return self.__dict__

