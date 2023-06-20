import functools

from nicegui import ui, app
from auth import Auth
from requests import api
from config import API_HOST
from models import ESPModel, KeyModel

auth = Auth()


def get_esp_list():
    auth.refresh_access()
    header = auth.get_header()
    path = API_HOST / 'esp/'
    esp_list = api.get(path, headers=header)
    if esp_list.status_code == 200:
        esp_list_model: list[ESPModel] = []
        for esp in esp_list.json():
            key_model_list: list[KeyModel] = []
            for key_json in esp.get('keys'):
                key_model_list.append(
                    KeyModel.load_from_json(key_json)
                )
            esp_list_model.append(ESPModel(
                esp_id=esp.get('esp_id', None),
                name=esp.get('name', None),
                is_connected=esp.get('is_connected', None),
                keys=key_model_list
            ))

        return esp_list_model


def change_key_status(key_id, status):
    auth.refresh_access()
    header = auth.get_header()
    path = API_HOST / f'esp/key/{key_id}'
    key = api.put(path, headers=header, data={
        "current": status
    })
    if key.status_code == 200:
        ui.notify('Key change')


def main_view():
    with ui.column().classes('container mx-auto'):
        ui.label('Smart ROOM - PARS').classes('text-lg text-center mx-auto')
        ui.label('ESP').classes('inline-block text-lg text-center')

        for esp in get_esp_list():
            with ui.row().classes('w-full grid  grid-cols-3').style('display:flex'):

                if esp.is_connected:
                    ui.icon('favorite').classes('pt-1').props('color=green')
                else:
                    ui.icon('favorite_border').classes('pt-1').props('color=red')
                ui.label(esp.name).classes('text-lg')
            with ui.row():
                for key in esp.keys:
                    with ui.card():
                        ui.label(key.name)
                        ui.switch(text=key.id,value=key.current, on_change=lambda x: change_key_status(x.sender.text, x.value))

