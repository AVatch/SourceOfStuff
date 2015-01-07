from django.forms import ModelForm
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['contributors', 'upvotes', 'downvotes', 'last_accessed', 'last_modified']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['cover'].widget.attrs['class'] = 'form-control'
        self.fields['origin_story'].widget.attrs['class'] = 'form-control'
        self.fields['first_mentioned'].widget.attrs['class'] = 'form-control'
        self.fields['first_mentioned'].widget.attrs['id'] = 'datetimepicker1'
        self.fields['geographic_origin'].widget.attrs['class'] = 'form-control'
        self.fields['inventor'].widget.attrs['class'] = 'form-control'
