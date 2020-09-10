from celery import shared_task
from posts.models import Post


@shared_task
def reset():
    # Method for zeroing amount_votes
    posts = Post.objects.all()
    for post in posts:
        post.reset_votes()
