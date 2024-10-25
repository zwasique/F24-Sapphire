from django.db import models

class UserPost(models.Model): # made this sinfular
        author = models.ForeignKey(User, on_delete=models.CASCADE)
	project_name = models.CharField(max_length=30)
	num_required = models.IntegerField()
	written_text = models.CharField(max_length=6000)
	recency_score = models.IntegerField()
	post_tags = models.ForeignKey(ProjectTagMapping, on_delete=models.CASCADE)
	publish_datetime = models.DateTimeField()




class User(models.Model): # made this singular because one object does not contain multiple users.
	school_email = models.EmailField()
	password = models.CharField(max_length=60) # with authentification does uconnect need to store this??
	user_tags = models.ForeignKey(UserTagMapping, on_delete=models.CASCADE)

class UserTagMapping(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tag_id = models.IntegerField()
	
class UserTags(models.Model):
	name = models.CharField(max_length=15)

class Inbox(models.Model):
	recipient_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)
	sender_id = models.IntegerField() # should this be mapped to user as well

class Messages(models.Model):
	message_id = models.IntegerField()
	time_sent = models.DateTimeField()
	message_content = models.CharField(max_length=600)
# useful fields include: DateTimeField (date and time), DateField, BooleanField, EmailField, FileField, FloatField, IntegerField, TimeField, TextField (large text field), UUIDField (for storing universally unique identifiers), ForeignKey
# https://docs.djangoproject.com/en/5.1/ref/models/fields/#model-field-types
