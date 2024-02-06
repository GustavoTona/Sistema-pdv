from django.shortcuts import render, HttpResponse

def dashboard(request):
    return render(request, 'dashboard/dashboard_list.html')