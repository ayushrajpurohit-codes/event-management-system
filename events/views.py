from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventType


@login_required
def event_list(request):
    events = Event.objects.select_related('event_type').all()

    return render(
        request,
        'events/event_list.html',
        {'events': events}
    )


@login_required
def new_event(request):
    event_types = EventType.objects.filter(status=True)

    if request.method == 'POST':
        event_type_id = request.POST.get('event_type')
        name = request.POST.get('name')
        description = request.POST.get('description')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        venue = request.POST.get('venue')

        event_type = get_object_or_404(
            EventType,
            id=event_type_id,
            status=True
        )

        Event.objects.create(
            event_type=event_type,
            name=name,
            description=description,
            event_date=event_date,
            event_time=event_time or None,
            venue=venue,
            status=True
        )

        return redirect('event_list')

    return render(
        request,
        'events/new_event.html',
        {'event_types': event_types}
    )


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event_types = EventType.objects.filter(status=True)

    if request.method == 'POST':
        event_type_id = request.POST.get('event_type')

        event.event_type = get_object_or_404(
            EventType,
            id=event_type_id,
            status=True
        )

        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date')
        event.event_time = request.POST.get('event_time') or None
        event.venue = request.POST.get('venue')

        event.save()

        return redirect('event_list')

    return render(
        request,
        'events/edit_event.html',
        {
            'event': event,
            'event_types': event_types,
        }
    )


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()

    return redirect('event_list')


@login_required
def event_type_list(request):
    event_types = EventType.objects.all()

    return render(
        request,
        'events/event_type_list.html',
        {'event_types': event_types}
    )


@login_required
def new_event_type(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        EventType.objects.create(
            name=name,
            description=description,
            status=True
        )

        return redirect('event_type_list')

    return render(
        request,
        'events/new_event_type.html'
    )


@login_required
def edit_event_type(request, event_type_id):
    event_type = get_object_or_404(
        EventType,
        id=event_type_id
    )

    if request.method == 'POST':
        event_type.name = request.POST.get('name')
        event_type.description = request.POST.get('description')
        event_type.save()

        return redirect('event_type_list')

    return render(
        request,
        'events/edit_event_type.html',
        {'event_type': event_type}
    )


@login_required
def delete_event_type(request, event_type_id):
    event_type = get_object_or_404(
        EventType,
        id=event_type_id
    )

    event_type.delete()

    return redirect('event_type_list')