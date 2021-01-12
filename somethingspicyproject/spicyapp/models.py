from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should be at least two characters'
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least two characters'
        if len(post_data['user_name']) < 5:
            errors['user_name'] = 'Username should be at least five characters'
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email/password!"
        
        if len(post_data['password']) < 8:
            errors['password'] = 'Password should be at least eight characters'
        
        if (post_data['password'] != post_data['confirm_password']):
            errors['confirm_password'] = "Password confirm didn't match"

        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) > 0:
            errors['email_password'] = "Email/password is incorrect. Please try again."
        return errors

    def login_validator(self, post_data):
        errors ={}
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) == 0:
            errors['email_password'] = "Email/password is incorrect. Please try again."
        else:
            if bcrypt.checkpw(
                post_data['password'].encode(),
                user_list[0].password.encode()
            ) != True:
                errors['email_password'] = "Email/password is incorrect. Please try again."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Videoone(models.Model):
    username = models.ForeignKey(User, related_name='username1', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_by1')
    video1 = models.CharField(max_length=255)

class Videotwo(models.Model):
    username = models.ForeignKey(User, related_name='username2', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_by2')
    video2 = models.CharField(max_length=255)

class Videothree(models.Model):
    username = models.ForeignKey(User, related_name='username3', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_by3')
    video3 = models.CharField(max_length=255)

class Comment(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='comment_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Suggestion(models.Model):
    member = models.ForeignKey(User, related_name='suggestions', on_delete=models.CASCADE)
    video_game = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    like = models.ManyToManyField(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
