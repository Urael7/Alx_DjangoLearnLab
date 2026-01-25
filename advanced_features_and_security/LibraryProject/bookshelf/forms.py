from django import forms


class BookSearchForm(forms.Form):
    q = forms.CharField(
        label="Search",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class ExampleForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=False)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=False)
