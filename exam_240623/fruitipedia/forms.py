from django import forms

from exam_240623.fruitipedia.models import Profile, Fruit


#  profiles -------------------------------------------------------

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'first_name', 'last_name', 'email', 'password'

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'first_name', 'last_name', 'image_url', 'age'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for name, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.delete()
        Fruit.objects.all().delete()
        return self.instance


#  fruits ----------------------------------------------------------

class AddFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['nutrition']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
