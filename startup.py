from post_app.models import Posts, Comments
post1 = Posts.objects.create(title="This is my first post!",
                             post_author="Tiffany", body="I don't know what to say.")
comment1 = Comments.objects.create(
    text="I knew you could do it!", comment_author="Jordon", post=post1)
post2 = Posts.objects.create(
    title="This is my second post.", post_author="Umar", body="I'm the best instructor.")
comment2 = Comments.objects.create(
    text="Yay!", comment_author="Gmo", post=post2)
