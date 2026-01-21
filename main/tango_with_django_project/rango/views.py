from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    html_content = """
    <html>
        <body>
            <a>Rango says hey there partner!</a>
            <a href="/rango/about/">About</a>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def about(request):
    html_content = """
    <html>
        <body>
            <a>Rango says here is the about page.</a>
            <a href="/rango/">Index</a>
        </body>
    </html>
    """
    return HttpResponse(html_content)