from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.BigIntegerField(primary_key=True) # unique id to identify the post
    author_id = models.BigIntegerField(db_index=True) # author id to identify the post author
    parent_id = models.BigIntegerField(null=False) # to identify the parent post. can be used for creating table for parent post series.
    title = models.CharField(max_length=200) # post title
    meta_title = models.CharField(max_length=100) # for SEO (search engine optimization)
    slug = models.SlugField(max_length=50, unique=True) # post slug to form the URL
    summary = models.TextField(max_length=100) # key highlights
    published = models.SmallIntegerField() # used to identify whether post is publicly available
    createdAt = models.DateTimeField("Create At") # timestamps date and time of post creation
    updatedAt = models.DateTimeField("Update At") # timestamps date and time of update
    publishedAt = models.DateTimeField("Published At") # Date and time of publishing
    content = models.TextField() # stores the post content


class Post_Meta(models.Model):
    # unique id to identify the post meta
    meta_id = models.BigIntegerField(null=False, primary_key=True)
    # post to identify parent post
    post_id = models.BigIntegerField(null=False, unique=True)
    # key identifying the meta
    key = models.CharField(max_length=50, null=False, unique=True)
    content = models.TextField(default=True, null=False)


class Post_Comment(models.Model):
    # uniquely identifies post comment
    post_comment_id = models.BigIntegerField(primary_key=True, null=False)

    # post id to identify the parent post
    post_id = models.BigIntegerField(null=False)
    # parent id to identify the parent comment
    parentId = models.BigIntegerField(null=False)
    # comment title
    title = models.CharField(max_length=100)
    # published to identify whether the comment is publicly available
    published = models.SmallIntegerField(max_length=1, null=False)
    # createdAt to store the date and time at which comment is submitted
    createdAt = models.DateTimeField("Created At")
    # publishedAt to store the date and time at which comment is published
    publishedAt = models.DateTimeField("Published At")
    # actual comment
    comment = models.TextField()


class Category(models.Model):
    # to identify the category
    category_id = models.BigIntegerField(primary_key=True, null=False)
    # to identify the parent category
    parentId = models.BigIntegerField(null=False)
    # category title
    title = models.CharField(max_length=50, null=False)
    # meta title
    meta_title = models.CharField(max_length=50, null=True)
    # slug to form the URL
    slug = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False, default=True)


class Post_Category(models.Model):
    # postId to identify the post
    postId = models.BigIntegerField(primary_key=True, null=False, db_index=True)
    # category id to identify the category
    categoryId = models.BigIntegerField(null=False, db_index=True)


