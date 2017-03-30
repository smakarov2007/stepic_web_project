def app(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  qs = environ['QUERY_STRING']
  return [bytes(i+'\n','utf-8') for i in qs.split('&')]
