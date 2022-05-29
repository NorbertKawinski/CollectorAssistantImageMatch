import json

import ca_config
from flask import Flask, render_template, request, jsonify

import ca_elastic_db

app = Flask(__name__)


def start_server():
    app.run(host=ca_config.server_host, port=ca_config.server_port, debug=ca_config.server_debug)


@app.route('/test_caim_form')
def index():
    return render_template('test_caim.html')


@app.route('/upload', methods=["POST"])
def upload():
    img_id: str = request.form["img_id"]
    img_meta: dict = json.loads(request.form["metadata"])
    img_bytes: bytes = request.files["file"].read()
    ca_elastic_db.add_image(img_id, img_meta, img_bytes)
    return "OK"


# It might be weird, but search is "POST" request.
# Not all web servers support "GET" requests with body, so this is a bit of a workaround.
@app.route('/search', methods=["POST"])
def search():
    img_bytes: bytes = request.files["file"].read()
    result = ca_elastic_db.search_image(img_bytes)
    return jsonify(result)


@app.route('/delete', methods=["POST"])
def delete():
    img_id = request.form['img_id']
    ca_elastic_db.delete_image(img_id)
    return "OK"
