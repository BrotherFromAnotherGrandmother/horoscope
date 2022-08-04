from django.shortcuts import render


# Create your views here.
def get_info_about_kianu(request):
    data = {
        'year_born': 1964,
        'city_born': 'Злынка',
        'movie_name': 'The Lord of the rings',
    }
    return render(request, 'Kianu_Rivz/index.html', context=data)
