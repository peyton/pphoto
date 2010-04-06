"""
A collection of reusable utilities
"""

import re
from django import template
from django.conf import settings

register = template.Library()

SAMPLE_LIST = [
'wineglasses',
'barstool',
'cuisinartcups',
'10pcpots',
'toaster',
'readingglasses',
'slippers',
'bathbody',
'hopediamond',
'gemstonebracelet',
'floralnecklace',
'tie',
'luggage',
'golfbasket',
'lamp',
'smithsonianpillow',
'smartbear',
'toycar',
'umbrella',
'lion',
'curtainrods',
'grilltools',
'drill',
'yellowvalve',
]

@register.simple_tag
def active(request, pattern):
    """
    Determines the active navigational link based on the current path.
    """
    if pattern == '/':
        pattern = '^/$' # Regexp compatible; prevent unintentional highlighting
    if re.search(pattern, request.path):
        return 'active'
    return ''

def parse_ttag(token, given_tags = None):
    tagname, bits = (lambda x: (x[0], x[1:]))(token.split_contents())
    tags = [bits[0]]
    possible_tags = given_tags or ['as', 'for', 'limit', 'exclude']
    for index, bit in enumerate(bits):
        if bit.strip() in possible_tags:
            tags.append(bits[index+1])
    return tags
    
@register.tag(name="make_sample_list")
def do_sample_list(parser, token):
    tags = parse_ttag(token, ['as'])
    return MakeSampleListNode(*tags)

class MakeSampleListNode(template.Node):
    def __init__(self, context_var='sample_list'):
        self.context_var = context_var
    
    def render(self, context):
        context[self.context_var] = SAMPLE_LIST
        return ''