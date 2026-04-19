from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import Http404
from django.conf import settings
from django.conf.urls.static import static
from biodata.models_37th_sammelan import Sammelan37MumbaiMaharashtra


def _get_sammelan37_model_admin():
    model_admin = admin.site._registry.get(Sammelan37MumbaiMaharashtra)
    if not model_admin:
        raise Http404('37th UK-Europe admin is not registered.')
    return model_admin


def sammelan37_uk_europe_changelist_alias(request):
    return _get_sammelan37_model_admin().changelist_view(request)


def sammelan37_uk_europe_add_alias(request):
    return _get_sammelan37_model_admin().add_view(request)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path(
        'admin/biodata/sammelan37mumbaimaharashtra/',
        RedirectView.as_view(url='/admin/biodata/37_sammelan_UK_europe/', permanent=False),
    ),
    path(
        'admin/biodata/sammelan37mumbaimaharashtra/add/',
        RedirectView.as_view(url='/admin/biodata/37_sammelan_UK_europe/add/', permanent=False),
    ),
    path(
        'admin/biodata/37_sammelan_UK_europe/',
        admin.site.admin_view(sammelan37_uk_europe_changelist_alias),
        name='admin_37_sammelan_uk_europe_changelist',
    ),
    path(
        'admin/biodata/37_sammelan_UK_europe/add/',
        admin.site.admin_view(sammelan37_uk_europe_add_alias),
        name='admin_37_sammelan_uk_europe_add',
    ),
    path('admin/', admin.site.urls),
    path('', include('biodata.urls')),
    path('test/', include('test_form.urls')),       # ← test form app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
