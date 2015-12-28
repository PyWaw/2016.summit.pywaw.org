from django.db import models

TALK_LEVELS = (
    ('beginner', 'Beginner'),
    ('advanced', 'Advanced'),
    ('expert', 'Expert'),
)


class TalkProposal(models.Model):
    submit_date = models.DateTimeField(auto_now_add=True)
    speaker_name = models.CharField(max_length=50, verbose_name='Name')
    speaker_email = models.EmailField(verbose_name='Email')
    speaker_phone = models.CharField(max_length=50, verbose_name='Phone',
                                     help_text='We will use it only in case of emergency')
    speaker_tagline = models.CharField(max_length=50, blank=True, verbose_name='Tagline',
                                       help_text='e.g. VP at ACME Corp')
    speaker_website = models.URLField(blank=True, verbose_name='Website')
    speaker_location = models.CharField(max_length=50, blank=True, verbose_name='Location',
                                        help_text='Country and city you live in')
    speaker_twitter = models.CharField(max_length=50, blank=True, verbose_name='Twitter')
    speaker_github = models.CharField(max_length=50, blank=True, verbose_name='GitHub')
    speaker_bio = models.TextField(verbose_name='Bio')
    speaker_previous_talks = models.TextField(blank=True, verbose_name='Previous talks',
                                              help_text='If you had talked at conferences or meetups, list them here, '
                                                        'especially if there are some slides or video recordings')
    talk_title = models.CharField(max_length=250, verbose_name='Title')
    talk_description = models.TextField(verbose_name='Description',
                                        help_text='Public abstract of your talk, it will be published in the agenda')
    talk_level = models.CharField(max_length=10, choices=TALK_LEVELS, verbose_name='Level')
    sponsorship_interested = models.BooleanField(verbose_name='Interested in sponsorship?',
                                                 help_text='Would your company be interested in sponsoring this '
                                                           'conference?')
    sponsorship_email = models.EmailField(blank=True, verbose_name='Sponsorship e-mail')
    comments = models.TextField(blank=True,
                                help_text='Any other comments/questions about conference and call for papers')

    def __str__(self):
        return '{title} - {name}'.format(
            title=self.talk_title,
            name=self.speaker_name,
        )
