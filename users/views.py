from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def user_list(request):
    users = User.objects.all().order_by('username')

    return render(
        request,
        'users/user_list.html',
        {'users': users}
    )


@login_required
def new_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('new_user')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'User created successfully.')
        return redirect('user_list')

    return render(request, 'users/new_user.html')


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('edit_user', user_id=user.id)

        user.username = username
        user.email = email

        if password:
            user.set_password(password)

        user.save()

        messages.success(request, 'User updated successfully.')
        return redirect('user_list')

    return render(
        request,
        'users/edit_user.html',
        {'user': user}
    )


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.is_superuser:
        messages.error(request, 'Superuser cannot be deleted.')
        return redirect('user_list')

    user.delete()

    messages.success(request, 'User deleted successfully.')
    return redirect('user_list')