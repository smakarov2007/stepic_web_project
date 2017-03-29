def app(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  qs = parse_qs(environ['QUERY_STRING'])
  start_response(status, headers)
  return ['%s=%<br>' % (k, qs[k][0] for k in qs)]
