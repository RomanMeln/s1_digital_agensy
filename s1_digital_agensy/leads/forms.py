import re
from django import forms
from .models import ProjectStart


class ProjectStartForm(forms.ModelForm):
    contact = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': '+7 (___) ___-__-__', 'required': 'required'})
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Сообщение', 'required': 'required'})
    )

    agreement = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'required': 'required'})
    )

    class Meta:
        model = ProjectStart
        fields = ['name', 'contact', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-input', 'placeholder': 'Имя Фамилия', 'required': 'required'}),
        }

    def clean_name(self):
        """Проверка поля Имени"""
        name = self.cleaned_data.get('name')
        # Разрешает только буквы (русские и английские), пробелы и дефисы
        name_regex = r'^[a-zA-Zа-яА-ЯёЁ\s-]+$'

        if not re.match(name_regex, name):
            raise forms.ValidationError("Имя может содержать только буквы, пробелы и дефис.")

        if len(name.strip()) < 2:
            raise forms.ValidationError("Имя слишком короткое.")

        return name

    def clean_contact(self):
        """Проверка поля Телефона строго для РФ"""
        contact = self.cleaned_data.get('contact')

        # Регулярное выражение проверяет формат: +7 (XXX) XXX-XX-XX или +7(XXX)XXX-XX-XX
        phone_regex = r'^\+7\s?\(?\d{3}\)?\s?\d{3}-?\d{2}-?\d{2}$'

        # альтернативная проверка на случай, если пользователь введет просто 11 цифр подряд (например, 8999...)
        # принудительно очистит от символов и посчитает цифры
        digits = re.sub(r'\D', '', contact)

        # если строка не подходит под маску и количество цифр не равно 11 (или первая цифра не 7/8)
        if not (re.match(phone_regex, contact) or (len(digits) == 11 and digits[0] in ['7', '8'])):
            raise forms.ValidationError("Формат номера должен быть: +7 (999) 999-99-99")

        return contact
