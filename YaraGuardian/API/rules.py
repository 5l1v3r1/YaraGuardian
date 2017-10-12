from django.conf.urls import include, url

from rules.REST_views import (RulesetsListingView,
                              RulesetView,
                              RulesetStatsView,
                              RulesetSearchView,
                              RulesetExportView,
                              RulesetBulkEditView,
                              RulesetDeconflictView,
                              RuleDetailsView,
                              RuleTagsView,
                              RuleMetadataView,
                              RuleCommentsView,
                              RuleCommentDetailsView)


urlpatterns = [

    url(r'^$', RulesetsListingView.as_view(), name='rulesets'),

    url(r'^(?P<group_name>[\s\w]+)/$', RulesetView.as_view(), name='ruleset'),
    url(r'^(?P<group_name>[\s\w]+)/stats/$', RulesetStatsView.as_view(), name='ruleset-stats'),
    url(r'^(?P<group_name>[\s\w]+)/search/$', RulesetSearchView.as_view(), name='ruleset-search'),
    url(r'^(?P<group_name>[\s\w]+)/export/$', RulesetExportView.as_view(), name='ruleset-export'),
    url(r'^(?P<group_name>[\s\w]+)/deconflict/$', RulesetDeconflictView.as_view(), name='ruleset-deconflict'),
    url(r'^(?P<group_name>[\s\w]+)/bulk/$', RulesetBulkEditView.as_view(), name='ruleset-bulk'),

    url(r'^(?P<group_name>[\s\w]+)/(?P<rule_pk>\d+)/$', RuleDetailsView.as_view(), name='rule-details'),
    url(r'^(?P<group_name>[\s\w]+)/(?P<rule_pk>\d+)/tags/(?P<tag>\w+)/$', RuleTagsView.as_view(), name='rule-tags'),
    url(r'^(?P<group_name>[\s\w]+)/(?P<rule_pk>\d+)/metadata/(?P<metakey>\w+)/$', RuleMetadataView.as_view(), name='rule-metadata'),
    url(r'^(?P<group_name>[\s\w]+)/(?P<rule_pk>\d+)/comments/$', RuleCommentsView.as_view(), name='rule-comments'),

    url(r'^(?P<group_name>[\s\w]+)/(?P<rule_pk>\d+)/comments/(?P<comment_pk>\d+)/$',
        RuleCommentDetailsView.as_view(),
        name='rule-comment-details'),
]
