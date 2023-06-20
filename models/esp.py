from dataclasses import dataclass


@dataclass
class KeyModel:
    id: str or None
    name: str
    current: bool

    @classmethod
    def load_from_json(cls, json):
        return cls(id=json.get('id', None), name=json.get('name', None), current=json.get('current', None))

    @property
    def json(self):
        return self.__dict__


@dataclass
class ESPModel:
    esp_id: str or None
    name: str
    is_connected: bool
    keys: list[KeyModel]

    @property
    def json(self):
        return self.__dict__


