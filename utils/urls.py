from django.conf.urls import url

from utils.views import (CrunchProductStatsView, CrunchAgentStatsView,
                         SleuthUserTopUpView, SleuthGetUserBalanceView)

urlpatterns = [
    url('^crunch/agents/$', CrunchAgentStatsView.as_view()),
    url('^crunch/products/$', CrunchProductStatsView.as_view()),
    url('^billing/add$', SleuthUserTopUpView.as_view()),
    url('^billing/balance$', SleuthGetUserBalanceView.as_view())
]
