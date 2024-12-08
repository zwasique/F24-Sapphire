from django import forms
from django.forms import ModelForm, Form

from .models import Tag, User, UserPost


class PostForm(ModelForm):
    project_name = forms.CharField(label="Project Name: ", max_length=50, help_text="Focus on what the project does")
    num_required = forms.IntegerField(
        label="Desired Number of Seekers: ", min_value=1, max_value=15, help_text="No more than 15")
    project_length = forms.IntegerField(
        label="Expected Project Length(Months)", min_value=0, max_value=24, help_text="Estimated length of project in months") #i added it to say months in the label because it does not show up in help text? idk how that works -Tyger
    # project tags, seeking tags (guys i'm inclined to just have one field for these.)
    post_body = forms.CharField(
        label="Project Description: ", max_length=4096, help_text="Visit the Home Page if you need an example",
        widget=forms.Textarea)
    
    #okay i split the tags here so that it shows up as a drop down again, and set the first one to requiered
    tag_1 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=True, label="Tag 1")
    tag_2 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 2")
    tag_3 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 3")
    tag_4 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 4")
    tag_5 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 5")
    tag_6 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 6")
    
    tags = forms.ModelMultipleChoiceField(label="Select up to 6 tags.", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
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


class FilterForm(Form):
    keywords = forms.CharField(
        required=False,
        label="Filter by text:",
        widget=forms.TextInput(attrs={'placeholder': 'Search by keyword...'})
    )
    tag_1 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 1")
    tag_2 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 2")
    tag_3 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 3")
    tag_4 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 4")
    tag_5 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 5")
    tag_6 = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, label="Tag 6")
