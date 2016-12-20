from django.db import models

class BlackcatPackage(models.Model):
    query_id = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=255)
    login_date = models.DateTimeField('login date')
    establishment = models.CharField(max_length=255)

    def __str__(self):
        return '{} at {}'.format(self.state, self.login_date)