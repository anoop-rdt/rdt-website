from django import forms



class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'contactinput fullwidth pdgS10'}))
    contact_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'contactinput fullwidth pdgS10'}))
    contact_phone = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'contactinput fullwidth pdgS10'}))
    subject = forms.CharField(max_length=100, help_text='100 characters max.',widget=forms.TextInput(attrs={'class' : 'contactinput fullwidth pdgS10'}))
    content = forms.CharField(max_length=2000, help_text='2000 characters max.',required=True,widget=forms.TextInput(attrs={'class' : 'contacttext fullwidth'}))

