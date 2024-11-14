from django import forms
from django.forms import ModelForm

from .models import User


class CreatePost(ModelForm):
    project_name = forms.CharField(label="Project Name: ", max_length=50, help_text="Focus on what the project does")
    number_sought = forms.IntegerField(
        label="Desired Number of Seekers: ", min_value=1, max_value=15, help_text="No more than 15")
    project_length = forms.IntegerField(
        label="Expected Project Length", min_value=0, max_value=24, help_text="Estimated length of project in months")

    #initial tag edits; editing later
    PROJECT_TAG_CHOICES = ["undergraduate", "graduate", "research", "laboratory", "survey", "experiment", "academic", "personal", "interview", "accounting", "linguistics", "ESL", "TESL",
    "art_history", "visual_fine_art", "biochemistry", "microbiology", "prehealth", "marine_biology", "chemistry", "business_admin", "economics", "finance", "marketing", "engineering", 
    "communication", "cinema", "media_studies", "mathematics", "data_science", "simulation", "compsci", "info_technology", "counseling", "writing", "criminology", "cybersecurity", "AI", 
    "dental_hygiene", "ECE", "ecology", "aerospace", "biomedical", "mechanical", "english", "lit_and_comp", "journalism", "fine_arts", "graphic_design", "painting", "drawing", "photography", 
    "print_media", "geography", "urban_planning", "health_science", "history", "human_services", "app development", "database", "ecommerce", "infosys", "game_studies", "game_design", 
    "leadership", "intl studies", "big_data", "analytics", "lab_science", "ROTC", "music", "vocal", "music recording", "naval_science", "nursing", "midwifery", "postlicensure", "prelicensure", 
    "earth_science", "oceanography", "philosophy", "politics", "legal_studies", "religion", "phys_ed", "coaching", "phys_therapy", "physics", "astrophysics", "polisci", "global_politics", 
    "psychology", "public_admin", "public_health", "reading", "sociology", "audiology", "theater", "theatre", "dance", "design_tech", "performance", "womens_studies", "world_languages", 
    "world_cultures", "french", "german", "japanese", "spanish", "arabic", "programming", "ethics", "digital_art", "design", "modeling", "biology"] 

    project_tags = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PROJECT_TAG_CHOICES,
    )
    
    post_body = forms.CharField(
        label="Project Description: ", max_length=4000, help_text="Visit the Home Page if you need an example",
        widget=forms.Textarea)

# class for making a user's profile; the forms should get the user's first and last name as well as biography
class ProfileForm(ModelForm):
    school_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label="First name", max_length=50)
    last_name = forms.CharField(label="Last name", max_length=50)
    biography = forms.CharField(label="Biography", widget=forms.Textarea)
    class Meta:
        model = User
        fields = ['school_email', 'password', 'first_name', 'last_name', 'biography']
