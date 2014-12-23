from django.conf.urls import patterns, url

urlpatterns = patterns('django.contrib.auth.views',
    url('^login', "login", {"template_name": "{{ app_name }}/login.html"}, name='{{ app_name }}_login'),
    url('^logout', "logout", {"template_name": "{{ app_name }}/logged_out.html"}, name='{{ app_name }}_logout'),
)

urlpatterns += patterns('{{ app_name }}.views',
    url(r'^$', "{{ app_name }}_view", name="{{ app_name }}_view"),
)
