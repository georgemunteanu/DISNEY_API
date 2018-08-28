#------------  Tap into required namespaces 
import os


#--------------- Define 4 HTTP request elements (protocol, url, port, params)
HTTP_PROTOCOL = "http://"
BASE_URL = "localhost"
PORT = ":9000"
SIGNUP_URL = "/users/signup"
GET_BLOG_URL = "/blog/"
POST_NEW_BLOG_URL = GET_BLOG_URL + "new"
LOGIN_URL = "/users/login" 
PARAM_FILE = os.path.join(os.path.dirname(__file__), 'payloads.json')
