from django.db import models
from django.utils import timezone


class User(
    models.Model
):  # made this singular because one object does not contain multiple users.
    school_email = models.EmailField()
    password = models.CharField(
        max_length=60
    )  # with authentification does uconnect need to store this??
    first_name = models.CharField(max_length=50, default="First name")
    last_name = models.CharField(max_length=50, default="Last name")
    biography = models.CharField(
        max_length=1000,
        default="This user has thus far opted to maintain an air of mystery.",
    )  # check it out i added something please write me a good peer review

    def __str__(self):
        return self.school_email
    
    def get_messages(self): #get all messages sent to user
        return Message.objects.filter(recipient=self).order_by('-time_sent')


class UserPost(models.Model):  # made this sinfular
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    num_required = models.IntegerField()
    written_text = models.CharField(max_length=6000)
    recency_score = models.IntegerField()
    publish_datetime = models.DateTimeField()

    def __str__(self):
        return self.project_name


class Tag(
    models.Model
):  # Changed to just "Tag" since it seems we're using a single tag pool for posts/users
    name = models.CharField(max_length=15)
    #tags = ["Programming", "Art"] (this could be wrong)

class UserTagMapping(models.Model):
    # This is an Association Table; enables many-to-many between Users and Tags
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PostTagMapping(models.Model):
    # Mirrors UserTagMapping (but for posts)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Conversation(models.Model): 
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE, null=True) 
    seeker_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="seeker") #seeker reaching out 
    launcher_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="launcher") #launcher receiving message

    def __str__(self): #return the project name
        return f"{self.post_id.project_name}"
    
    def get_message(self): #get all messages in specific conversation
        return self.message_set.order_by('time_sent')


class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)  # Conversation to which it belongs
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="sent_msg")  # Who sent the message; I think null=True allows null so we don't need a default
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="received_msg")  # who received message
    subject = models.CharField(max_length=255, default="Enter subject line here") 
    time_sent = models.DateTimeField()
    message_content = models.TextField() #TextField for multiline, better for msg/comment type strings (?)
    
    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} at {self.time_sent}"

    def send_message(self, from_sender, to_recipient, message_content, post):
        conversation, created = Conversation.objects.get_or_create(
            post_id = post,
            seeker_id = from_sender,
            launcher_id = to_recipient
        )
        message = Message(
            conversation_id = conversation,
            sender = from_sender,
            recipient = to_recipient,
            subject = post.project_name, #subject line = project name of post
            time_sent = timezone.now(),
            message_content = message_content
        )
        message.save()
        return message