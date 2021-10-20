# Generated by Django 3.0.14 on 2021-10-20 09:53

from django.db import migrations, models
import django.db.models.deletion
import invoice.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('invoice', '0011_billeventmutation_billitemmutation_billmutation_billpaymentmutation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='code_sdr',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='currency_sdr_code',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='sender_id',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='sender_type',
        ),
        migrations.RemoveField(
            model_name='historicalbill',
            name='code_sdr',
        ),
        migrations.RemoveField(
            model_name='historicalbill',
            name='currency_sdr_code',
        ),
        migrations.RemoveField(
            model_name='historicalbill',
            name='sender_id',
        ),
        migrations.RemoveField(
            model_name='historicalbill',
            name='sender_type',
        ),
        migrations.RemoveField(
            model_name='historicalinvoice',
            name='code_rcp',
        ),
        migrations.RemoveField(
            model_name='historicalinvoice',
            name='currency_rcp_code',
        ),
        migrations.RemoveField(
            model_name='historicalinvoice',
            name='recipient_id',
        ),
        migrations.RemoveField(
            model_name='historicalinvoice',
            name='recipient_type',
        ),
        migrations.RemoveField(
            model_name='historicalinvoicepayment',
            name='code_rcp',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='code_rcp',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='currency_rcp_code',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='recipient_id',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='recipient_type',
        ),
        migrations.RemoveField(
            model_name='invoicepayment',
            name='code_rcp',
        ),
        migrations.AddField(
            model_name='bill',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='currency_tp_code',
            field=models.CharField(db_column='CurrencyTpCode', default=invoice.models.get_default_currency, max_length=255),
        ),
        migrations.AddField(
            model_name='bill',
            name='thirdparty_id',
            field=models.CharField(db_column='ThirdpartyId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='thirdparty_type',
            field=models.OneToOneField(db_column='ThirdpartyType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='billpayment',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalbill',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalbill',
            name='currency_tp_code',
            field=models.CharField(db_column='CurrencyTpCode', default=invoice.models.get_default_currency, max_length=255),
        ),
        migrations.AddField(
            model_name='historicalbill',
            name='thirdparty_id',
            field=models.CharField(db_column='ThirdpartyId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalbill',
            name='thirdparty_type',
            field=models.ForeignKey(blank=True, db_column='ThirdpartyType', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='historicalbillpayment',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='currency_tp_code',
            field=models.CharField(db_column='CurrencyTpCode', default=invoice.models.get_default_currency, max_length=255),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='thirdparty_id',
            field=models.CharField(db_column='ThirdpartyId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='thirdparty_type',
            field=models.ForeignKey(blank=True, db_column='ThirdpartyType', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='historicalinvoicepayment',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency_tp_code',
            field=models.CharField(db_column='CurrencyTpCode', default=invoice.models.get_default_currency, max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='thirdparty_id',
            field=models.CharField(db_column='ThirdpartyId', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='thirdparty_type',
            field=models.OneToOneField(db_column='ThirdpartyType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='invoicepayment',
            name='code_tp',
            field=models.CharField(db_column='CodeTp', max_length=255, null=True),
        ),
    ]
