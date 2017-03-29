def app(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  body = environ['QUERY_STRING'].split("&")
  start_response(status, headers)
  return ['%s=%<br>' % (k, body[k][0] for k in body)]
