import socket
from . import excepts

def _parsing_http(http):
    http = http.split('\n\n')
    
    body = http[1]
    headers = {}
    for header in http[0].split('\n')[1:]:
        header = header.split(':')
        headers[header[0]] = header[1]
    print(headers, body)
    return headers, body

def run_server(service, run_config, *service_args):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((run_config['host'], run_config['port']))
    print('Starting server: ' + run_config['host'], run_config['port'], sep=':')
    sock.listen(run_config['nodes_on_hold'])
    while True:
        client_socket, client_address = sock.accept()
        data = client_socket.recv(run_config['input_size']).decode('utf-8')
        http_headers, http_body = _parsing_http(data)
        if http_headers['X-Service'] == run_config['service']:
            response = service(http_body, *service_args)
            client_socket.send(response.encode('utf-8'))
        else:
            client_socket.send('505'.encode('utf-8'))

        client_socket.close()
    sock.close()