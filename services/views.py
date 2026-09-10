from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service


@login_required
def service_list(request):
    services = Service.objects.all()

    return render(
        request,
        'services/service_list.html',
        {'services': services}
    )


@login_required
def new_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        Service.objects.create(
            name=name,
            description=description,
            price=price,
            status=True
        )

        return redirect('service_list')

    return render(
        request,
        'services/new_service.html'
    )


@login_required
def edit_service(request, service_id):
    service = get_object_or_404(
        Service,
        id=service_id
    )

    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.description = request.POST.get('description')
        service.price = request.POST.get('price')

        service.save()

        return redirect('service_list')

    return render(
        request,
        'services/edit_service.html',
        {'service': service}
    )


@login_required
def delete_service(request, service_id):
    service = get_object_or_404(
        Service,
        id=service_id
    )

    service.delete()

    return redirect('service_list')