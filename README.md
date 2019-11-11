# Easy forms in Django

### Load bootstrap4 with pip install

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

### Forms in Django
```python
from django import forms


# forms.Form class
class MovieForm(forms.Form):

    title_en = forms.CharField(
                    max_length=100,
                    label='English title',
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Enter english title',
                        }
                    )
                )

    open_date = forms.DateField(
                    widget=forms.DateInput(
                        attrs={
                            'type': 'date'
                        }
                    )
                )


# forms.ModelForm class
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', )
```

```django
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block body %}

  <!-- url_name defines linked url -->
  {% if request.resolver_match.url_name == 'create_modelform' %}
    <h1>Create</h1>
  {% else %}
    <h1>Update</h1>
  {% endif %}

  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='Submit' %}{% endbuttons %}
  </form>

{% endblock %}
```