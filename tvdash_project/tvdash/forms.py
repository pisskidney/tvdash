from django import forms


class SearchForm(forms.Form):
    """Form used to search the homepage"""
    query = forms.CharField()
