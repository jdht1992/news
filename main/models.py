from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=500,  null=True)
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=500, null=True)
    url = models.URLField(max_length=200)
    image = models.URLField(max_length=200, blank=True, null=True)
    published = models.DateField()
    content = models.TextField(max_length=500, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.author

