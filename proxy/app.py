import os
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)
API_URL = "http://users:3000"


@app.route('/hello', methods=['GET'])
def hello():
    return '<p>Hello world!</p>'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def proxy(path):
    app.logger.info(f'===== Forward request to {path} =====')
    resp = requests.request(
        method=request.method,
        url=f"{API_URL}/{path}",
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    response = jsonify(resp.json())
    response.status_code = resp.status_code

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PROXY_PORT'], debug=True)
