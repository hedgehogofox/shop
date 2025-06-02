from django import forms
from .models import Product
from django.db.models import Max, Min

class PriceRangeForm(forms.Form):
    price_min = forms.IntegerField(required=False, label="От")
    price_max = forms.IntegerField(required=False, label="До")

class MakerFilterForm(forms.Form):
    all_makers = forms.BooleanField(required=False, label="Все производители")
    makers = forms.MultipleChoiceField(
        choices=[],  # Will be populated in the view
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=""
    )

    def __init__(self, products, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['makers'].choices = []
        for m in products.values('product__maker').distinct():
            if not (f"{m['product__maker']}",f"{m['product__maker']}") in self.fields['makers'].choices:
                self.fields['makers'].choices.append((f"{m['product__maker']}",f"{m['product__maker']}"))
        
        
class ColorFilterForm(forms.Form):
    all_colors = forms.BooleanField(required=False, label="Все цвета")
    colors = forms.MultipleChoiceField(
        choices=[],  # Will be populated in the view
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=""
    )

    def __init__(self, products, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['colors'].choices = []
        for m in products.values('product__color').distinct():
            if not (f"{m['product__color']}",f"{m['product__color']}") in self.fields['colors'].choices:
                self.fields['colors'].choices.append((f"{m['product__color']}",f"{m['product__color']}"))

class MaterialFilterForm(forms.Form):
    all_materials = forms.BooleanField(required=False, label="Все цвета")
    materials = forms.MultipleChoiceField(
        choices=[],  # Will be populated in the view
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=""
    )

    def __init__(self, products, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['materials'].choices = []
        for m in products.values('product__material').distinct():
            if not (f"{m['product__material']}",f"{m['product__material']}") in self.fields['materials'].choices:
                self.fields['materials'].choices.append((f"{m['product__material']}",f"{m['product__material']}"))
