from django.shortcuts import render

# Create your views here.
def get_info_about_beautiful_table(request):
    return render(request, 'table/beautiful_table.html')