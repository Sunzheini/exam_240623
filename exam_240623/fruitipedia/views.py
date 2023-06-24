from django.shortcuts import render, redirect

from exam_240623.fruitipedia.forms import AddProfileForm, AddFruitForm, DeleteProfileForm, DeleteFruitForm, \
    EditProfileForm, EditFruitForm
from exam_240623.fruitipedia.models import Profile, Fruit


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


#  general -------------------------------------------------------

def index(request):
    template = 'core/index.html'
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, template, context)


def dashboard(request):
    template = 'core/dashboard.html'
    profile = get_profile()
    all_fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'all_fruits': all_fruits,
    }
    return render(request, template, context)


#  fruits --------------------------------------------------------

def create_fruit(request):
    template = 'fruits/create-fruit.html'
    profile = get_profile()

    if request.method == 'POST':
        form = AddFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddFruitForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)


def fruit_details(request, pk):
    template = 'fruits/details-fruit.html'
    profile = get_profile()
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'profile': profile,
        'fruit': fruit,
    }
    return render(request, template, context)


def edit_fruit(request, pk):
    template = 'fruits/edit-fruit.html'
    profile = get_profile()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditFruitForm(instance=fruit)

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, template, context)


def delete_fruit(request, pk):
    template = 'fruits/delete-fruit.html'
    profile = get_profile()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    else:
        form = DeleteFruitForm(instance=fruit)

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, template, context)


#  profiles ------------------------------------------------------

def create_profile(request):
    template = 'profiles/create-profile.html'

    if request.method == 'POST':
        form = AddProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddProfileForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def profile_details(request):
    template = 'profiles/details-profile.html'
    profile = get_profile()
    all_fruit_posts = Fruit.objects.all().count()

    if all_fruit_posts == 0:
        all_fruit_posts = None

    context = {
        'profile': profile,
        'all_fruit_posts': all_fruit_posts,
    }
    return render(request, template, context)


def edit_profile(request):
    template = 'profiles/edit-profile.html'
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)


def delete_profile(request):
    template = 'profiles/delete-profile.html'
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)
