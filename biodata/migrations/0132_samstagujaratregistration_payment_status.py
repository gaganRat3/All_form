# Generated manually on 2026-08-24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biodata", "0131_alter_samstagujaratregistration_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="samstagujaratregistration",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pending", "Pending"),
                    ("paid", "Payment Success"),
                    ("partial", "Partial"),
                    ("unpaid", "Unpaid"),
                    ("conf_pay_pending", "Confirmation Done & Payment Pending"),
                    ("paid_member", "Paid Member"),
                ],
                default="pending",
                max_length=30,
                verbose_name="Payment Status (Admin)",
            ),
        ),
    ]
