from django import forms
from .models import Purchase,User
from django.contrib.auth.forms import UserCreationForm
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Поиск...'}))

class PurchaseForm(forms.ModelForm):

    ApplicationStartDate = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.TextInput(attrs={'placeholder': 'дд/мм/гггг', 'class': 'datepicker'}),
        label="Дата начала заявки"
    )

    ApplicationEndDate = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.TextInput(attrs={'placeholder': 'дд/мм/гггг', 'class': 'datepicker'}),
        label="Дата окончания заявки"
    )

    PlacementDate = forms.DateField(
      input_formats=["%d/%m/%Y"],
        widget=forms.TextInput(attrs={'placeholder': 'дд/мм/гггг', 'class': 'datepicker'}),
        label="Дата размещения"
    )

    UpdateDate = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.TextInput(attrs={'placeholder': 'дд/мм/гггг', 'class': 'datepicker'}),
        label="Дата обновления"
    )

    AuctionDate = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.TextInput(attrs={'placeholder': 'дд/мм/гггг', 'class': 'datepicker'}),
        label="Дата аукциона"
    )
    class Meta:
        model = Purchase
        fields = '__all__'  # Или перечислите поля, которые хотите отображать в форме
    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)

        # Пройдемся по всем полям формы и установим required=False
        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = False
        
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Выберите CSV файл')


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, help_text="Обязательное поле.")

    class Meta:
        model = User
        fields = ('name', 'username', 'password1', 'password2')