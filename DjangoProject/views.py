from cgitb import html
from django.http import HttpResponse

html_string = """
<html>
<h1>404 not found!!</h1>
<p>nah just kiddin</p>
</html>
"""

def home_view(request):
    print('home')
    return HttpResponse(html_string)
