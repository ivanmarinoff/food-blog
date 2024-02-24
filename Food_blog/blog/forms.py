from django import forms

from .models import Profile, Blog


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture', 'email', 'age', 'password']
        exclude =['user']


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture', 'user']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = None
        exclude = ['first_name', 'last_name', 'profile_picture', 'email', 'age', 'password']

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.__set_disabled_fields()

        # def __set_disabled_fields(self):
        #     for _, field in self.fields.values():
        #         field.widget.attrs['disabled'] = 'disabled'
        #         field.required = False

        def __init__(self):
            self.instance = None

        def save(self, commit=True):
            if commit:
                Profile.objects.all().delete()
            return self.instance


class BlogBaseForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'utility', 'difficulty_level', 'image_url', 'summary']
        exclude = ['id']


class BlogCreateForm(BlogBaseForm):
    pass


class BlogEditForm(BlogBaseForm):
    pass


class BlogDeleteForm(BlogBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
