from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import conference.views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^call-for-papers/$', conference.views.TalkProposalCreateView.as_view(), name='talk_proposal_create'),
    url(r'^call-for-papers/success/$', conference.views.TalkProposalSuccessView.as_view(), name='talk_proposal_success'),
    url(r'^admin/', include(admin.site.urls)),
]
