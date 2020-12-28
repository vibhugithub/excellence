from excellence import *
from datetime import datetime
import json
import re


@app.route('/register', methods=['POST'])
def register():
    """
    payload = {
    "username": "vibhuti",
    "password": "testing"
    }
    """
    if request.method == "POST":
        try:
            payload = json.loads(request.data) if type(request.data) != dict else request.data

            if 'username' not in payload.keys() or 'password' not in payload.keys():
                response = {'status': 400,
                            'message': "Request must contain username and password in post data",
                            'data': {}}
            username = payload.get('username', str(datetime.now().timestamp()).replace('.', ''))
            password = payload.get('password', str(datetime.now().timestamp()).replace('.', ''))

            db_connection = get_db_connection()
            cursor = db_connection.cursor()

            query = "INSERT INTO users (username, password) values('{}',password('{}'));"\
                .format(username, password)
            cursor.execute(query)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            response = {'status': 200,
                        'message': "Successfully Registered",
                        'data': {'username': username}}

        except mysql.connector.IntegrityError as err:
            response = {'status': 400,
                        'message': "Username already exists : " + str(username),
                        'data': {'exception': str(err)}}

        except Exception as excep:
            response = {'status': 400,
                        'message': "Something went wrong",
                        'data': {'exception': str(excep)}}

    else:
        response = {'status': 400,
                    'message': "Allowed methods: POST.\n, You are using " + str(request.method),
                    'data': {}}

    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    payload = {
    "username": "vibhuti",
    "password": "testing"
    }
    """
    if request.method == "GET" or request.method == "POST":
        try:
            payload = json.loads(request.data) if type(request.data) != dict else request.data

            if 'username' not in payload.keys() or 'password' not in payload.keys():
                response = {'status': 400,
                            'message': "Request must contain username and password in post data",
                            'data': {}}
            username = payload.get('username', "")
            password = payload.get('password', "")

            db_connection = get_db_connection()
            cursor = db_connection.cursor()

            query = "select id, username from users where username = '{}' and password = password('{}');"\
                .format(username, password)

            cursor.execute(query)
            users_obj = cursor.fetchall()
            db_connection.commit()
            cursor.close()
            db_connection.close()
            if len(users_obj) == 1 and users_obj[0][1] == username:
                user_id = users_obj[0][0]
                response = {'status': 200,
                            'message': "Successfully login",
                            'data': {
                                'id': str(user_id),
                                'username': str(username)
                            }}
            else:
                response = {'status': 400,
                            'message': "Login failed, Try again with correct username password",
                            'data': {
                                'username': str(username)
                            }}

        except Exception as excep:
            response = {'status': 400,
                        'message': "Something went wrong",
                        'data': {'exception': str(excep)}}

    else:
        response = {'status': 400,
                    'message': "Allowed methods: GET, POST.\n, You are using " + str(request.method),
                    'data': {}}

    return response


@app.route('/update_address', methods=['POST'])
def update_user_address():
    """
    1.) payload must contain username (mandatory field)
    2.) pincode must be a number
    3.) all other fields are of varchar type

    sample :
    {
    "username": "vibhuti",
    "street": "test",
    "pincode": "123520",
    "state": "haryana",
    "country": "India",
    "phone_no": "9876567899"
    }
    """
    if request.method == "POST":
        try:
            payload = json.loads(request.data) if type(request.data) != dict else request.data

            if 'username' not in payload.keys(): # Mandatory key to find user_id for address creation
                response = {'status': 400,
                            'message': "Request must contain username in post data",
                            'data': {}}

            # paload must contain atleast 1 value to create an address
            elif not ('street' in payload.keys() or 'pincode' in payload.keys() or 'country' in payload.keys()
                      or 'state' in payload.keys() or 'phone_no' in payload.keys()):
                response = {'status': 400,
                            'message': "Please provide data for address creation",
                            'data': {}}
            else:
                username = payload.get('username', "")
                if 'pincode' in payload.keys() and not (re.match("^[0-9]{6}$", str(payload.get('pincode')))):
                    raise Exception('Pincode should be a number of 6 digits')

                db_connection = get_db_connection()
                cursor = db_connection.cursor()

                query = "select id, username from users where username = '{}';".format(username)

                cursor.execute(query)
                users_obj = cursor.fetchall()

                if len(users_obj) == 1 and users_obj[0][1] == username:
                    user_id = users_obj[0][0]
                    query = "INSERT INTO users_address (user_id, street,pincode,country,state,phone_no) " \
                            "values({},'{}',{},'{}','{}','{}');".format(user_id, payload.get('street', 'null'),
                                                                        payload.get('pincode', "null"),
                                                                        payload.get('country', 'null'),
                                                                        payload.get('state', 'null'),
                                                                        payload.get('phone_no', "null"))

                    cursor.execute(query)
                    response = {'status': 200,
                                'message': "Address Successfully Added",
                                'data': {'username': username}}
                else:
                    response = {'status': 400,
                                'message': "No user exist with provided username",
                                'data': {
                                    'username': str(username)
                                }}

                db_connection.commit()
                cursor.close()
                db_connection.close()

        except mysql.connector.IntegrityError as err:
            response = {'status': 400,
                        'message': "Please provide proper values for all fields!!",
                        'data': {'exception': str(err)}}

        except Exception as excep:
            response = {'status': 400,
                        'message': "Something went wrong",
                        'data': {'exception': str(excep)}}

    else:
        response = {'status': 400,
                    'message': "Allowed methods: POST.\n, You are using " + str(request.method),
                    'data': {}}

    return response


if __name__ == '__main__':
    app.run(debug=False)
