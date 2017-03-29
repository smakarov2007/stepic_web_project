def app(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  start_response(status, headers)
  qs = environ['QUERY_STRING'].split("&")
  return [item+"\r\n" for item in qs]
