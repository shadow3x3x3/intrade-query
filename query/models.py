from django.db import models

class BlackcatPackage(models.Model):
    blakcat_id = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=255)
    login_date = models.DateTimeField('login date')
    establishment = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {} at {}'.format(
            self.blakcat_id, self.state, self.login_date
        )

class ChinesePackage(models.Model):
    chinese_id = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=255)
    login_date = models.DateTimeField('login date')
    location = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {} at {}'.format(
            self.chinese_id, self.state, self.login_date
        )
