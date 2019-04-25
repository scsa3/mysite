import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

import tkinter
import threading


def run_django():
    application = get_wsgi_application()
    call_command('runserver', '127.0.0.1:8000')


t = threading.Thread(target=run_django)
t.start()
top = tkinter.Tk()
top.mainloop()
