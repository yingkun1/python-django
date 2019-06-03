from django.db import models

class FrontUser(models.Model):
    username =models.CharField(max_length=200)

class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name="extension")
    def __str__(self):
        return ("UserExtension school:%s,user:%s"%(self.school,self.user_id))
