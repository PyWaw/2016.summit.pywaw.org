from django.core.urlresolvers import reverse
from django.test import TestCase
from . import models


class CallForPapersTestCase(TestCase):

    def test_submit_talk(self):
        response = self.client.post(
            path=reverse('talk_proposal_create'),
            data={
                'speaker_name': 'Guido van Rossum',
                'speaker_email': 'guido@python.org',
                'speaker_phone': '+01 123 234 345',
                'speaker_bio': 'I made it.',
                'talk_title': 'A few interesting things about Python',
                'talk_description': 'Python is a very good programming language.',
                'talk_level': 'beginner',
            }
        )

        self.assertRedirects(response, reverse('talk_proposal_success'))
        self.assertTrue(models.TalkProposal.objects.filter(
            speaker_email='guido@python.org',
        ).exists())
