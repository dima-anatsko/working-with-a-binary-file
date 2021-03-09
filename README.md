#### It's Django application for working with a binary file

API available only to authorized users.  

Example HTTP GET:

```http request
GET /api/keys/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Token c3b1e9375936198bd3186ffb6676429a22a26036
```

Example HTTP GET to search for a substring:

```http request
GET /api/keys/?q=value HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Token c3b1e9375936198bd3186ffb6676429a22a26036
```

The POST, PUT and DELETE methods are only available for the admins group.  
Example HTTP POST:

```http request
POST /api/keys/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Token c3b1e9375936198bd3186ffb6676429a22a26036
Content-Type: application/json
Content-Length: 43

{"data": {"key": "key8","value": "value8"}}
```

PUT and DELETE queries are created in the same way.

