from django.shortcuts import render


# Create your views here.
def browse_page(request, input_path=None):
    entries = []
    return render(request,
                  'browse.html',
                  {
                      'input_path': input_path,
                      'entries': entries,
                  })
    # return HttpResponse(f'<html>Welcome to <span>{input_path}</span></html>')
