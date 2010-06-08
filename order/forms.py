import itertools

from django.conf import settings
from django.core.mail import send_mail
from django import forms
from django.contrib.formtools.wizard import FormWizard
from django.contrib.localflavor.us.forms import USPhoneNumberField
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

ASSEMBLY_CHOICES = (
    ('N', 'No'),
    ('Y', 'Yes'),
)

ANGLE_CHOICES = (
    ('N', 'No preference'),
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

EFFECT_CHOICES = (
    ('N', 'No preference'),
    ('D', 'Drop shadow'),
    ('R', 'Reflection'),
    ('O', 'Outline'),
)

FOCUS_CHOICES = (
    ('N', 'No preference'),
    ('F', 'Full focus'),
    ('S', 'Selective focus'),
)

DELIVERY_CHOICES = (
    ('W', 'Web download (FTP)'),
    ('D', 'CD shipped overnight (additional charge)'),
)

RESOLUTION_CHOICES = (
    ('W', 'Web resolution (800x526 pixels)'),
    ('H', 'High resolution (5000x4000 pixels, additional charge)'),
)

class ProductInfoForm(forms.Form):
    error_css_class    = 'error'
    required_css_class = 'required'

    single_quantity      = forms.IntegerField(widget=forms.widgets.TextInput(attrs={'class':'short'}), 
        label=_('Single item'), initial=0, required=False, min_value=0,
        )
    small_group_quantity = forms.IntegerField(widget=forms.widgets.TextInput(attrs={'class':'short'}), 
        label=_('Small group'), initial=0, required=False, min_value=0,
        )
    large_group_quantity = forms.IntegerField(widget=forms.widgets.TextInput(attrs={'class':'short'}), 
        label=_('Large group'), initial=0, required=False, min_value=0, error_messages={
            'min_value': 'Please enter a number greater than 0.'
            }
        )
    assembly_required    = forms.BooleanField(label=_('Assembly required?'), initial='N',
        widget=forms.widgets.RadioSelect(choices=ASSEMBLY_CHOICES, attrs={'class':'radio'}))
    angle         = forms.BooleanField(label=_('Preferred shooting angle'), initial='N',
        widget=forms.widgets.RadioSelect(choices=ANGLE_CHOICES, attrs={'class':'radio'}))
    effects       = forms.BooleanField(label=_('Desired effects'), initial='N',
        widget=forms.widgets.RadioSelect(choices=EFFECT_CHOICES, attrs={'class':'radio'}))
    focus         = forms.BooleanField(label=_('Focus style'), initial='N',
        widget=forms.widgets.RadioSelect(choices=FOCUS_CHOICES, attrs={'class':'radio'}))

class ContactInfoForm(forms.Form):
    error_css_class    = 'error'
    required_css_class = 'required'
    
    name          = forms.CharField(max_length=70, error_messages={'required': 'Please enter your name.'})
    email    = forms.EmailField(max_length=320, error_messages={'required': 'Please enter your email address.',
        'invalid':'Please enter a valid email address.'},
        )
    phone         = USPhoneNumberField(label=_('Phone number'),
        error_messages={'required': 'Please enter your phone number.',
        'invalid': 'Please enter your phone number in the form XXX-XXX-XXXX.'}
        )
    company       = forms.CharField(max_length=70, required=False, label=_('Company (optional)'))
    # address       = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'smaller'}), label=_('Full address'),
    #     error_messages={'required': 'Please enter your full address, including Street, City, State, and ZIP Code.'}
    #     )
    
    # resolution    = forms.BooleanField(label=_('Image resolution'), initial='W',
    #     widget=forms.widgets.RadioSelect(choices=RESOLUTION_CHOICES, attrs={'class':'radio'}))
    deliver_via   = forms.BooleanField(label=_('Deliver via'), initial='W',
        widget=forms.widgets.RadioSelect(choices=DELIVERY_CHOICES, attrs={'class':'radio'}))
    # date          = forms.DateField(label=_('Preferred date (optional)'), required=False,
    #     error_messages={'invalid': 'Please enter a date in the form MM/DD/YYYY.'}
    #     )
    comments      = forms.CharField(widget=forms.widgets.Textarea(), required=False,
            label=_('Additional comments (optional)'),
        )

# class DeliveryInfoForm(forms.Form):
#     error_css_class    = 'error'
#     required_css_class = 'required'
#     
#     # resolution    = forms.BooleanField(label=_('Image resolution'), initial='W',
#     #     widget=forms.widgets.RadioSelect(choices=RESOLUTION_CHOICES, attrs={'class':'radio'}))
#     deliver_via   = forms.BooleanField(label=_('Deliver via'), initial='W',
#         widget=forms.widgets.RadioSelect(choices=DELIVERY_CHOICES, attrs={'class':'radio'}))
#     # date          = forms.DateField(label=_('Preferred date (optional)'), required=False,
#     #     error_messages={'invalid': 'Please enter a date in the form MM/DD/YYYY.'}
#     #     )
#     comments      = forms.CharField(widget=forms.widgets.Textarea(), required=False,
#             label=_('Additional comments (optional)'),
#         )

class OrderWizard(FormWizard):    
    def get_message_dict(self, form_list):
        form_data_list = [form.cleaned_data for form in form_list]
        self.form_data = {}
        for x in form_data_list:
            self.form_data.update(x)
        self.subject = 'Order: %s, %s' % (self.form_data['name'], self.form_data['email'])
        self.message = render_to_string('order/email_template.txt', {'form_data': self.form_data})
        self.recipient_list = [a[1] for a in settings.ADMINS]
        self.from_email = self.form_data['email']
        message_dict = {}
        for message_part in ('from_email', 'message', 'recipient_list', 'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = callable(attr) and attr() or attr
        return message_dict
    
    def get_template(self, step):
        return 'order/step%d.html' % step
    
    # def save(self, fail_silently=False):
    #     send_mail(fail_silently=fail_silently, **self.get_message_dict())
    #     super(OrderForm, self).save()
        
    def done(self, request, form_list, fail_silently=True):
        send_mail(fail_silently=fail_silently, **self.get_message_dict(form_list))
        success_url = reverse('order_form_sent')
        return HttpResponseRedirect(success_url)
        
 