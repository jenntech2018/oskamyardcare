from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'autocomplete': 'given-name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control', 'autocomplete': 'email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'form-control', 'autocomplete': 'off' })
    )