# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# import Flask 
from flask import Flask

# Inject Flask magic
app = Flask(__name__)

DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# Assets Management
app.config['ASSETS_ROOT'] = os.getenv('ASSETS_ROOT', '/static/assets')

# App Config - the minimal footprint
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'S#perS3crEt_9999') 

app.config['DEBUG'] = str(DEBUG)

# Import routing to render the pages
from app import views

app.logger.info('DEBUG       = ' + str(DEBUG))
app.logger.info('ASSETS_ROOT = ' + app.config['ASSETS_ROOT'])

if __name__ == "__main__":
    app.run()
