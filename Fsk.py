import json
from flask import Flask, redirect, url_for, request,make_response,jsonify,render_template
from FskQuery import DetailQuery
app = Flask(__name__)


@app.route('/collect<login>', methods=['POST', 'GET'])
def collect(login):
    empty_dict = {}
    convert_quotes = login.replace("'", '"')
    data_dict = json.loads(convert_quotes)
    query = DetailQuery()
    query.insert(data_dict)
    format_dict = empty_dict.update(data_dict)
    return jsonify(empty_dict)


@app.route('/success<login>')
def success(login):
    return login


dict_data = {}  # hash password


@app.route('/create', methods=['POST', 'GET'])
def create():
    form_data = ["name", "phone_number", "location", "gmail"]
    if request.method == 'POST':
        for x in form_data:
            user = request.form[x]
            dict_data.update({x: user})
        return make_response(redirect(url_for('collect', login=dict_data)))


@app.route('/read_contact', methods=['POST'])
def read():
    if request.method == 'POST':
        user = request.form["integer"]
        query = DetailQuery()
        obj = query.all_data()
        data = query.read(user)
    return jsonify(obj, {user: data})


@app.route('/read_login', methods=['POST', 'GET'])
def read_example():
    form_list = ["user_login", "password"]
    if request.method == 'POST':
        for x in form_list:
            user = request.form[x]
            dict_data.update({x: user})


@app.route('/update<login>', methods=['GET', 'POST'])
def update(login):
    convert_quotes = login.replace("'", '"')
    data_dict = json.loads(convert_quotes)
    query = DetailQuery()
    res = query.update(data_dict)
    format_dict = dict_data.update(data_dict)
    return jsonify(res)


@app.route('/update_data', methods=['POST', 'GET'])
def update_data():
    try:
        empty_dict = {}
        form_data = ["integer_u", "name", "phone_number", "location", "gmail"]
        if request.method == 'POST':
            for x in form_data:
                user = request.form[x]
                empty_dict.update({x:user})
            return make_response(redirect(url_for('update', login=empty_dict)))

    except Exception as err:
        return 'err'

    # return empty_dict, make_response(redirect(url_for('update', login=[get_id,empty_dict])))


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        user = request.form["integer_"]
        result = DetailQuery()
        obj = result.delete(user)
        obj_all_data = result.all_data()
    return jsonify({'data': [user+' deleted', obj_all_data]})


if __name__ == '__main__':
    app.run()

# GET /login?alphabetic=saranyaG
# else:['user_login'],password=dict_data['password']
#     for x in form_data:
#         user = request.args.get(x)
#         dict_data.update({x: user})
#     return make_response(dict_data)
# data = json.dumps(name) data=json.load(name),dictt=dict_data
# {"ok": 'saranyaA','json':take_json,'name':name} take_json = request.form['user_login']
# import urllib.parseres = urllib.parse.parse_qs(name)
# y = json.dumps(name) return {'ID': data['user_login'], 'name': data['name']}
