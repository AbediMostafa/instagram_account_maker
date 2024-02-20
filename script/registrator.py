import json
import random
import urllib.parse
from datetime import datetime
import requests

from utils import *
from helpers import *
from APIS.starting_point import *
from APIS.phone import *
from APIS.code_confirmation import *
from APIS.password import *
from APIS.birthday import *
from APIS.name import *
from APIS.username1 import *
from APIS.final import *


class Registrator:
    device_id = None
    family_device_id = None
    android_id = None
    header = None
    waterfall_id = None
    registration_flow_id = None
    headers_flow_id = None
    name = None
    birthday_timestamp = None
    birthday_date = None
    phone = None
    username = None
    phone_number = None
    phone_number_id = None
    confirmation_code = "0"
    data = {}

    def __init__(self):
        self.device_id = generate_uuid()
        self.family_device_id = generate_uuid()
        self.waterfall_id = generate_uuid()
        self.registration_flow_id = generate_uuid()
        self.headers_flow_id = generate_uuid()
        self.android_id = generate_android_device_id()
        self.header = headers
        self.params = None

    def init_header(self):
        self.header["X-Pigeon-Session-Id"] = generate_uuid('UFS-', '-0')
        self.header["X-Pigeon-Rawclienttime"] = raw_client_time()
        self.header["X-Ig-Bandwidth-Speed-Kbps"] = bandwidth_speed()
        self.header["X-Ig-Device-Id"] = self.device_id
        self.header["X-Ig-Family-Device-Id"] = self.family_device_id
        self.header["X-Ig-Android-Id"] = self.android_id

        return self

    def regenerate_header_timestamp(self):
        self.header["X-Pigeon-Rawclienttime"] = raw_client_time()
        return self

    def set_req_info_params(self, req_info_type):
        req_info = req_info_type
        req_info['device_id'] = self.android_id
        req_info['family_device_id'] = self.family_device_id
        req_info['registration_flow_id'] = self.registration_flow_id

        return req_info

    def set_params(self, param_type, req_info):
        self.params = param_type

        self.params["client_input_params"]["device_id"] = self.android_id

        self.params["server_params"]["device_id"] = self.android_id
        self.params["server_params"]["waterfall_id"] = self.waterfall_id
        self.params["server_params"]["family_device_id"] = self.family_device_id
        self.params["server_params"]["qe_device_id"] = self.device_id
        self.params["server_params"]["reg_info"] = json.dumps(req_info)

    def json_decode_data(self):
        self.data['params'] = json.dumps(self.params, separators=(',', ':'))
        self.data['bk_client_context'] = json.dumps(bk_client_context, separators=(',', ':'))
        self.data['bloks_versioning_id'] = bloks_versioning_id

    def set_starting_point_params(self):
        req_info = self.set_req_info_params(starting_reg_info)
        self.set_params(starting_params, req_info)
        self.params["client_input_params"]["family_device_id"] = self.family_device_id
        self.params["client_input_params"]["qe_device_id"] = self.device_id

        self.json_decode_data()

        return self

    def set_phone_params(self, phone):
        self.phone = phone
        req_info = self.set_req_info_params(phone_reg_info)
        self.set_params(phone_params, req_info)
        self.params["client_input_params"]["family_device_id"] = self.family_device_id
        self.params["client_input_params"]["phone"] = phone
        self.params["server_params"]["event_request_id"] = generate_uuid()
        self.json_decode_data()

        return self

    def set_code_confirmation_params(self):
        req_info = self.set_req_info_params(code_confirmation_reg_info)
        req_info['headers_flow_id'] = self.headers_flow_id
        self.set_params(code_confirmation_params, req_info)
        write_to_file('request/code_confirmation_req_info.json', req_info)

        self.params["client_input_params"]["code"] = self.confirmation_code
        self.params["server_params"]["event_request_id"] = generate_uuid()
        write_to_file('request/code_confirmation_params.json', self.params)

        self.json_decode_data()

        return self

    def set_password_params(self):
        req_info = self.set_req_info_params(password_reg_info)
        req_info['headers_flow_id'] = self.headers_flow_id
        write_to_file('request/password_req_info.json', req_info)

        self.set_params(password_params, req_info)
        del self.params["client_input_params"]["device_id"]

        self.params["server_params"]["event_request_id"] = generate_uuid()
        write_to_file('request/password_params.json', self.params)

        self.json_decode_data()

        return self

    def set_birthday_params(self):
        self.birthday_date = '02-03-1997'
        # self.birthday_date = random.choice(birthdays)
        tmstmp = datetime.timestamp(datetime.strptime(self.birthday_date, "%d-%m-%Y"))
        self.birthday_timestamp = 857297823
        # self.birthday_timestamp = str(tmstmp).replace('.0', '')

        req_info = self.set_req_info_params(birthday_reg_info)
        req_info['headers_flow_id'] = self.headers_flow_id
        write_to_file('request/birthday_req_info.json', req_info)

        self.set_params(birthday_params, req_info)
        del self.params["client_input_params"]["device_id"]
        self.params["client_input_params"]["birthday_timestamp"] = self.birthday_timestamp
        write_to_file('request/birthday_params.json', self.params)


        self.json_decode_data()

        return self

    def set_name_params(self):
        self.name = random.choice(names)
        print(f'name is : {self.name}')
        req_info = self.set_req_info_params(name_reg_info)
        req_info['headers_flow_id'] = self.headers_flow_id
        req_info['birthday'] = self.birthday_date
        write_to_file('request/name_req_info.json', req_info)

        self.set_params(name_params, req_info)

        del self.params["client_input_params"]["device_id"]
        self.params["client_input_params"]["name"] = self.name
        write_to_file('request/name_params.json', self.params)

        self.json_decode_data()

        return self

    def set_username_params(self, username):
        self.username = username
        req_info = self.set_req_info_params(username1_reg_info)
        req_info['headers_flow_id'] = self.headers_flow_id
        req_info['full_name'] = self.name
        req_info['birthday'] = self.birthday_date
        req_info['username_prefill'] = self.username
        write_to_file('request/username_req_info.json', req_info)

        self.set_params(usernam1_params, req_info)

        self.params["client_input_params"]["validation_text"] = username
        self.params["client_input_params"]["family_device_id"] = self.family_device_id
        self.params["client_input_params"]["qe_device_id"] = self.device_id
        write_to_file('request/username_params.json', self.params)

        self.json_decode_data()

        return self

    def set_final_params(self):
        req_info = self.set_req_info_params(final_reg_info)
        req_info['full_name'] = self.name
        req_info['birthday'] = self.birthday_date
        req_info['headers_flow_id'] = self.headers_flow_id
        req_info['username'] = self.username
        req_info['username_prefill'] = self.username
        write_to_file('request/final_req_info.json', req_info)

        self.set_params(final_params, req_info)
        write_to_file('request/final_params.json', self.params)

        self.json_decode_data()

        return self

    def send_request(self, url):
        data = urllib.parse.urlencode(self.data)
        res = requests.post(url, data=data, headers=self.header)

        return res

    def get_number(self):
        res = requests.get(sweden_phone_number_api)

        self.phone_number = '+' + res.json()['NUMBER']
        self.phone_number_id = res.json()['ID']

    def get_confirmation_code(self):
        self.confirmation_code = "0"
        counter = 0

        while self.confirmation_code == "0":
            counter += 1
            get_confirmation_url = f'https://api.numberland.ir/v2.php/?apikey=ed6375c3ba657177bc7d4a512fe3860d&method=checkstatus&id={self.phone_number_id}'
            res = requests.get(get_confirmation_url)
            code = res.json()['CODE']
            self.confirmation_code = code
            time.sleep(3)
            print(f'confirmation code for the {counter} time : {self.confirmation_code}')
            if counter == 40:
                break
