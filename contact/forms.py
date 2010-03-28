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
        # self.request = request
    
    # def get_message_dict(self):
    #     if not self.is_valid():
    #         raise ValueError(_("Message cannot be sent from invalid contact form"))
    #     message_dict = {}
    #     for messaeg_part in ('from_email', 'message', 'recipient_list', 'subject'):
    #         attr = getattr(self, message_part)
    #         message_dict[message_part] = callable(attr) and attr() or attr
    #     return message_dict
    # 
    # def save(self, fail_silently=False):
    #     send_mail(fail_silently=fail_silently, **self.get_message_dict())
    #     super(MessageForm, self).save(fail_silently=fail_silently)
    
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        
    # subject = "The Product Photo: %s" % name
    # recipient_list = [email for name, email in settings.ADMINS]
    # from_email = email
 