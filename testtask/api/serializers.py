from ctypes import c_ulong

from django.conf import settings


def utf8len(s):
    len_string = len(s.encode('utf-8'))
    # return str(c_ulong(len_string))
    return str(len_string)


def get_keys():
    return get_data()[2::4]


def get_data():
    with open(settings.BASE_DIR / r'api/files/data.bin', 'rb') as f:
        data = f.read().decode().split('|')
    return data


def save_data(data):
    with open(settings.BASE_DIR / r'api/files/data.bin', 'wb') as f:
        data = '|'.join(data).encode()
        f.write(data)


def validated_data(*args):
    if all(isinstance(s, str) for s in args):
        return True
    return False


def post_data(key, value):
    data = get_data()
    key_size = utf8len(key)
    value_size = utf8len(value)
    data.extend([key_size, value_size, key, value])
    save_data(data)


def get_index_key(key, data):
    index_key = 2
    while index_key < len(data):
        if data[index_key] == key:
            return index_key
        index_key += 4
    return -1


def put_value(key, value):
    data = get_data()
    index_key = get_index_key(key, data)
    if index_key < 0:
        raise KeyError('Invalid key')
    data[index_key + 1] = value
    save_data(data)


def delete_data(key):
    data = get_data()
    index_key = get_index_key(key, data)
    if index_key < 0:
        raise KeyError('Invalid key')
    del data[index_key - 2: index_key + 2]
    save_data(data)
