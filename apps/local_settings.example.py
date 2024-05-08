import os

# Local db
DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ATOMIC_REQUESTS": True,
    }
}

# General
DEBUG = True
STATIC_URL = ""
STATIC_ROOT = ""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, ""), os.path.join(BASE_DIR, "", "")]

AZURE_EVENT_ENDPOINT = ""
QUEUE_NAME = ""
AZURE_EVENT_KEY = ""
