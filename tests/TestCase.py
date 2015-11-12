import urllib2
from flask import Flask
from flask.ext.testing import LiveServerTestCase


class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask('app')
        app.config['TESTING'] = False
        app.config['LIVESERVER_PORT'] = 8000
        return app

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)