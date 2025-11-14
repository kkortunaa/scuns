from django.db import models



class Profile(models.Model):
    prof = models.CharField(max_length=256)
    
    def __str__(self):
        return self.prof



class User(models.Model):
    surname = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    name2 = models.CharField(max_length=256)
    reg_num = models.IntegerField()
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    phone_num = models.IntegerField(null=False)
    email = models.EmailField(max_length=256)
    avg_score = models.IntegerField()
    city = models.CharField(max_length=256)
    participation_in_olympiads = models.IntegerField()
    avg_oge_score = models.IntegerField()
    avg_score_of_exam = models.IntegerField()
    
    is_on_main = models.BooleanField(default=False)