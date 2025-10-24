from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event, Participant

def index(request):
    events = Event.objects.all()

    # Tambah event
    if request.method == 'POST' and 'add_event' in request.POST:
        title = request.POST['title']
        date = request.POST['date']
        location = request.POST['location']
        quota = request.POST['quota']
        Event.objects.create(title=title, date=date, location=location, quota=quota)
        messages.success(request, f"Event '{title}' berhasil ditambahkan!")
        return redirect('/')

    return render(request, 'index.html', {'events': events})


def register(request):
    if request.method == 'POST' and 'register_participant' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        event_name = request.POST['event_name']

        try:
            event = Event.objects.get(title=event_name)
        except Event.DoesNotExist:
            messages.error(request, f"Event '{event_name}' tidak ditemukan.")
            return redirect('/')

        Participant.objects.create(name=name, email=email, event=event)
        messages.success(request, f"Pendaftaran berhasil untuk event '{event.title}'!")
        return redirect('/')


def participants(request, event_id=None):
    if event_id:
        participants = Participant.objects.filter(event_id=event_id)
        try:
            event = Event.objects.get(id=event_id)
            title = f"Peserta untuk Event: {event.title}"
        except Event.DoesNotExist:
            title = "Event tidak ditemukan"
            participants = []
    else:
        participants = Participant.objects.select_related('event').all()
        title = "Daftar Semua Peserta"

    return render(request, 'participants.html', {
        'participants': participants,
        'title': title
    })

