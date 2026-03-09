# Generated migration for Bhudev Kalakaar 2026 Talent Registration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0107_physicalform'),
    ]

    operations = [
        migrations.CreateModel(
            name='BhudevKalakaar2026Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200, verbose_name='Full Name of Participant')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, verbose_name='Gender')),
                ('dateOfBirth', models.CharField(max_length=10, verbose_name='Date of Birth (DD-MM-YYYY)')),
                ('ageGroup', models.CharField(choices=[('5-10', '5 Yrs to 10 Yrs'), ('11-20', '11 Yrs to 20 Yrs'), ('21-40', '21 Yrs to 40 Yrs'), ('41-above', '41 Yrs and Above')], max_length=20, verbose_name='Age Group')),
                ('event', models.CharField(choices=[('singing', 'Singing'), ('dancing', 'Dancing'), ('musical-instrument', 'Musical Instrument'), ('others', 'Others')], max_length=50, verbose_name='Event Category')),
                ('talent', models.CharField(help_text='Mention details about your talent (e.g., Which Instrument, Awards, etc.)', max_length=500, verbose_name='Talent Details')),
                ('city', models.CharField(max_length=100, verbose_name='Current Residence City')),
                ('whatsappNumber', models.CharField(max_length=20, verbose_name='WhatsApp Number')),
                ('photo', models.ImageField(upload_to='bk2026_registration_photos/', verbose_name='Participant Photo')),
                ('terms', models.CharField(choices=[('yes', 'Yes, I Agree'), ('no', "No, I Don't Agree")], max_length=10, verbose_name='Terms & Conditions Agreement')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')),
            ],
            options={
                'verbose_name': 'Bhudev Kalakaar 2026 Talent Registration',
                'verbose_name_plural': 'Bhudev Kalakaar 2026 Talent Registrations',
                'ordering': ['-submitted_at'],
            },
        ),
    ]
