# [Encrypter-API](https://encrypter-api.onrender.com/)

[![API Testing](https://github.com/li-shangru/Encrypter-API/actions/workflows/api_testing.yml/badge.svg)](https://github.com/li-shangru/Encrypter-API/actions/workflows/api_testing.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/697abd5b80404d8e9e8acac31be528b1)](https://www.codacy.com/gh/li-shangru/Encrypter-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=li-shangru/Encrypter-API&amp;utm_campaign=Badge_Grade)
[![CodeQL](https://github.com/li-shangru/Encrypter-API/actions/workflows/codeql.yml/badge.svg)](https://github.com/li-shangru/Encrypter-API/actions/workflows/codeql.yml)
![GitHub](https://img.shields.io/github/license/li-shangru/Encrypter-API)

## Description

A REST API of Python script [Encrypter](https://github.com/li-shangru/Encrypter).

This API is written using Python web framework [Flask](https://flask.palletsprojects.com/en/1.1.x/)
with [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

API URL: [https://encrypter-api.onrender.com](https://encrypter-api.onrender.com)

## Usage

### Route 1

Request:

* **Route**: [/](https://encrypter-api.onrender.com/)
* **Route**: [/ping](https://encrypter-api.onrender.com/ping)
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

* **Route**: [/version](https://encrypter-api.onrender.com/version)
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

* **Route**: [/encrypt](https://encrypter-api.onrender.com/encrypt)
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

* **Route**: [/decrypt](https://encrypter-api.onrender.com/decrypt)
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
