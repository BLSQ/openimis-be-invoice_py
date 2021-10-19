# Generated by Django 3.0.14 on 2021-10-19 13:51

import core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_missing_roles'),
        ('invoice', '0010_auto_20211018_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillPaymentMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='invoice.BillPayment')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill_payments', to='core.MutationLog')),
            ],
            options={
                'db_table': 'bill_BillPaymentMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
        migrations.CreateModel(
            name='BillMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='invoice.Bill')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bills', to='core.MutationLog')),
            ],
            options={
                'db_table': 'bill_BillMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
        migrations.CreateModel(
            name='BillItemMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bile_items', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='invoice.BillItem')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill_line_items', to='core.MutationLog')),
            ],
            options={
                'db_table': 'bill_BillLineItemsMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
        migrations.CreateModel(
            name='BillEventMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill_event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='invoice.BillEvent')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill_event_messages', to='core.MutationLog')),
            ],
            options={
                'db_table': 'bill_BillEventMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
    ]
