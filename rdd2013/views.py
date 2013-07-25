from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    metaInfo = '<table>%s</table>' % '\n'.join(html)
    context = {'meta': metaInfo}
    return render(request, 'userinfo.html', context)
