from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(label='Product description', widget=forms.Textarea)
    price = forms.DecimalField(min_value=1, max_value=100000)
    quantity = forms.IntegerField(min_value=0, max_value=1000)
    # date_received = forms.DateTimeField(auto_now_add=True)
    has_additional_guarantee = forms.BooleanField()
    archived = forms.BooleanField()
