import json
from config import BASE_DIR


class DataBase:
    def __init__(self):
        self.db_name = BASE_DIR / 'db/.db_obj'

    def get(self, key) -> object:
        data = open(self.db_name, 'r+', encoding='utf-8').read()
        try:
            db = json.loads(data)
            return db.get(key)
        except:
            pass

    def set(self, key, value) -> None:
        try:
            data = open(self.db_name, 'r+', encoding='utf-8').read()
            db = json.loads(data)
            db.update({key: value})
            data = open(self.db_name, 'w', encoding='utf-8')
            data.write(str(json.dumps(db)))
        except:
            pass

