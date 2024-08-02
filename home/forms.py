from django import forms
from home.models import ContactMessage #, Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)


#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ('name', 'email', 'body')

class CommentForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

class SubscriptionForm(forms.Form):
    email = forms.EmailField()

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['sender_name', 'sender_email', 'sender_phone', 'sender_message']


