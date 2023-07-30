import json
from server import server
from operations import all_operations
from contextlib import ExitStack
request_body = """{
  "operation": "add",
  "data": {
    "classes": null,
    "name": "Andrew",
    "surname": "Cuznecov",
    "age": 15,
    "email": "andrew15@gmail.com",
    "password": "42241416"
  }
}"""
def parse_config(config_file_name):
    with open(config_file_name, 'r') as c:
        config = json.load(c)
    return config

def profileServiceHandler(request_body, db_config):
    request_body = json.loads(request_body)
    data = request_body['data']
    operation = request_body['operation']
    if operation in all_operations:
        response = all_operations[operation](data, db_config)
    else:
        response = 'HTTP/1.1 SERVICE_ERROR: No such operation'
    return response

def main():
    print(profileServiceHandler(request_body, parse_config('configs/db_config.json')))
    #server.run_server(profileServiceHandler, parse_config('configs/server_config.json'), 
    #                  parse_config('configs/db_config.json'))


if __name__ == '__main__':
    main()
