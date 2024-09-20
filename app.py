from flask import Flask, render_template, request, jsonify, url_for
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

clients = [
            { 'name': "MVA Client A", "link" : 'https://app.leadconduit.com/flows/661eeb850ebe9b2e4e22ca05/sources/66b2780076bac1b4195cb287/submit'}
            
            ]

API_KEY = "3a74fe14e6bd37d4838a237888315178"

ehb_api_url = "https://experthelping.dialerhosting.com/RffsxNwc/non_agent_api.php"

@app.route('/', methods=['GET', 'POST'])
def form():

    
    if request.method == 'POST':
        source = request.args.get('source')
        user = request.args.get('user')
        password = request.args.get('pass')
        list_id = request.args.get('list_id')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        address1 = request.args.get('address1')
        city = request.args.get('city')
        postal_code = request.args.get('postal_code')
        state = request.args.get('state')
        phone_number = request.args.get('phone_number')
        created_at = request.args.get('created_at')
        IP_address = request.args.get('IP_address')
        Jornaya_token = request.args.get('Jornaya_token')
        TrustedForm = request.args.get('TrustedForm')
        URL = request.args.get('URL')
        custom_fields = request.args.get('custom_fields')
        subID = request.args.get('subID')
        email = request.args.get('email')
        comments = request.args.get('comments')
        data_dict = {
            "source": source,
            "user": user,
            "password": password,
            "list_id": list_id,
            "first_name": first_name,
            "last_name": last_name,
            "address1": address1,
            "city": city,
            "postal_code": postal_code,
            "state": state,
            "phone_number": phone_number,
            "created_at": created_at,
            "IP_address": IP_address,
            "Jornaya_token": Jornaya_token,
            "TrustedForm": TrustedForm,
            "URL": URL,
            "custom_fields": custom_fields,
            "subID": subID,
            "email" : email
        }

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'api-version': '4.0'
        }
        data = {
            "phone": phone_number,
            "email": email
        }

        # Make the POST request
        # print(TrustedForm)
        # print(data_dict)
        # print(ehb_api_url)

        # print('----------------------______--------------------_______-----------------------------______--------------------_______-----------------------------')
        response_tf = requests.post(comments, json=data, headers=headers, auth=HTTPBasicAuth('API', API_KEY))

        full_url = f"{ehb_api_url}/?{requests.utils.quote('&'.join([f'{key}={value}' for key, value in data_dict.items()]))}"
        query_parameters = request.args.to_dict()  # Convert MultiDict to a regular dict

        # response_ehb_api = requests.get(full_url)
        response_ehb_api = requests.get(ehb_api_url, params=query_parameters)
        print(response_ehb_api.url)

        return jsonify({
        "trustedform_response": {
            "status_code": response_tf.status_code,
            "response": response_tf.json() if response_tf.status_code == 200 else response_tf.text
        },
        "ehb_api_response": {
            "status_code": response_ehb_api.status_code,
            "response": response_ehb_api.text
        }
    }), 200

    
    return jsonify({
        "status": "This is a post request endpoint",
    }), 200  # 400 Error

if __name__ == '__main__':
    app.run(debug=True)
