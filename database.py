from django.db import models

class UserPost(models.Model): # made this sinfular
        author = models.ForeignKey(User, on_delete=models.CASCADE)
	project_name = models.CharField(max_length=30)
	num_required = models.IntegerField()
	written_text = models.CharField(max_length=800)
	recency_score = models.IntegerField()

class User(models.Model): # made this singular because one object does not contain multiple users.
	school_email = models.EmailField()
	# password. okay two issues here. 1- django doesn't offer a preset password type, so we need to either make a custom type or just use varchar and the internet is roasting people for doing that. 2- does uconnect need to store a user password if we're just using a third-party authenticator to log in? in that case, the app doesn't store passcode info.


class UserTagMapping(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
# userful fields include: DateTimeField (date and time), DateField, BooleanField, EmailField, FileField, FloatField, IntegerField, TimeField, TextField (large text field), UUIDField (for storing universally unique identifiers), ForeignKey
	tag_id = models.IntegerField()
	

class Inbox(models.Model):
	

# https://docs.djangoproject.com/en/5.1/ref/models/fields/#model-field-types
