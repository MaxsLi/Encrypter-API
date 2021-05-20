# [Encrypter-API](https://encrypter-api.herokuapp.com/)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/697abd5b80404d8e9e8acac31be528b1)](https://www.codacy.com/gh/MaxsLi/Encrypter-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MaxsLi/Encrypter-API&amp;utm_campaign=Badge_Grade)
![GitHub](https://img.shields.io/github/license/MaxsLi/Encrypter-API)

## Description

A REST API of Python script [Encrypter](https://github.com/MaxsLi/Encrypter).

This API is written using Python web framework [Flask](https://flask.palletsprojects.com/en/1.1.x/)
with [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

API URL: [https://encrypter-api.herokuapp.com/](https://encrypter-api.herokuapp.com/)

## Usage

### Route 1

Request:

* **Route**: https://encrypter-api.herokuapp.com/
* **Route**: https://encrypter-api.herokuapp.com/ping
* **Method**: GET

Response:

* Response body (JSON):

```json
{
  "status": "ok"
}
```

* Response status code: 200

### Route 2

Request:

* **Route**: https://encrypter-api.herokuapp.com/version
* **Method**: GET

Response:

* Response body (JSON):

```json
{
  "encrypter": "3.3",
  "api": "1.4"
}
```

* Response status code: 200

### Route 3

Request:

* **Route**: https://encrypter-api.herokuapp.com/encrypt
* **Method**: POST
* **Query Parameter**:

| **Field** | **Type** | **Description** |
| --------- | -------- | --------------- |
|   input   |  String  | The input to be encrypted |

Successful Response:

* Response body (JSON):

```json
{
  "result": "<encrypted_text>"
}
```

* Response status code: 200

Error Response:

* Response body (JSON):

```json
{
  "error": "<error_message>"
}
```

* Response status code: 400

### Route 4

Request:

* **Route**: https://encrypter-api.herokuapp.com/decrypt
* **Method**: POST
* **Query Parameter**:

| **Field** | **Type** | **Description** |
| --------- | -------- | --------------- |
|   input   |  String  | The input to be decrypted |

Successful Response:

* Response body (JSON):

```json
{
  "result": "<decrypted_text>"
}
```

* Response status code: 200

Error Response:

* Response body (JSON):

```json
{
  "error": "<error_message>"
}
```

* Response status code: 400
