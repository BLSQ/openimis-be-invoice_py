# Generated by Django 3.0.14 on 2021-09-13 12:20

import core.fields
import datetime
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfallback.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('subject_id', models.CharField(db_column='SubjectId', max_length=255, null=True)),
                ('recipient_id', models.CharField(db_column='RecipientId', max_length=255, null=True)),
                ('code', models.CharField(db_column='Code', max_length=255)),
                ('code_rcp', models.CharField(db_column='CodeRcp', max_length=255, null=True)),
                ('code_ext', models.CharField(db_column='CodeExt', max_length=255, null=True)),
                ('date_due', core.fields.DateField(db_column='DateDue', null=True)),
                ('date_invoice', core.fields.DateField(db_column='DateInvoice', default=datetime.date.today, null=True)),
                ('date_payed', core.fields.DateField(db_column='DatePayed', null=True)),
                ('amount_discount', models.DecimalField(db_column='AmountDiscount', decimal_places=2, default=0, max_digits=18, null=True)),
                ('amount_net', models.DecimalField(db_column='AmountNet', decimal_places=2, max_digits=18)),
                ('amount_total', models.DecimalField(db_column='AmountTotal', decimal_places=2, max_digits=18, null=True)),
                ('tax_analysis', jsonfallback.fields.FallbackJSONField(db_column='TaxAnalysis', null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Draft'), (1, 'Validated'), (2, 'Payed'), (3, 'Cancelled'), (4, 'Deleted')], db_column='Status', default=0)),
                ('currency_rcp_code', models.CharField(db_column='CurrencyRcpCode', default=None, max_length=255)),
                ('currency_code', models.CharField(db_column='CurrencyCode', default=None, max_length=255)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
                ('terms', models.TextField(blank=True, db_column='Terms', null=True)),
                ('payment_reference', models.CharField(db_column='PaymentReference', max_length=255, null=True)),
                ('recipient_type', models.OneToOneField(db_column='RecipientType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient_type', to='contenttypes.ContentType')),
                ('subject_type', models.OneToOneField(db_column='SubjectType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subject_type', to='contenttypes.ContentType')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblInvoice',
                'managed': True,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoicePayment',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Accepted'), (1, 'Rejected'), (2, 'Refunded')], db_column='Status')),
                ('code_ext', models.CharField(db_column='CodeExt', max_length=255, null=True)),
                ('code_rcp', models.CharField(db_column='CodeRcp', max_length=255, null=True)),
                ('code_receipt', models.CharField(db_column='CodeReceipt', max_length=255, null=True)),
                ('label', models.CharField(db_column='Label', max_length=255, null=True)),
                ('amount_payed', models.DecimalField(db_column='AmountPayed', decimal_places=2, max_digits=18, null=True)),
                ('fees', models.DecimalField(db_column='Fees', decimal_places=2, max_digits=18, null=True)),
                ('amount_received', models.DecimalField(db_column='AmountReceived', decimal_places=2, max_digits=18, null=True)),
                ('date_payment', core.fields.DateField(db_column='DatePayment', null=True)),
                ('invoice', models.ForeignKey(db_column='InvoiceId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments', to='invoice_payment.Invoice')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoicepayment_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoicepayment_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblInvoicePayment',
                'managed': True,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(db_column='Code', max_length=255)),
                ('line_id', models.CharField(db_column='LineId', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('details', jsonfallback.fields.FallbackJSONField(db_column='Details', null=True)),
                ('ledger_account', models.CharField(db_column='LedgerAccount', max_length=255, null=True)),
                ('quantity', models.IntegerField(db_column='Quantity', null=True)),
                ('unit_price', models.DecimalField(db_column='UnitPrice', decimal_places=2, max_digits=18, null=True)),
                ('discount', models.DecimalField(db_column='Discount', decimal_places=2, max_digits=18, null=True)),
                ('tax_rate', models.UUIDField(db_column='CalculationUUID', null=True)),
                ('tax_analysis', jsonfallback.fields.FallbackJSONField(db_column='TaxAnalysis', null=True)),
                ('amount_total', models.DecimalField(db_column='AmountTotal', decimal_places=2, max_digits=18, null=True)),
                ('amount_net', models.DecimalField(db_column='AmountNet', decimal_places=2, max_digits=18, null=True)),
                ('invoice', models.ForeignKey(db_column='InvoiceId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_items', to='invoice_payment.Invoice')),
                ('line_type', models.OneToOneField(db_column='LineType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_type', to='contenttypes.ContentType')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoicelineitem_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoicelineitem_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblInvoiceLineItem',
                'managed': True,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceEvent',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('event_type', models.SmallIntegerField(choices=[(0, 'Message'), (1, 'Status'), (2, 'Warning'), (3, 'Payment'), (4, 'Payment Error')], db_column='Status', default=0)),
                ('message', models.CharField(db_column='Message', max_length=500, null=True)),
                ('invoice', models.ForeignKey(db_column='InvoiceId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='invoice_payment.Invoice')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoiceevent_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoiceevent_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblInvoiceEvent',
                'managed': True,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInvoicePayment',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Accepted'), (1, 'Rejected'), (2, 'Refunded')], db_column='Status')),
                ('code_ext', models.CharField(db_column='CodeExt', max_length=255, null=True)),
                ('code_rcp', models.CharField(db_column='CodeRcp', max_length=255, null=True)),
                ('code_receipt', models.CharField(db_column='CodeReceipt', max_length=255, null=True)),
                ('label', models.CharField(db_column='Label', max_length=255, null=True)),
                ('amount_payed', models.DecimalField(db_column='AmountPayed', decimal_places=2, max_digits=18, null=True)),
                ('fees', models.DecimalField(db_column='Fees', decimal_places=2, max_digits=18, null=True)),
                ('amount_received', models.DecimalField(db_column='AmountReceived', decimal_places=2, max_digits=18, null=True)),
                ('date_payment', core.fields.DateField(db_column='DatePayment', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(blank=True, db_column='InvoiceId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='invoice_payment.Invoice')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical invoice payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInvoiceLineItem',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(db_column='Code', max_length=255)),
                ('line_id', models.CharField(db_column='LineId', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('details', jsonfallback.fields.FallbackJSONField(db_column='Details', null=True)),
                ('ledger_account', models.CharField(db_column='LedgerAccount', max_length=255, null=True)),
                ('quantity', models.IntegerField(db_column='Quantity', null=True)),
                ('unit_price', models.DecimalField(db_column='UnitPrice', decimal_places=2, max_digits=18, null=True)),
                ('discount', models.DecimalField(db_column='Discount', decimal_places=2, max_digits=18, null=True)),
                ('tax_rate', models.UUIDField(db_column='CalculationUUID', null=True)),
                ('tax_analysis', jsonfallback.fields.FallbackJSONField(db_column='TaxAnalysis', null=True)),
                ('amount_total', models.DecimalField(db_column='AmountTotal', decimal_places=2, max_digits=18, null=True)),
                ('amount_net', models.DecimalField(db_column='AmountNet', decimal_places=2, max_digits=18, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(blank=True, db_column='InvoiceId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='invoice_payment.Invoice')),
                ('line_type', models.ForeignKey(blank=True, db_column='LineType', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical invoice line item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInvoiceEvent',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('event_type', models.SmallIntegerField(choices=[(0, 'Message'), (1, 'Status'), (2, 'Warning'), (3, 'Payment'), (4, 'Payment Error')], db_column='Status', default=0)),
                ('message', models.CharField(db_column='Message', max_length=500, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(blank=True, db_column='InvoiceId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='invoice_payment.Invoice')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical invoice event',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInvoice',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('subject_id', models.CharField(db_column='SubjectId', max_length=255, null=True)),
                ('recipient_id', models.CharField(db_column='RecipientId', max_length=255, null=True)),
                ('code', models.CharField(db_column='Code', max_length=255)),
                ('code_rcp', models.CharField(db_column='CodeRcp', max_length=255, null=True)),
                ('code_ext', models.CharField(db_column='CodeExt', max_length=255, null=True)),
                ('date_due', core.fields.DateField(db_column='DateDue', null=True)),
                ('date_invoice', core.fields.DateField(db_column='DateInvoice', default=datetime.date.today, null=True)),
                ('date_payed', core.fields.DateField(db_column='DatePayed', null=True)),
                ('amount_discount', models.DecimalField(db_column='AmountDiscount', decimal_places=2, default=0, max_digits=18, null=True)),
                ('amount_net', models.DecimalField(db_column='AmountNet', decimal_places=2, max_digits=18)),
                ('amount_total', models.DecimalField(db_column='AmountTotal', decimal_places=2, max_digits=18, null=True)),
                ('tax_analysis', jsonfallback.fields.FallbackJSONField(db_column='TaxAnalysis', null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Draft'), (1, 'Validated'), (2, 'Payed'), (3, 'Cancelled'), (4, 'Deleted')], db_column='Status', default=0)),
                ('currency_rcp_code', models.CharField(db_column='CurrencyRcpCode', default=None, max_length=255)),
                ('currency_code', models.CharField(db_column='CurrencyCode', default=None, max_length=255)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
                ('terms', models.TextField(blank=True, db_column='Terms', null=True)),
                ('payment_reference', models.CharField(db_column='PaymentReference', max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('recipient_type', models.ForeignKey(blank=True, db_column='RecipientType', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType')),
                ('subject_type', models.ForeignKey(blank=True, db_column='SubjectType', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical invoice',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
