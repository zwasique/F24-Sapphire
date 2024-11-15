from django.db import models


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


class UserPost(models.Model):  # made this sinfular
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    num_required = models.IntegerField()
    written_text = models.CharField(max_length=6000)
    recency_score = models.IntegerField()
    publish_datetime = models.DateTimeField()

    def __str__(self):
        return self.author


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
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    seeker_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    conversation_id = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, null=True
    )  # Conversation to which it belongs
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )  # Who sent the message; I think null=True allows null so we don't need a default
    time_sent = models.DateTimeField()
    message_content = models.CharField(max_length=600)
