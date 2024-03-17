from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)


# не стал добавлять для ошибок новое приложение
# т.к. по заданию они лежат в pages
def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)
# https://proghunter.ru/articles/django-base-2023-set-custom-error-view-for-403-404-500-pages
# на этом сайте используют хэндлер


def internal_server_error(request):
    return render(request, 'core/500.html', status=500)
