# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('speaker_name', models.CharField(verbose_name='Name', max_length=50)),
                ('speaker_email', models.EmailField(verbose_name='Email', max_length=254)),
                ('speaker_phone', models.CharField(help_text='We will use it only in case of emergency', verbose_name='Phone', max_length=50)),
                ('speaker_tagline', models.CharField(blank=True, help_text='e.g. VP at ACME Corp', verbose_name='Tagline', max_length=50)),
                ('speaker_website', models.URLField(blank=True, verbose_name='Website')),
                ('speaker_location', models.CharField(blank=True, help_text='Country and city you live in', verbose_name='Location', max_length=50)),
                ('speaker_twitter', models.CharField(blank=True, verbose_name='Twitter', max_length=50)),
                ('speaker_github', models.CharField(blank=True, verbose_name='GitHub', max_length=50)),
                ('speaker_bio', models.TextField(verbose_name='Bio')),
                ('speaker_previous_talks', models.TextField(blank=True, help_text='If you had talked at conferences or meetups, list them here, especially if there are some slides or video recordings', verbose_name='Previous talks')),
                ('talk_title', models.CharField(verbose_name='Title', max_length=250)),
                ('talk_description', models.TextField(help_text='Public abstract of your talk, it will be published in the agenda', verbose_name='Description')),
                ('talk_level', models.CharField(verbose_name='Level', choices=[('beginner', 'Beginner'), ('advanced', 'Advanced'), ('expert', 'Expert')], max_length=10)),
                ('sponsorship_interested', models.BooleanField(help_text='Would your company be interested in sponsoring this conference?', verbose_name='Interested in sponsorship?')),
                ('sponsorship_email', models.EmailField(blank=True, verbose_name='Sponsorship e-mail', max_length=254)),
                ('comments', models.TextField(blank=True, help_text='Any other comments/questions about conference and call for papers')),
            ],
        ),
    ]
