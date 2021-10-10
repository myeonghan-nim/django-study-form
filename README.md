# Study: form

## django-bootstrap4

```bash
$ pip install django-bootstrap4
```

```python
INSTALLED_APPS = [
    'bootstrap4',
]
```

```django
{% extends 'base.html' %}
{% load bootstrap4 %}
```

## form and modelform

```python
from django import forms

from .models import Movie, Comment


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
```

```django
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
  {% if request.resolver_match.url_name == 'create_modelform' %}
    <h1>CREATE</h1>
  {% else %}
    <h1>UPDATE</h1>
  {% endif %}
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='Submit' %}{% endbuttons %}
  </form>
{% endblock %}
```
