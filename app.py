from flask import Flask, abort, request
import service


app = Flask(__name__)


@app.route('/')
def index():
    return "Intellead Fitscore"


@app.route('/fitscore', methods=['POST'])
def get_fitscore():
    data = request.get_json()
    if data is None:
        abort(400)
    cargo = data['cargo']
    area = data['area']
    segmento = data['segmento']
    if (cargo is None) | (cargo == '') | (area is None) | (area == '') | (segmento is None) | (segmento == ''):
        abort(400)
    fit_score = service.get_fit_score(cargo, area, segmento)
    return fit_score


if __name__ == '__main__':
    app.run(host='0.0.0.0')
