import os
import json
import humanize
from flask import Flask, request, jsonify
from pwd import getpwuid


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_root():
    return jsonify(loop_dir('/'))

@app.route('/<path:path>', methods=['GET'])
def get_path(path):
    full_path = os.path.join('/', path)
    if os.path.isdir(full_path):
        return jsonify(loop_dir(full_path))
    elif os.path.isfile(full_path):
        with open(full_path, 'r') as f:
            return f.read()
    else:
        return 'Not found', 404

@app.route('/<path:path>', methods=['POST'])
def post_new_file(path): 
    full_path = os.path.join('/', path)
    if os.path.exists(full_path):
        return 'Conflict: file already exists', 409
    else:
        with open(full_path, 'w') as f:
            f.write(request.data.decode())
        return 'Created', 201, {'Location': full_path}

def loop_dir(full_path):
    output = []
    for x in os.listdir(full_path):
        x_path = os.path.join(full_path, x)
        if os.path.isfile(x_path):
            output.append({x: get_file_details(x_path)})
        else:
            output.append(x)
    return output

def get_file_details(filename):
    return {
        "Filetype": os.path.splitext(filename)[1],
        "Size": humanize.naturalsize(os.path.getsize(filename)),
        "Owner": getpwuid(os.stat(filename).st_uid).pw_name
    }


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python webserver.py /path/to/serve/from [port]')
        sys.exit(1)
    path = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    os.chdir(path)
    app.run(port=port)
