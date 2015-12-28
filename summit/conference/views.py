from django.core.urlresolvers import reverse_lazy
from django.views import generic
from . import models


class TalkProposalCreateView(generic.CreateView):
    model = models.TalkProposal
    fields = [
        'speaker_name',
        'speaker_email',
        'speaker_phone',
        'speaker_tagline',
        'speaker_website',
        'speaker_location',
        'speaker_twitter',
        'speaker_github',
        'speaker_bio',
        'speaker_previous_talks',
        'talk_title',
        'talk_description',
        'talk_level',
        'sponsorship_interested',
        'sponsorship_email',
        'comments',
    ]
    success_url = reverse_lazy('talk_proposal_success')


class TalkProposalSuccessView(generic.TemplateView):
    template_name = 'conference/talkproposal_success.html'
