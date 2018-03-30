from django.db import models


class SourceType(models.Model):
    name = models.CharField(max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)


class Source(models.Model):
    name = models.CharField(max_length=60)
    source_type = models.ForeignKey(SourceType, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.__class__.__name__}(name={self.name},source_type={self.source_type.name})'


class BalanceEvent(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
