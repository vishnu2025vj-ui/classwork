from django.shortcuts import render
from .forms import MovieForm

def movie(request):
    message = ""
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()  # ✅ This line saves data to DB
            message = f"Movie saved: {movie.name} ({movie.year})"
            form = MovieForm()  # clear the form
    else:
        form = MovieForm()

    return render(request, 'movie.html', {'form': form, 'message': message})
