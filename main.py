from auth import Auth
from datetime import datetime
from nicegui import ui, app
from page import login_view, main_view

auth = Auth()

login_page = ui.page('/login')
login_page(login_view)

main_p = ui.page('/main')
main_p(main_view)

if auth.is_login():

    main_view()
else:
    login_view()

app.native.window_args['resizable'] = True
app.native.start_args['debug'] = False

if datetime.now().hour > 20 or datetime.now().hour < 6:
    ui.dark_mode().enable()

ui.run(native=True, window_size=(1280, 720), fullscreen=False, title="F4 |", favicon="🚀")

