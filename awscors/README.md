## Django rest framework

This is the work flow for create your first viewserializer

Starting with the project:

- python3 -m venv [name of you virtual enviroment]

- To activate the venv you can click f1 if you're using vscode this would guide to a couple of options that of differents python enviroments, he usually would recommend you to use one, so choose that one. If maybe vscode is not recommend you nothing about it, you can start the project by doing this:

- source [name of you venv]/bin/activate
- to deactivate it would be -> deactivate

Then you go with installing the necessary librarys and frameworks.

- pip install django
- pip install djangorestframework
- pip install mysql-connector-python
- pip install mysqlclient
- pip PyMySQL

- django-admin startproject [name of you project] . (the dot is to create the file inside of the folder that you currently have, if you don't use the dot, django will create the project insidie of antoher folder that he would create)

- python manage.py startapp [name of you app]

## Than you need to apply the new app to the settings of the project

You go first to settigns:

- settings > INSTALLED_APPS > add 'rest_framework' at the end and add after that '[the name of your app]' as well.

## IF YOU NEED TO CHANGE YOU DATA BASE DO THIS, IF NOT PASS TO NEXT STEP

- settings > data bases > this is the structure:

DATABASES = {
'default': {  
 'ENGINE': 'django.db.backends.[name of your DB provider]',
'NAME': '[name of your schema]',
'USER':'[name of you user (usually is root)]',
'PASSWORD':'[password of you db]',
'HOST':'[name or numbers of you host (usully is 127.0.0.1)]',
'PORT':'[name of you port (usually is 3306)]'
}
}

## Than you make migrations and migrate

## IMPORTANT TO UNDERSTAND

You use makemigrations to record model changes, and then migrate to apply those changes to the database. For instance, if you add a new field email to a User model, you’d run makemigrations to create the migration file, and then migrate to actually add the new column to the User table in your database.

- python manage.py makemigrations
- python manage.py migrate

If you already create models in your app

- python manage.py makemigrations [name of your app]
- python manage.py migrate

## Add the models to the addmin section

go to the admin of your app

- import the models
- admin.site.register([name of your model])

## Now, you need to convert your models into serializers , in order to do that

- In your app you need to create a seralizer.py file
- from rest_framework import serializer (that's literally how you need to imported)
- Import your models and write this code:

class userSerializers(serializers.ModelSerializer):
class Meta:
model = user
fields = "**all**"

Than we need to create the view for the serilizers can be manage (the htm view)

- In your app you go to to the view file
- Than from rest_framework import viewsets, permissions (this is the code as well that you need to placed)
- Your import you models and the serializer that you just create and add this code to create the view

class userViewserializer(viewsets.ModelViewSet):
queryset = user.objects.all()
permission_classes = [permissions.AllowAny]
serializer_class = userSerializers

Than we need to create the url in where we can access to this view set (html) with our serializer

- In your app you need to create a url file
- Import your viewsets
- Than import this, from rest_framework import routers
- Don't forget to import path and include from django.urls
- Now add this code:

router = routers.DefaultRouter()
router.register(r'user', userViewserializer)

urlpatterns = [
path('', include(router.urls))
]

Than you need to add that url file to the general urls of the project

like this: path('user/', include('awsapi.urls'))

And than you can run your project
