from django import forms
from .models_booklet_camp_adv import BookletCampAdvBooking

class BookletCampAdvBookingForm(forms.ModelForm):
    class Meta:
        model = BookletCampAdvBooking
        fields = ['name', 'booking_date', 'phone', 'city', 'book']
