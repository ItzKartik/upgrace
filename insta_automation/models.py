from django.db import models


class used_by(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class left_ids(models.Model):
    link = models.ForeignKey(used_by, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)


class insta_ids(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
