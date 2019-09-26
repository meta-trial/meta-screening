# Generated by Django 2.2.5 on 2019-09-25 23:31

import django.core.validators
from django.db import migrations
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):

    dependencies = [("meta_screening", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="initials",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        "[A-Z]{1,3}", "Invalid format"
                    ),
                    django.core.validators.MinLengthValidator(2),
                    django.core.validators.MaxLengthValidator(3),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="initials",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        "[A-Z]{1,3}", "Invalid format"
                    ),
                    django.core.validators.MinLengthValidator(2),
                    django.core.validators.MaxLengthValidator(3),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="initials",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        "[A-Z]{1,3}", "Invalid format"
                    ),
                    django.core.validators.MinLengthValidator(2),
                    django.core.validators.MaxLengthValidator(3),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="initials",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        "[A-Z]{1,3}", "Invalid format"
                    ),
                    django.core.validators.MinLengthValidator(2),
                    django.core.validators.MaxLengthValidator(3),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="initials",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        "[A-Z]{1,3}", "Invalid format"
                    ),
                    django.core.validators.MinLengthValidator(2),
                    django.core.validators.MaxLengthValidator(3),
                ],
            ),
        ),
    ]
