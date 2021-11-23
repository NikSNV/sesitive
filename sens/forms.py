from django import forms


class SensForm(forms.Form):
    number = forms.IntegerField(max_value=99, min_value=10, label='Загаданное число')
