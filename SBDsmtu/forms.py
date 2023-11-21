from django import forms
from .models import Purchase,User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
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

class RussianUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, help_text="Обязательное поле.")

    class Meta:
        model = User
   
        fields = ('name', 'username', 'password1', 'password2')
        # Переопределение текста для подсказок и сообщений об ошибках
        help_texts = {
            'username': 'Введите уникальное имя пользователя.',
            'password1': 'Введите пароль. Длина пароля не менее 8 символов.',
            'password2': 'Повторите введенный пароль для подтверждения.',
        }
        error_messages = {
            'username': {
                'unique': 'Пользователь с таким именем уже существует.',
            },
            
        }
     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['username'].label = 'Логин'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтвердите пароль'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Переопределение сообщений об ошибках для требований к паролю
        if len(password1) < 8:
            raise ValidationError('Пароль должен содержать как минимум 8 символов.')
        if password1.isdigit():
            raise ValidationError('Пароль не может состоять только из цифр.')

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Проверка на совпадение паролей
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают.')

        return password2