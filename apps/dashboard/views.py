from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from apps.news.models import News, Category, Notice, Ticker, SamajCommunity
from apps.events.models import Event
from apps.gallery.models import Album, Photo
from apps.accounts.models import User
from .forms import (
    NewsForm, NoticeForm, EventForm, AlbumForm, TickerForm, 
    PhotoForm, SamajCommunityForm
)

def is_admin(user):
    return user.is_active and (user.is_superuser or user.is_staff)

@login_required
@user_passes_test(is_admin)
def dashboard_home(request):
    context = {
        'total_news': News.objects.count(),
        'total_events': Event.objects.count(),
        'total_notices': Notice.objects.count(),
        'total_users': User.objects.count(),
        'total_albums': Album.objects.count(),
    }
    return render(request, 'dashboard/home.html', context)

# News / Posts
@login_required
@user_passes_test(is_admin)
def manage_posts(request):
    posts = News.objects.all().order_by('-created_at')
    return render(request, 'dashboard/posts.html', {'posts': posts})

@login_required
@user_passes_test(is_admin)
def add_edit_post(request, pk=None):
    post = get_object_or_404(News, pk=pk) if pk else None
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post saved successfully.')
            return redirect('dashboard:posts')
    else:
        form = NewsForm(instance=post)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Post'})

@login_required
@user_passes_test(is_admin)
def delete_post(request, pk):
    post = get_object_or_404(News, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted.')
    return redirect('dashboard:posts')

# Rajasthan & Society News (Filtered views of posts)
@login_required
@user_passes_test(is_admin)
def rajasthan_news(request):
    category = Category.objects.get(slug='rajasthan')
    posts = News.objects.filter(category=category).order_by('-created_at')
    return render(request, 'dashboard/posts.html', {'posts': posts, 'title': 'Rajasthan News'})


# Notices
@login_required
@user_passes_test(is_admin)
def manage_notices(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'dashboard/notices.html', {'notices': notices})

@login_required
@user_passes_test(is_admin)
def add_edit_notice(request, pk=None):
    notice = get_object_or_404(Notice, pk=pk) if pk else None
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice saved.')
            return redirect('dashboard:notices')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Notice'})

@login_required
@user_passes_test(is_admin)
def delete_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('dashboard:notices')

# Events
@login_required
@user_passes_test(is_admin)
def manage_events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'dashboard/events.html', {'events': events})

@login_required
@user_passes_test(is_admin)
def add_edit_event(request, pk=None):
    event = get_object_or_404(Event, pk=pk) if pk else None
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard:events')
    else:
        form = EventForm(instance=event)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Event'})

@login_required
@user_passes_test(is_admin)
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('dashboard:events')

# Gallery
@login_required
@user_passes_test(is_admin)
def manage_gallery(request):
    albums = Album.objects.all().order_by('-created_at')
    return render(request, 'dashboard/gallery.html', {'albums': albums})

@login_required
@user_passes_test(is_admin)
def add_edit_album(request, pk=None):
    album = get_object_or_404(Album, pk=pk) if pk else None
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('dashboard:gallery')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Album'})

@login_required
@user_passes_test(is_admin)
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('dashboard:gallery')

# Gallery Photos
@login_required
@user_passes_test(is_admin)
def manage_photos(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'dashboard/gallery_photos.html', {'photos': photos})

@login_required
@user_passes_test(is_admin)
def add_edit_photo(request, pk=None):
    photo = get_object_or_404(Photo, pk=pk) if pk else None
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard:photos')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Photo'})

@login_required
@user_passes_test(is_admin)
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('dashboard:photos')

# Samaj Community links
@login_required
@user_passes_test(is_admin)
def manage_community(request):
    links = SamajCommunity.objects.all().order_by('-created_at')
    return render(request, 'dashboard/community.html', {'links': links})

@login_required
@user_passes_test(is_admin)
def add_edit_community(request, pk=None):
    link = get_object_or_404(SamajCommunity, pk=pk) if pk else None
    if request.method == 'POST':
        form = SamajCommunityForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('dashboard:community')
    else:
        form = SamajCommunityForm(instance=link)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add/Edit Community Link'})

@login_required
@user_passes_test(is_admin)
def delete_community(request, pk):
    link = get_object_or_404(SamajCommunity, pk=pk)
    link.delete()
    return redirect('dashboard:community')

# Members
@login_required
@user_passes_test(is_admin)
def manage_members(request):
    members = User.objects.all().order_by('-date_joined')
    return render(request, 'dashboard/members.html', {'members': members})

@login_required
@user_passes_test(is_admin)
def approve_member(request, pk):
    member = get_object_or_404(User, pk=pk)
    member.is_approved = True
    member.save()
    return redirect('dashboard:members')

@login_required
@user_passes_test(is_admin)
def delete_member(request, pk):
    member = get_object_or_404(User, pk=pk)
    member.delete()
    return redirect('dashboard:members')
