from flask import Flask, request, jsonify
from flask_caching import Cache
from time import sleep
import logging

app = Flask(__name__)

#caching
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 60
}
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/naman')
def hello_world():
    data = request.args.get('nom')
    sleep(60)
    res = get_square(nom=int(data))
    return jsonify({"result":res})

@cache.memoize(timeout=120)
def get_square(nom):
    print('fn hit')
    return nom*nom


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
