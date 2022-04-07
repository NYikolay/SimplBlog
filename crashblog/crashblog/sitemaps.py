from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Category, Post


class CategorySiteMap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSiteMap(Sitemap):
    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.created_at
