from portafolio.models import Page

def get_pages(request):
    pages = Page.objects.values_list('id', 'title', 'slug', 'visible')
    slugs = Page.objects.all()
    return {
        'pages': pages,
        'slugs': slugs,
    }