import os
from sunpower import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run('127.0.0.1', port=port, debug=False, threaded=False,
            use_reloader=True)
    # app.run(port=8000, debug=True, host='0.0.0.0')
    # this can be omitted if using gevent wrapped around gunicorn
