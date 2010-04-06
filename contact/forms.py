from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from contact.models import Message

class MessageForm(ModelForm):
    
    def __init__(self, data=None, files=None, request=None, *args, **kwargs):
        if request is None:
            raise TypeError("Keyword argument 'request' must be supplied")
        super(MessageForm, self).__init__(data=data, files=files, *args, **kwargs)
        self.request = request
    
    error_css_class    = 'error'
    required_css_class = 'required'
    
    def get_message_dict(self):
        self.subject = "The Product Photo: %s, %s" % (self.cleaned_data['name'], self.cleaned_data['from_email'],)
        self.message = self.cleaned_data['message'] + "\n\n-%s" % self.cleaned_data['name']
        self.recipient_list = [a[1] for a in settings.ADMINS]
        self.from_email = self.cleaned_data['from_email']
        if not self.is_valid():
            raise ValueError(_("Message cannot be sent from invalid contact form"))
        message_dict = {}
        for message_part in ('from_email', 'message', 'recipient_list', 'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = callable(attr) and attr() or attr
        return message_dict
    
    def save(self, fail_silently=False):
        send_mail(fail_silently=fail_silently, **self.get_message_dict())
        super(MessageForm, self).save()
    
    class Meta:
        model = Message
        fields = ('name', 'from_email', 'message')
 