# You can run the tests using the following command (while server is running):
# pytest -v test_api.py

import pytest
import requests
import os

BASE_URL = "http://localhost:8000"

def test_get_root_endpoint():
    req = requests.get(f"{BASE_URL}/")
    assert req.status_code == 200

def test_get_path_endpoint():
    cwd = os.getcwd()
    filepath = f"{BASE_URL}/{cwd}/tests/test_dir"
    req1 = requests.get(f"{filepath}/test1.txt")
    assert req1.status_code == 200
    assert "This program is amazing!" in req1.text
    req2 = requests.get(f"{filepath}/test2.py")
    assert req2.status_code == 200
    assert "def function():" in req2.text

def test_post_newfile_endpoint():
    cwd = os.getcwd()
    filepath = f"{cwd}/tests/newfilename.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
    file_content = "newfile for tests"

    preq = requests.post(f"{BASE_URL}/{filepath}", data=file_content)
    assert preq.status_code == 201
    greq = requests.get(f"{BASE_URL}/{filepath}")
    assert greq.status_code == 200
    assert file_content in greq.text
    os.remove(filepath)
