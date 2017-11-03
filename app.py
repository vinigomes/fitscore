# Copyright 2017 Softplan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
