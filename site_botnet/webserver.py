import cherrypy
import os, time
import random, string


SESSION_KEY = '_cp_username'
COOKIE_NAME = "BOTID"
session_cookie = ""


def check_credentials(username, password):
    if username in ('admin', 'steve') and password == '123456':
        return None
    else:
        return "Incorrect username or password."


def require_login(username, session):
	if username == session:
		return "pass"
	else:
		return (username, session)
	
		
def enter_admin(func):
    def wrapper(*args, **kwargs):
        global session_cookie
        if session_cookie and COOKIE_NAME in cherrypy.request.cookie and session_cookie == cherrypy.request.cookie[COOKIE_NAME].value:
            return func(*args, **kwargs)                     
        else:
            raise cherrypy.HTTPRedirect("/login")
    return wrapper
    
    
def check_session(func):
	def wrapper(*args, **kwargs):
		global session_cookie
		if session_cookie and COOKIE_NAME in cherrypy.request.cookie and session_cookie == cherrypy.request.cookie[COOKIE_NAME].value:
			return 'You already logged! <a href ="./logout" > End session </a>'		
		else:
			return func(*args, **kwargs)	
	return wrapper
	
	
class Main(object):
	@cherrypy.expose
	@enter_admin
	def index(self):
		with open("index.php", 'r') as site:
			return (site.read())
	
	
	@cherrypy.expose
	@check_session
	def login(self, msg = "Login"):
		with open("login.php", 'r') as login:
			return (login.read())
	
	
	@cherrypy.expose
	def login_check(self,username,password, from_page):
		if username == "" or password == "":
			return 'Incorrect username or password. <a href="./login">Try again</a>'
		error_msg = check_credentials(username,password)
		if error_msg == "Incorrect username or password.":
			return 'Incorrect username or password. <a href="./login">Try again</a>'
			raise cherrypy.HTTPRedirect("/login")
		else:
			cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
			autentica = require_login(username, cherrypy.session[SESSION_KEY])
			if autentica == "pass":
				global session_cookie
				session_cookie = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(64))
				cherrypy.response.cookie[COOKIE_NAME] = session_cookie
				raise cherrypy.HTTPRedirect("/")
			else:
				return autentica
				
				
	@cherrypy.expose
	@enter_admin
	def logout(self):
		global session_cookie
		session_cookie = ""
		cherrypy.response.cookie[COOKIE_NAME] = session_cookie
		raise cherrypy.HTTPRedirect("/login")
		
	
def error_page_404(status, message, traceback, version):
	return "There is nothing here to see..."
	
		
if __name__ == '__main__':
    conf = {
        '/': {  
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'error_page.404': error_page_404
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(Main(), '/', conf)
