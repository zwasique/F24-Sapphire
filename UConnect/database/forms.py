from django import forms


class CreatePost(forms.Form):
    project_name = forms.CharField(label="Project Name: ", max_length=50, help_text="Focus on what the project does")
    number_sought = forms.IntegerField(
        label="Desired Number of Seekers: ", min_value=1, max_value=15, help_text="No more than 15")
    project_length = forms.IntegerField(
        label="Expected Project Length", min_value=0, max_value=24, help_text="Estimated length of project in months")
    # project tags, seeking tags (guys i'm inclined to just have one field for these.)
    post_body = forms.CharField(
        label="Project Description: ", max_length=4000, help_text="Visit the Home Page if you need an example")


class SetProfile(forms.Form):
    pass
