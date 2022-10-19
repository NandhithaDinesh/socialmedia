from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profilepictures",null=True)
    cover_pic=models.ImageField(upload_to="coverpics",null=True)

    dob=models.DateField(null=True)
    gender=models.CharField(max_length=20)
    bio=models.CharField(max_length=120)
    following=models.ManyToManyField(User,null=True,related_name="following")
class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=500)
    image=models.ImageField(upload_to="postimages",null=True)
    created_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)
    def __str__(self):
        return self.title
    def fetch_comments(self):
        return self.comments_set.all()

    def like_count(self):
        return self.liked_by.all().count()
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

