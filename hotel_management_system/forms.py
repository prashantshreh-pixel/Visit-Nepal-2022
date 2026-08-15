from django import forms
from datetime import datetime
from .models import RoomCategory


class AvailabilityForm(forms.Form):
    # room_category = forms.ModelChoiceField(
    #     queryset=RoomCategory.objects.all())
    # room = forms.CharField(required=True)
    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
