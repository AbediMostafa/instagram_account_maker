import time
from utils import *
import random
from helpers import *

from registrator import Registrator
import urllib.parse


# ==================================================
reg = Registrator()
starting_point_res = (reg.init_header().
                      set_starting_point_params().
                      send_request(starting_point_url))

print(f'starting point status code : {starting_point_res.status_code}')
write_to_file('responds/starting_point.json', starting_point_res.text)
time.sleep(random.randint(4, 6))
# ====================================================================
reg.get_number()
print('Phone numbers :', reg.phone_number, reg.phone_number_id)

phone_res = (reg.regenerate_header_timestamp().
             set_phone_params(reg.phone_number).
             send_request(phone_url))

print(f'phone status code : {phone_res.status_code}')
write_to_file('responds/phone.json', phone_res.text)
time.sleep(random.randint(10, 12))
# ====================================================================
reg.get_confirmation_code()

confirmation_code_res = (reg.regenerate_header_timestamp().
                         set_code_confirmation_params().
                         send_request(code_confirmation_url))

print(f'confirmation code status code : {confirmation_code_res.status_code}')
write_to_file('responds/confirmation_code.json', confirmation_code_res.text)
time.sleep(random.randint(10, 20))
# ====================================================================
password_res = (reg.regenerate_header_timestamp().
                set_password_params().
                send_request(password_url))

print(f'password status code : {password_res.status_code}')
write_to_file('responds/password.json', password_res.text)
time.sleep(random.randint(15, 20))
# ====================================================================
birthday_res = (reg.regenerate_header_timestamp().
                set_birthday_params().
                send_request(birthday_url))

print(f'birthday date: {reg.birthday_date}')
print(f'birthday timestamp: {reg.birthday_timestamp}')

print(f'birthday status code : {birthday_res.status_code}')
write_to_file('responds/birthday.json', birthday_res.text)
time.sleep(random.randint(12, 20))
# ====================================================================
name_res = (reg.regenerate_header_timestamp().
            set_name_params().
            send_request(name_url))

print(f'name status code : {name_res.status_code}')
write_to_file('responds/name.json', name_res.text)
time.sleep(random.randint(10, 15))
# ====================================================================
username_res = (reg.regenerate_header_timestamp().
                set_username_params("ertmadni_11").
                send_request(username_url))

print(f'username status code : {username_res.status_code}')
write_to_file('responds/username.json', username_res.text)
time.sleep(random.randint(10, 15))
# ====================================================================
final_res = (reg.regenerate_header_timestamp().
             set_final_params().
             send_request(final_url))

print(f'final status code : {final_res.status_code}')
write_to_file('responds/final.json', final_res.text)
# ====================================================================
final_res = (reg.regenerate_header_timestamp().
             set_final_params().
             send_request(final_url))

print(f'final status code : {final_res.status_code}')
write_to_file('responds/final.json', final_res.text)
# ====================================================================

# phone - confirmation - password - save_info - birthday - name - agree
