# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gwells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vw_well_class',
            fields=[
                ('subactivity', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('well_class', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'verbose_name': 'Registries Well Class',
                'verbose_name_plural': 'Registries Well Classes',
                'db_table': 'vw_well_class',
            },
        ),
        migrations.CreateModel(
            name='AccreditedCertificateCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('acc_cert_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Accredited Certificate UUID')),
                ('name', models.CharField(editable=False, max_length=100, verbose_name='Certificate Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['registries_activity', 'cert_auth'],
                'verbose_name_plural': 'Accredited Certificates',
                'db_table': 'registries_accredited_certificate_code',
            },
        ),
        migrations.CreateModel(
            name='ActivityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_activity_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Activity codes',
                'db_table': 'registries_activity_code',
            },
        ),
        migrations.CreateModel(
            name='ApplicationStatusCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_application_status_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Application Status Codes',
                'db_table': 'registries_application_status_code',
            },
        ),
        migrations.CreateModel(
            name='CertifyingAuthorityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('cert_auth_code', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Certifying Authority Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['cert_auth_code'],
                'verbose_name_plural': 'Certifying Authorities',
                'db_table': 'registries_certifying_authority_code',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('contact_detail_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Contact At UUID')),
                ('contact_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact telephone number')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email adddress')),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Information',
                'db_table': 'registries_contact_detail',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('org_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Organization UUID')),
                ('name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=100, null=True, verbose_name='Street Address')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Town/City')),
                ('postal_code', models.CharField(max_length=10, null=True, verbose_name='Postal Code')),
                ('main_tel', models.CharField(max_length=15, null=True, verbose_name='Telephone number')),
                ('fax_tel', models.CharField(max_length=15, null=True, verbose_name='Fax number')),
                ('website_url', models.URLField(null=True, verbose_name='Website')),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
                ('province_state', models.ForeignKey(db_column='province_state_code', on_delete=django.db.models.deletion.PROTECT, related_name='companies', to='gwells.ProvinceStateCode', verbose_name='Province/State')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Organizations',
                'db_table': 'registries_organization',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('person_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Person UUID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
                ('organization', models.ForeignKey(blank=True, db_column='organization_guid', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person_set', to='registries.Organization')),
            ],
            options={
                'ordering': ['first_name', 'surname'],
                'verbose_name_plural': 'People',
                'db_table': 'registries_person',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_well_qualification_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Qualification / Well Class UUID')),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['subactivity', 'display_order'],
                'verbose_name_plural': 'Qualification codes',
                'db_table': 'registries_well_qualification',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('register_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register UUID')),
                ('registration_no', models.CharField(blank=True, max_length=15, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('register_removal_date', models.DateField(blank=True, null=True, verbose_name='Date of Removal from Register')),
                ('person', models.ForeignKey(db_column='person_guid', on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='registries.Person')),
            ],
            options={
                'verbose_name_plural': 'Registrations',
                'db_table': 'registries_register',
            },
        ),
        migrations.CreateModel(
            name='RegistriesApplication',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('application_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Application UUID')),
                ('file_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ORCS File # reference.')),
                ('over19_ind', models.BooleanField(default=True)),
                ('registrar_notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registrar notes, for internal use only.')),
                ('reason_denied', models.CharField(blank=True, max_length=255, null=True, verbose_name='Free form text explaining reason for denial.')),
                ('primary_certificate_no', models.CharField(max_length=50)),
                ('primary_certificate', models.ForeignKey(blank=True, db_column='acc_cert_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.AccreditedCertificateCode', verbose_name='Certificate')),
                ('registration', models.ForeignKey(db_column='register_guid', on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='registries.Register', verbose_name='Person Reference')),
            ],
            options={
                'verbose_name_plural': 'Applications',
                'db_table': 'registries_application',
            },
        ),
        migrations.CreateModel(
            name='RegistriesApplicationStatus',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('application_status_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Application Status UUID')),
                ('notified_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
                ('application', models.ForeignKey(db_column='application_guid', on_delete=django.db.models.deletion.CASCADE, related_name='status_set', to='registries.RegistriesApplication', verbose_name='Application Reference')),
                ('status', models.ForeignKey(db_column='registries_application_status_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ApplicationStatusCode', verbose_name='Application Status Code Reference')),
            ],
            options={
                'ordering': ['application', 'effective_date'],
                'verbose_name_plural': 'Application status',
                'db_table': 'registries_application_status',
            },
        ),
        migrations.CreateModel(
            name='RegistriesRemovalReason',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_removal_reason_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Registry Removal Reasons',
                'db_table': 'registries_removal_reason_code',
            },
        ),
        migrations.CreateModel(
            name='RegistriesStatusCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_status_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Registry Status Codes',
                'db_table': 'registries_status_code',
            },
        ),
        migrations.CreateModel(
            name='SubactivityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_subactivity_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
                ('registries_activity', models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode')),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Subactivity codes',
                'db_table': 'registries_subactivity_code',
            },
        ),
        migrations.CreateModel(
            name='WellClassCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_well_class_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display_order', 'description'],
                'verbose_name_plural': 'Well Classes',
                'db_table': 'registries_well_class_code',
            },
        ),
        migrations.AddField(
            model_name='registriesapplication',
            name='subactivity',
            field=models.ForeignKey(db_column='registries_subactivity_code', on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='registries.SubactivityCode'),
        ),
        migrations.AddField(
            model_name='register',
            name='register_removal_reason',
            field=models.ForeignKey(blank=True, db_column='registries_removal_reason_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.RegistriesRemovalReason', verbose_name='Removal Reason'),
        ),
        migrations.AddField(
            model_name='register',
            name='registries_activity',
            field=models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode'),
        ),
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.ForeignKey(db_column='registries_status_code', default='P', on_delete=django.db.models.deletion.PROTECT, to='registries.RegistriesStatusCode', verbose_name='Register Entry Status'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='subactivity',
            field=models.ForeignKey(db_column='registries_subactivity_code', on_delete=django.db.models.deletion.PROTECT, related_name='qualification_set', to='registries.SubactivityCode'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='well_class',
            field=models.ForeignKey(db_column='registries_well_class_code', on_delete=django.db.models.deletion.PROTECT, to='registries.WellClassCode'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='person',
            field=models.ForeignKey(db_column='person_guid', on_delete=django.db.models.deletion.PROTECT, related_name='contact_info', to='registries.Person', verbose_name='Person Reference'),
        ),
        migrations.AddField(
            model_name='accreditedcertificatecode',
            name='cert_auth',
            field=models.ForeignKey(db_column='cert_auth_code', on_delete=django.db.models.deletion.PROTECT, to='registries.CertifyingAuthorityCode'),
        ),
        migrations.AddField(
            model_name='accreditedcertificatecode',
            name='registries_activity',
            field=models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode'),
        ),
    ]
