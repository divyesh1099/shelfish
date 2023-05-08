# Hosting Instructions

## Frontend Hosting Instructions
(Referred to Vercel App Deployment Documentation) - [Vercel App Deployment Documentation](https://vercel.com/guides/deploying-react-with-vercel)
1. First Connect your GitHub Account where the project repository is available. 
2. Now in the dashboard select your github respository containing the code
3. Now Press "Deploy" button present in the dashboard and your project will be deployed. 

[Check Frontend Deployment Here - Shelfish_Frontend](https://shelfish-frontend.vercel.app/index.html)

## Backend Hosting Instructions 
(Refered to PythonAnywhere Documentation) - [PythonAnywhere Documentation](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
1. Upload Project to PythonAnywhere 
2. Create a virtualenv and install Django and any other requirements
3. Setting up your Web app and WSGI file by uncommenting the following code in the provided wsgi file: 
 ```
 # +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
 ```
4. Setup database by running the following command
```
./manage.py migrate
```
5. Now just restart the server using the "Restrat Web App" button provided on the dashboard and then it's done. 

[Check Backend Deployment Here - Shelfish_Backend](https://motidivya.pythonanywhere.com/booksapi/)