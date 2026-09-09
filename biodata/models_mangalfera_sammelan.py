from django.db import models


class MangalferaSammelanBiodata(models.Model):
    # Personal Details
    name = models.CharField(max_length=255, verbose_name="Candidate Full Name")
    gender = models.CharField(max_length=10, verbose_name="Gender")
    dob = models.CharField(max_length=20, verbose_name="Date of Birth")
    marital = models.CharField(max_length=50, verbose_name="Marital Status")
    disability = models.CharField(max_length=150, verbose_name="Any Disability or Minor Problem?")
    tob = models.CharField(max_length=20, verbose_name="Birth Time")
    birthPlace = models.CharField(max_length=100, verbose_name="Birth Place")
    city = models.CharField(max_length=100, verbose_name="Current City")
    country = models.CharField(max_length=100, verbose_name="Current Country")
    visa = models.CharField(max_length=50, verbose_name="Visa Status")
    height = models.CharField(max_length=20, verbose_name="Height")
    weight = models.CharField(max_length=20, verbose_name="Weight (kg)")
    education = models.CharField(max_length=150, verbose_name="Education")
    educationDetail = models.CharField(max_length=200, verbose_name="Education Detail")
    occupationCat = models.CharField(max_length=100, verbose_name="Occupation Type")
    occupationDetails = models.CharField(max_length=200, verbose_name="Company / Business Name")
    salary = models.CharField(max_length=30, verbose_name="Monthly Income (Rs.)")
    shani = models.CharField(max_length=30, verbose_name="Shani / Mangal")
    hobbies = models.CharField(max_length=200, verbose_name="Hobbies")

    # Family Details
    father = models.CharField(max_length=100, verbose_name="Father's Name")
    mother = models.CharField(max_length=100, verbose_name="Mother's Name")
    fatherWp = models.CharField(max_length=20, verbose_name="Father's Mobile No.")
    motherWp = models.CharField(max_length=20, verbose_name="Mother's Mobile No.")
    caste = models.CharField(max_length=100, verbose_name="Type of Brahmin")
    gotra = models.CharField(max_length=100, verbose_name="Gotra")
    kuldevi = models.CharField(max_length=100, verbose_name="Kuldevi")
    siblings = models.TextField(blank=True, verbose_name="Siblings (Brother / Sister)")

    # Lifestyle & Habits
    eating_habbits = models.CharField(max_length=100, verbose_name="Eating Habits")
    alcohol = models.CharField(max_length=10, verbose_name="Alcoholic Drinks?")
    smoke = models.CharField(max_length=10, verbose_name="Smoke?")
    other_habbit = models.CharField(max_length=100, verbose_name="Any Other Habit?")
    legal_case = models.CharField(max_length=100, verbose_name="Any Legal or Police Case?")

    # Partner Preferences
    locChoice = models.CharField(max_length=100, verbose_name="Partner's Location")
    ageGap = models.CharField(max_length=50, verbose_name="Partner's Age Bracket")
    eduChoice = models.CharField(max_length=100, verbose_name="Partner's Education")
    otherChoice = models.TextField(blank=True, verbose_name="Any Other Specific Choice")

    # Registration Details
    who = models.CharField(max_length=100, verbose_name="Who is doing this Registration?")
    regMobile = models.CharField(max_length=20, verbose_name="Mobile No. (person registering)")
    resCat = models.CharField(max_length=100, verbose_name="Current Residence Area")
    nadi = models.CharField(max_length=50, verbose_name="Nadi")
    email = models.EmailField(verbose_name="Email Address")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp Number")
    photo = models.ImageField(upload_to='mangalfera_photos/', verbose_name="Candidate Photo")
    declaration = models.CharField(max_length=20, verbose_name="Declaration")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submission Time")

    class Meta:
        verbose_name = "Mangalfera Sammelan Biodata"
        verbose_name_plural = "Mangalfera Sammelan Biodatas"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.city} - {self.regMobile}"

