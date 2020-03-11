from django.forms import ModelForm , TextInput
from .models import Stock


class StockForm(ModelForm):
	class Meta:
		model = Stock
		fields = ['code','date']
		widgets = {'code' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Companys code'}),
					'date' : TextInput(attrs={'class' : 'input', 'placeholder' : 'yyyy-mm-dd'})}