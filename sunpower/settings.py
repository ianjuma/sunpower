from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URI = "postgresql://synod:@localhost:5432/sunpower"
BUNDLE_ERRORS = True

basedir = abspath(dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = join(basedir, 'db_repository')

try:
    from sunpower.settings_dev import *
except ImportError:
    pass