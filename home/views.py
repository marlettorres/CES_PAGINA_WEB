from django.shortcuts import render

def error_404(request, excepción):
        return render(request, '404.html')
def error_500(request, excepción):
        return render(request, '500.html')
def error_403(request, excepción):
        return render(request, '403.html')