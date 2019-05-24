# Server Side Code

## Run a [webserver](https://en.wikipedia.org/wiki/Web_server)

## Requirements

```
pip install flask
```

## Running it

In the terminal:

```
$ export FLASK_APP=snakes_server.py
$ flask run
```

Then, visit http://localhost:5000.

## Key Remarks

```
@app.route('/')
```

This decorator defines what to do when a request is received at the '/' route(url), ie. `http://yoursite.com/` with no extension behind.
