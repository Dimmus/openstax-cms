from django.conf import settings
from wagtail.wagtailcore.models import Site


def build_document_url(url):
    site = Site.objects.get(is_default_site=True)
    if site.port == 80:
        folder = url.split('/')[1]
        filename = url.split('/')[-1]
        return "{}{}/{}".format(settings.MEDIA_URL, folder, filename)
    else:
        return "http://{}:{}{}".format(site.hostname, site.port, url)