from django.db import models

# Create your models here.
    fields = ('id', 'content', 'publish_time', 'author_name', 'author_email', 'post_id')

    Class Comment(Models.Model):
        content = models.charfield()
        publish_time = models.datefield(publish_time)
        author_name = models.charfield(length = 50)
        author_email = models.charfield(length = 100)
        post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)