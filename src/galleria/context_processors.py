from django.conf import settings

def galleria_urls(request):
    static_url = getattr(settings, 'STATIC_URL')
    galleria_url = getattr(
        settings, 'GALLERIA_URL', '%sgalleria/src/' % static_url)
    galleria_script = getattr(
        settings, 'GALLERIA_SCRIPT', '%sgalleria.js' % galleria_url)
    galleria_theme = getattr(
        settings, 'GALLERIA_THEME',
        '%sthemes/classic/galleria.classic.js' % galleria_url)
    return {
        'GALLERIA_URL': galleria_url,
        'GALLERIA_SCRIPT': galleria_script,
        'GALLERIA_THEME': galleria_theme,
    }
