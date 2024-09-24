from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    subs = models.ManyToManyField('self', blank=True, related_name='parent_categories', symmetrical=False)

    def __str__(self):
        return self.category_name

    def get_descendants(self):
        descendants = set()
        subs = self.subs.all()
        for sub in subs:
            descendants.add(sub)
            descendants.update(sub.get_descendants())
        return descendants
