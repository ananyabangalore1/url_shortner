from django.shortcuts import render, redirect
from .models import URL
from .forms import ShortenURLForm

def shorten_url(request):
  if request.method == 'POST':
    form = ShortenURLForm(request.POST)
    if form.is_valid():
      url = form.cleaned_data['url']  # Access cleaned URL value
      try:
        url_obj = URL.objects.create(original_url=url)
        short_url = request.build_absolute_uri(url_obj.short_code)
        context = {'original_url': url, 'shortened_url': short_url}
        return render(request, 'success.html', context)
      except Exception as e:
        error = str(e)
        context = {'error': error}
        return render(request, 'unsuccessful.html', context)
  else:
    form = ShortenURLForm()  # Empty form for initial rendering

  context = {'form': form}
  return render(request, 'shorten_url.html', context)

def redirect_url(request, short_code):
  url_obj = URL.objects.get(short_code=short_code)
  url_obj.access_count += 1
  url_obj.save()
  return redirect(url_obj.original_url)
