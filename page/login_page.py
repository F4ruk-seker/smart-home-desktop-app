from nicegui import ui, app
from auth import Auth

auth = Auth()


def login_view():
    def login_wrapper(username,password):
        if auth.login(username, password):
            ui.open('main')
    with ui.column().classes('container mx-auto '):
        ui.label('Login - SMART HOME').classes('mx-auto')
        with ui.column().classes('w-78 mx-auto'):
            username = ui.input(label='Username').classes('w-full text-lg block')
            password = ui.input(label='Password', password=True).classes('w-full text-lg block')
            # ui.button('Login').classes('w-full text-lg block').on('click', print, [username,password])
            ui.button('Login', on_click=lambda x: login_wrapper(username.value, password.value)).classes('w-full text-lg block')

