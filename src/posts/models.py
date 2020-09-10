from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=64)
    link = models.CharField(max_length=64)
    creation_date = models.DateTimeField(null=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(null=True, default=0)
    author_name = models.CharField(max_length=20, unique=True)

    def update_amount(self):
        self.amount_of_upvotes = self.amount_of_upvotes + 1
        self.save()

    def reset_votes(self):
        self.amount_of_upvotes = 0
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    author_name = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
