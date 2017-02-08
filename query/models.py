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

class IntradePackageManager(models.Manager):
    def create_intrade_package(
        self, query_id, **packages_id):
        blackcat_id = packages_id.get('blackcat_id', None)
        chinese_id = packages_id.get('chinese_id', None)

        # Creating empty packages of blackcat and chinese first
        # try for duplicate key
        if blackcat_id:
            try:
                BlackcatPackage.objects.create(blackcat_id=blackcat_id)
            except:
                print('Creating empty blackcat package fails.')
        if chinese_id:
            try:
                ChinesePackage.objects.create(chinese_id=chinese_id)
            except:
                print('Creating empty chinese package fails.')

        intrade_package = self.create(
            query_id=query_id,
            blackcat_id=blackcat_id,
            chinese_id=chinese_id
        )
        return intrade_package


class IntradePackage(models.Model):
    query_id = models.CharField(max_length=100, primary_key=True)
    blackcat = models.ForeignKey('BlackcatPackage',
        on_delete=models.CASCADE, blank=True, default=None, null=True
    )
    chinese = models.ForeignKey('ChinesePackage',
        on_delete=models.CASCADE, blank=True, default=None, null=True
    )
    objects = IntradePackageManager()

    def __str__(self):
        return '{}: Blackcat = {} and Chinese = {}'.format(
            self.query_id, self.blackcat_id, self.chinese_id
        )