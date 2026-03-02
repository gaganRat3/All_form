from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('biodata', '0037_alter_technicalsupportrequest_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDirectoryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('business_name', models.CharField(max_length=200)),
                ('business_type', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('address', models.CharField(max_length=300, blank=True)),
                ('image', models.ImageField(upload_to='business_directory/', blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
