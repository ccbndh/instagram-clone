from django import template
import re

register = template.Library()


@register.simple_tag
def auto_add_link_hashtag(comment):
    res = ''
    for tag in comment.split():
        if tag.startswith("#"):
            # print(tag.strip("#"))
            res += '<a href="http://127.0.0.1:8000/search/?search=' + tag.strip("#") + '">#' + tag.strip("#") + '</a>'
        else:
            res += tag
        res += ' '
    return res