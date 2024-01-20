# ls
Python flask app that functions like the ls cmd

## Parameters of api
```
GET / -> list contents of root directory
GET /bar -> list contents of /bar/ directory
GET /foo1.txt -> contents of file foo1.txt
GET /bar/bar1 -> contents of file bar/bar1
POST /new_file.txt -> create a new file /new_file.txt
```
Files in directories will include name, type, size, and owner information.
Assumes all file content will fit in a JSON blob and still be readable.

## Usage
### cli
Adjust path to python as needed. (eg python3 instead of python)
```
pip install -r requirements.txt
python webserver.py <path> [port]
```
path is the desired working directory for the application.
port is optional and defaults to 8000.


### Testing
From dir of repo.
```
pytest -v tests/test_api.py
```
