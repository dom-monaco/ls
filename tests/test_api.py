# You can run the tests using the following command (while server is running):
# pytest -v test_api.py

import pytest
import requests
import os

BASE_URL = "http://localhost:8000"

def test_get_root_endpoint():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200

def test_get_path_endpoint():
    cwd = os.getcwd()
    r1 = requests.get(f"{BASE_URL}/{cwd}/tests/test_dir/test1.txt")
    assert r1.status_code == 200
    assert "This program is amazing!" in r1.text
    r2 = requests.get(f"{BASE_URL}/{cwd}/tests/test_dir/test2.py")
    assert r2.status_code == 200
    assert "def function():" in r2.text

def test_post_newfile_endpoint():
    cwd = os.getcwd()
    file_content = "newfile for tests"
    pr = requests.post(f"{BASE_URL}/{cwd}/tests/newfilename.txt", data=file_content)
    assert pr.status_code == 201
    gr = requests.get(f"{BASE_URL}/{cwd}/tests/newfilename.txt")
    assert gr.status_code == 200
    assert file_content in gr.text
    os.remove(f"{cwd}/tests/newfilename.txt")
