from django.db import models

class Sammelan37MumbaiMaharashtra(models.Model):
    # Choices for residence area
    RESIDENCE_CHOICES = [
        ('gujarat_region', 'Gujarat Region (North or Central or South)'),
        ('saurashtra_region', 'Saurashtra Region'),
        ('kachchh_region', 'Kachchh Region'),
        ('mumbai_maharashtra', 'Mumbai & Maharashtra Region'),
        ('rest_of_india', 'Rest of Indian Region (except Gujarat & Maharashtra)'),
        ('nri', 'NRI (Any Visa)'),
    ]
    
    MARITAL_CHOICES = [
        ('never_married', 'Never Married (Unmarried)'),
        ('divorce_no_child', 'Divorce (No Child)'),
        ('divorce_having_child', 'Divorce (Having Child)'),
        ('widow_no_child', 'Widow (No Child)'),
        ('widow_having_child', 'Widow (Having Child)'),
        ('divorce_annulled', 'Divorce (Annulled)'),
        ('divorce_in_process', 'Divorce in Process'),
        ('separated', 'Separated'),
        ('gol_dhana_cancel', '1 Time Gol-Dhana Done, but then Cancelled'),
        ('engagement_cancel', '1 Time Engagement Done, but then Cancelled'),
    ]
    
    VISA_CHOICES = [
        ('indian_citizen', 'Indian Citizen'),
        ('nri_student_visa', 'NRI - Student Visa'),
        ('nri_work_permit', 'NRI - Work Permit'),
        ('nri_pr', 'NRI - PR'),
        ('nri_pr_in_process', 'NRI - PR In Process'),
        ('nri_green_card_usa', 'NRI - Green Card (USA)'),
        ('nri_blue_card_eu', 'NRI - Blue Card (EU)'),
        ('nri_citizenship', 'NRI - Citizenship'),
        ('nri_visitor_visa', 'NRI - Visitor Visa'),
        ('nri_h1b_usa', 'NRI - H1B (USA)'),
        ('nri_business_visa', 'NRI - Business Visa'),
        ('nri_oci', 'NRI - OCI'),
        ('nri_f1', 'NRI - F1'),
    ]
    
    NADI_CHOICES = [
        ('aadhya_nadi', 'Aadhya Nadi'),
        ('madhya_nadi', 'Madhya Nadi'),
        ('antya_nadi', 'Antya Nadi'),
        ('dont_know', 'I Dont Know'),
        ('dont_believe', "We Don't Believe"),
    ]
    
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    marital = models.CharField(max_length=30, choices=MARITAL_CHOICES, default='never_married')
    disability = models.TextField()
    tob = models.CharField(max_length=20)
    birthPlace = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    visa = models.CharField(max_length=50, choices=VISA_CHOICES, default='indian_citizen')
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    education = models.CharField(max_length=100)
    educationDetail = models.CharField(max_length=100)
    occupationCat = models.CharField(max_length=50)
    occupationDetails = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)
    shani = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    fatherWp = models.CharField(max_length=20)
    motherWp = models.CharField(max_length=20)
    caste = models.CharField(max_length=50)
    gotra = models.CharField(max_length=50)
    kuldevi = models.CharField(max_length=50)
    siblings = models.TextField()
    eating_habbits = models.CharField(max_length=50)
    alcohol = models.CharField(max_length=10)
    smoke = models.CharField(max_length=10)
    other_habbit = models.CharField(max_length=50)
    legal_case = models.CharField(max_length=100)
    locChoice = models.CharField(max_length=100)
    ageGap = models.CharField(max_length=50)
    eduChoice = models.CharField(max_length=100)
    otherChoice = models.TextField()
    who = models.CharField(max_length=100)
    regMobile = models.CharField(max_length=20)
    resCat = models.CharField(max_length=50, choices=RESIDENCE_CHOICES, default='nri')
    nadi = models.CharField(max_length=20, choices=NADI_CHOICES, default='dont_know')
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='sammelan37_photos/')
    declaration = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "37th Sammelan - Mumbai & Maharashtra"
        verbose_name_plural = "37th Sammelan - Mumbai & Maharashtra"
