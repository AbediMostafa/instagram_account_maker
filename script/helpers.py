import random
import hashlib
import time
import uuid


def raise_exception(msg):
    print(msg)
    raise Exception(msg)


def one_three_chance():
    return random.randint(1, 3) == 3


def one_two_chance():
    return random.randint(1, 2) == 2


def generate_android_device_id():
    return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]


def generate_uuid(prefix: str = "", suffix: str = ""):
    return f"{prefix}{uuid.uuid4()}{suffix}"


def raw_client_time():
    return str(round(time.time(), 3))


def bandwidth_speed():
    return str(random.randint(2500000, 3000000) / 1000)


def write_to_file(file_name, content):
    f = open(file_name, "a", encoding="utf-8")
    f.write(str(content))
    f.close()
