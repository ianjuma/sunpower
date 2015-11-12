#!/usr/bin/env python
import os
from flask.ext.script import Manager

from sunpower import app
manager = Manager(app)
from sunpower import db
from sunpower.database import init_db


@manager.command
def run():
    """
    start sun-power rest API
    :return:
    """
    port = int(os.environ.get("PORT", 8000))
    db.create_all()
    init_db()
    app.run('127.0.0.1', port=port, debug=False, threaded=False,
            use_reloader=True)

if __name__ == "__main__":
    os.environ.setdefault("FLASK_SETTINGS_MODULE", "sunpower.settings")
    manager.run()
