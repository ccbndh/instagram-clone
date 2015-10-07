from django import template
import re

register = template.Library()


@register.simple_tag
def auto_add_link_hashtag(comment):
    # import pdb;pdb.set_trace()
    return re.sub('^#(\w+)(.*)', r'<a href="http://statigr.am/tag/\1"></a>\2', comment)
