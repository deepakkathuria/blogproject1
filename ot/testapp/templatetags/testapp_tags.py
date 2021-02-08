from django import template
from testapp.models import Post
register=template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()



@register.inclusion_tag('testapp/latest.html')
def show_latest_posts(count=5):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
