from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def get_descendants(self):
        descendants = set()
        subs = self.subcategories.all()
        for sub in subs:
            descendants.add(sub)
            descendants.update(sub.get_descendants())
        return descendants

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name