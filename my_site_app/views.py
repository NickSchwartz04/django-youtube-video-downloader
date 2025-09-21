from .models import homeModel
from django.shortcuts import render
from pytubefix import *
from django.http import FileResponse
import os

def home(request):
    content = homeModel.objects.all()
    context = {
        'content': content
    }
    return render(request, "index.html", context=context)

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        yt = YouTube(link)
        stream = yt.streams.get_lowest_resolution()

        download_path = stream.download(output_path="media")

        response = FileResponse(open(download_path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(download_path)}"'
        return response

    return render(request, 'youtube.html')



