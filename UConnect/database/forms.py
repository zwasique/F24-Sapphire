from django import forms
from django.forms import ModelForm, Form

from .models import Tag, User, UserPost


class PostForm(ModelForm):
    project_name = forms.CharField(label="Project Name", max_length=50, help_text="Focus on what the project does")
    num_required = forms.IntegerField(
        label="Desired Number of Seekers", min_value=1, max_value=15, help_text="No more than 15")
    project_length = forms.IntegerField(
        label="Expected Project Length", min_value=0, max_value=24, help_text="Estimated length of project in months")
    # project tags, seeking tags (guys i'm inclined to just have one field for these.)
    post_body = forms.CharField(
        label="Project Description", max_length=4096, help_text="Visit the Home Page if you need an example",
        widget=forms.Textarea)
    tags = forms.ModelMultipleChoiceField(label="Select up to 6 tags:", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = UserPost
        fields = ['project_name', 'num_required', 'project_length', 'post_body', 'tags'] # TODO: Currently missing Author, recency score

# class for making a user's profile; the forms should get the user's first and last name as well as biography
class ProfileForm(ModelForm):
    school_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label="First name", max_length=50)
    last_name = forms.CharField(label="Last name", max_length=50)
    biography = forms.CharField(label="Biography", widget=forms.Textarea)
    tags = forms.ModelMultipleChoiceField(label="Select up to 6 tags.", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    #to do: implement tag limit
    class Meta:
        model = User
        fields = ['school_email', 'password', 'first_name', 'last_name', 'biography', 'tags']


class AccountForm(ModelForm):
    biography = forms.CharField(label="Biography", widget=forms.Textarea, required=False)
    tags = forms.ModelMultipleChoiceField(label="Select up to 6 tags.", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    #to do: implement tag limit
    class Meta:
        model = User
        fields = ['biography', 'tags']


class FilterForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(label="Filter by tags:", queryset = Tag.objects.all(), required=False)
    keywords = forms.CharField(label="Filter by text:", required=False)

    class Meta:
        model = Tag
        fields = ['tags', 'keywords']