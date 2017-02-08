from django.db import models

class BlackcatPackage(models.Model):
    blackcat_id = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=255, null=True, blank=True, default=None)
    login_date = models.DateTimeField('login date', null=True, blank=True, default=None)
    establishment = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return '{}: {} at {}'.format(
            self.blackcat_id, self.state, self.login_date
        )

class ChinesePackage(models.Model):
    chinese_id = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=255, null=True, blank=True, default=None)
    login_date = models.DateTimeField('login date', null=True, blank=True, default=None)
    location = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return '{}: {} at {}'.format(
            self.chinese_id, self.state, self.login_date
        )

class IntradePackage(models.Model):
    query_id = models.CharField(max_length=100, primary_key=True)
    blackcat = models.ForeignKey('BlackcatPackage',
        on_delete=models.CASCADE, blank=True, default=None, null=True
    )
    chinese = models.ForeignKey('ChinesePackage',
        on_delete=models.CASCADE, blank=True, default=None, null=True
    )

    def __str__(self):
        return '{}: Blackcat = {} and Chinese = {}'.format(
            self.query_id, self.blackcat_id, self.chinese_id
        )