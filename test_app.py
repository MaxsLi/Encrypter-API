# -*- coding: utf-8 -*-

"""Test file for API `app.py`."""

import pytest

from app import app


@pytest.fixture
def api():
    app.config['TESTING'] = True
    with app.test_client() as api:
        yield api


def test_ping(api):
    response = api.get('/ping')
    assert response.status_code == 200
    assert response.json['status'] == "ok"


def test_version(api):
    response = api.get('/version')
    assert response.status_code == 200


def test_encrypt_method_error(api):
    response = api.get('/encrypt')
    assert response.status_code == 405


def test_encrypt_input_error(api):
    response = api.post('/encrypt', data=dict())
    assert response.status_code == 400


def test_encrypt(api):
    response = api.post('/encrypt', data=dict(input="hello"))
    assert response.status_code == 200


def test_decrypt_method_error(api):
    response = api.get('/decrypt')
    assert response.status_code == 405


def test_decrypt_input_error(api):
    response = api.post('/decrypt', data=dict())
    assert response.status_code == 400


def test_decrypt_cypher_error(api):
    response = api.post('/decrypt', data=dict(input="hello"))
    assert response.status_code == 400


def test_decrypt(api):
    text: str = "hello"
    response = api.post('/encrypt', data=dict(input=text))
    assert response.status_code == 200
    cypher: str = response.json['result']
    response = api.post('/decrypt', data=dict(input=cypher))
    assert response.status_code == 200
    assert response.json['result'] == text
