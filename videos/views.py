from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user  # Assuming user is logged in
            if  not video.video_url:
                form.add_error(None, 'Either upload a file or provide a URL')
                return render(request, 'upload_video.html', {'form': form})
            video.save()
            return redirect('video_list')  # Redirect to video listing page
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(uploaded_by__username__icontains=query)
        )
    else:
        videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('video_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def edit_video(request, id):
    video = get_object_or_404(Video, id=id)
    if request.user == video.uploaded_by:
        if request.method == 'POST':
            form = VideoForm(request.POST, instance=video)
            if form.is_valid():
                form.save()
                return redirect('video_list')  # Redirect to the video list after saving
        else:
            form = VideoForm(instance=video)
        return render(request, 'edit_video.html', {'form': form, 'video': video})
    else:
        return redirect('video_list')  # Redirect to video list if the user is not the uploader

@login_required
def delete_video(request, id):
    video = get_object_or_404(Video, id=id)
    if request.user == video.uploaded_by:
        video.delete()
    return redirect('video_list')  # Redirect to video list after deletion

