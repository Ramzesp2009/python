from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator


@deconstructible
class UkraineValidator:
    ALLOWED_CHARS = 'абвгдежзиклмнопрстуфхцчшщьюяєіїґАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЮЯЄІЇҐ0123456789- '
    code = 'ukraine'

    def __init__(self, message=None):
        self.message = message if message else 'Недопустимий символ'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise forms.ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):

    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label='Категорія не вибрана',
                                 label='Категорія')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     empty_label='Неодружена',
                                     required=False, label='Чоловік'
                                     )

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Довжина перевищує 50 символів")

        return title




