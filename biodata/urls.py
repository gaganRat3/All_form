from django.urls import path
from . import views
from . import views_divorce_sammelan
from . import views_40plus_sammelan

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('picnic-registration/', views.picnic_registration_view, name='picnic_registration_form'),
    path('picnic-registration-confirmation/', views.picnic_registration_confirmation, name='picnic_registration_confirmation'),
    path('garba-pass-registration', views.garba_pass_registration_view, name='garba_pass_registration'),
    path('bncf-application/', views.bncf_application_view, name='bncf_application'),
    # Other URL patterns...

    path('birthday-form/', views.birthday_form_view, name='birthday_form'),
    path('submit-birthday/', views.submit_birthday, name='submit_birthday'),
    path('happy-stories/', views.happy_stories_view, name='happy_stories'),
    path('happy-stories/thanks/', views.happy_stories_thanks_view, name='happy_stories_thanks'),
    path('happy-stories/submit/', views.happy_story_submit_view, name='submit_story'),
    path('35th-courier-booklet/', views.courier_booklet_35th_view, name='35th_courier_booklet'),
    path('35th-curier-booklet-success/', views.courier_booklet_35th_success, name='35th_curier_booklet_success'),
    path('booklet-camp-adv-booking/', views.booklet_camp_adv_booking_view, name='booklet_camp_adv_booking'),
    path('booklet-camp-adv-booking-confirmation/', views.booklet_camp_adv_booking_confirmation, name='booklet_camp_adv_booking_confirmation'),
    path('birthday-confirmation/', views.birthday_confirmation, name='birthday_confirmation'),

    path('mega-booklet-correction/', views.mega_booklet_correction_request, name='mega_booklet_correction_form'),
    path('mega-booklet-correction-confirmation/<int:request_id>/', views.mega_booklet_correction_confirmation, name='mega_booklet_correction_confirmation'),

    # Removed old mela_booklet_correction_confirmation path

]

from .views import astrology_form_view, technical_support
from .views import technical_support_confirmation

urlpatterns += [
    path('', views.home_page, name='home_page'),
    path('divorce-sammelan-form/', views_divorce_sammelan.divorce_sammelan_form_view, name='divorce_sammelan_form'),
    path('40-plus-sammelan-form/', views_40plus_sammelan.forty_plus_sammelan_form_view, name='40_plus_sammelan_form'),
    path('physical-form/', views.physical_form_view, name='physical_form'),
    path('physical-form-success/', views.physical_form_success_view, name='physical_form_success'),
    path('business-directory/', views.business_directory, name='business_directory'),
    # Removed separate form page path as form is handled in home_page
    # path('form/', views.biodata_form, name='biodata_form'),
    path('download-pdf/<int:candidate_id>/', views.download_biodata_pdf, name='download_biodata_pdf'),
    path('confirmation/<int:candidate_id>/', views.confirmation_page, name='confirmation'),
    # path('confirmation/', views.confirmation_redirect, name='confirmation_redirect'),  # Removed: no such view exists
    # path('gallery/', views.gallery_page, name='gallery_page'),  # Removed: no such view exists
    path('contact-us/', views.contact_us_page, name='contact_us_page'),
    path('about-us/', views.about_us_page, name='about_us_page'),
    path('advance-pass-booking/', views.advance_pass_booking, name='advance_pass_booking'),
    path('advance-booklet-booking/', views.advance_booklet_booking, name='advance_booklet_booking'),
    path('advance-booklet-booking/confirmation/<int:booking_id>/', views.advance_booklet_booking_confirmation, name='advance_booklet_booking_confirmation'),
    path('stage-registration/', views.stage_registration, name='stage_registration'),
    path('stage-registration/confirmation/<int:registration_id>/', views.stage_registration_confirmation, name='stage_registration_confirmation'),
    path('spot-advance-booklet/', views.spot_advance_booklet_view, name='spot_advance_booklet'),
    path('spot-advance-booklet/confirmation/<int:booking_id>/', views.spot_advance_booklet_confirmation, name='spot_advance_booklet_confirmation'),
    path('astrology_form/', astrology_form_view, name='astrology_form'),
    path('zoom-register/', views.register_view, name='zoom_register'),
    path('zoom-confirmation/', views.confirmation_view, name='zoom_confirmation'),
    path('mega-booklet-data-correction/', views.mega_booklet_correction_request, name='mega_booklet_data_correction_form'),
    path('technical-support/', technical_support, name='technical_support'),
    path('technical-support/confirmation/', technical_support_confirmation, name='technical_support_confirmation'),
    path('global-karmkand-directory/',
         __import__('biodata.views_karmkand_directory').views_karmkand_directory.global_karmkand_directory,
         name='global_karmkand_directory'),
    path('garba-form/', views.garba_pass_registration_view, name='garba_form'),
    # Removed submit_garba_form path as it is redundant and removed from views.py
    # path('garba-form/submit/', views.submit_garba_form, name='submit_form'),
    path('garba-confirmation/', views.garba_confirmation, name='garba_confirmation'),
    
    # Audience registration URLs
    path('submit-ticket/', views.audience_registration_view, name='audience_registration'),
    path('audience-form/', views.audience_registration_view, name='audience_form'),
    path('audience-confirmation/', views.audience_confirmation, name='audience_confirmation'),

    
    # Participant Event Registration URLs
    path('participant-form/', views.participant_form_view, name='participant_form'),
    path('participant-confirmation/<int:participant_id>/', views.participant_confirmation, name='participant_confirmation'),
    path('submit_form/', views.participant_form_view, name='submit_form'),  # For form action compatibility
    
    # 34th Sammelan Payment Form URLs
    path('34th-sammelan-payment/', views.sammelan_payment_form_view, name='sammelan_payment_form'),
    path('34th-sammelan-payment/confirmation/<int:payment_id>/', views.sammelan_payment_confirmation, name='sammelan_payment_confirmation'),
    path('booklet-library/', views.booklet_library_view, name='booklet_library'),
    path('booklet-library/confirmation/<int:pk>/', views.booklet_library_confirmation, name='booklet_library_confirmation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
