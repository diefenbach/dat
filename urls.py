from django.conf.urls import patterns, url


urlpatterns = patterns('{{ app_name }}.views',
    url(r'^$', "{{ app_name }}_view", name="{{ app_name }}_view"),
)
