from django import forms
from django.utils.safestring import mark_safe

CONFIDENCE_CHOICES = (
    (1, '1 (Not Sure)'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9 (Very Sure)'),
)

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """ Renders radio buttons horizontally instead of vertically
    """
    def render(self):
        """Renders radio buttons"""
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
