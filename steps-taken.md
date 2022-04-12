## 0. Architecture steps
0. init repo and install pipenv
1. use pipenv to create venv
2. install django https://docs.djangoproject.com/en/4.0/topics/install/
3. create project with `django-admin startproject capsaicin_events` https://docs.djangoproject.com/en/4.0/intro/tutorial01/
4. start the server to tests if it works `./manage.py runserver`
5. create the api folder with `./manage.py startapp api`
6. install DRF to allow us to create a REST api with https://www.django-rest-framework.org/#installation
7. configure paths and installed applications.
  - Issue: encoutered error "ModuleNotFoundError: No module named 'rest_framework'"
  - Solution: found that i'm using the wrong command to install packages. Should have used `pip3` instead of `pip` https://stackoverflow.com/questions/33308781/django-rest-framework-no-module-named-rest-framework
8. create super user so that i can log in to the django backend. https://docs.djangoproject.com/en/4.0/ref/django-admin/#django-admin-createsuperuser
9. start the server to tests if the admin login works `./manage.py runserver` 
10. go to localhost:8000/admin/ and log in.
11. Add django rest framework with the user model, view and serialzer.
12. Add authentication and registration view to make sure only authenticated users can get data.
---

## 1. Event creation
1. Create event model like created in the ERD 
2. Create serializer according to the drf docs https://www.django-rest-framework.org/tutorial/quickstart/ 
3. Create view according to the drf docs https://www.django-rest-framework.org/tutorial/quickstart/ 

