from django import forms
from broadcast.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write some post..',
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
