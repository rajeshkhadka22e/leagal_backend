from vercel_wsgi import handle_wsgi
from core.wsgi import application  # Replace 'myproject' with your actual project name

app = handle_wsgi(application)