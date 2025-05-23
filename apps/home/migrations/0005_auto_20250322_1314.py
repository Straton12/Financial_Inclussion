# Generated by Django 3.2.6 on 2025-03-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_surveydata2016_surveydata2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveydata2016',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='bank_account_current',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='bank_account_everyday',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='bank_account_savings',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='bank_overdraft',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='credit_card',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='debit_card',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='education_level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='financially_excluded',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_crop',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_education',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_health_other',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_home',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_life',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_livestock',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_motor',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_nhif',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='insurance_other',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_agri_buyer_supplier',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_bank',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_digital_app',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_employer',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_family_friend',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_goods_credit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_govt',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_group_chama',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_hire_purchase',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_microfinance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_mobile_banking',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_mortgage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_sacco',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_shopkeeper_cash',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='loan_shylock',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='marital_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='mobile_money_registered',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='pension_mbao',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='pension_nssf',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='pension_other',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='population_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='postbank_account',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='relationship_to_hh',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='residence_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_family_friend',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_group_friends',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_microfinance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_mobile_banking',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_sacco',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='surveydata2016',
            name='savings_secret_place',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
