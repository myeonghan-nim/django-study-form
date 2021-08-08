from django import forms

from .models import Movie, Comment


class MovieForm(forms.Form):
    title = forms.CharField(max_length=50)
    title_en = forms.CharField(
        max_length=100,
        label='English title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter english title',
            }
        )
    )
    audience = forms.IntegerField()
    open_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    genre = forms.CharField(max_length=20)
    watch_grade = forms.CharField(max_length=20)
    score = forms.FloatField()
    poster_url = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)


class MovieModelForm(forms.ModelForm):
    open_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
