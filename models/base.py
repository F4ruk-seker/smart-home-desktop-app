
class Base:
    def __init__(self, json: dict):
        self.json.update(json)

    @property
    def json(self):
        return self.__dict__

