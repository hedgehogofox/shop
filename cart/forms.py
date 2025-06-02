from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=100, initial=1, label=False)
