from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Participant

# Password admin sederhana
ADMIN_PASSWORD = "admin123"  # bisa kamu ubah

# === Halaman Utama (Tampilkan dan Tambah Event) ===
def index(request):
    events = Event.objects.all()

    # Tambah Event
    if request.method == 'POST' and 'add_event' in request.POST:
        if request.POST.get('admin_pass') != ADMIN_PASSWORD:
            messages.error(request, "❌ Password admin salah.")
            return redirect('/')
        title = request.POST['title']
        date = request.POST['date']
        location = request.POST['location']
        quota = request.POST['quota']
        Event.objects.create(title=title, date=date, location=location, quota=quota)
        messages.success(request, f"✅ Event '{title}' berhasil ditambahkan!")
        return redirect('/')

    return render(request, 'index.html', {'events': events})


# === Pendaftaran Peserta ===
def register(request):
    if request.method == 'POST' and 'register_participant' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        event_name = request.POST['event_name']
        try:
            event = Event.objects.get(title=event_name)
        except Event.DoesNotExist:
            messages.error(request, f"❌ Event '{event_name}' tidak ditemukan.")
            return redirect('/')
        Participant.objects.create(name=name, email=email, event=event)
        messages.success(request, f"✅ Pendaftaran '{name}' ke event '{event.title}' berhasil!")
        return redirect('/')


# === Lihat Semua Peserta ===
def participants(request, event_id=None):
    if event_id:
        participants = Participant.objects.filter(event_id=event_id)
        event = Event.objects.get(id=event_id)
        title = f"Peserta Event: {event.title}"
    else:
        participants = Participant.objects.select_related('event').all()
        title = "Daftar Semua Peserta"
    return render(request, 'participants.html', {'participants': participants, 'title': title})


# === Edit Event ===
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if request.POST.get('admin_pass') != ADMIN_PASSWORD:
            messages.error(request, "❌ Password admin salah.")
            return redirect('/')
        event.title = request.POST['title']
        event.date = request.POST['date']
        event.location = request.POST['location']
        event.quota = request.POST['quota']
        event.save()
        messages.success(request, f"✅ Event '{event.title}' berhasil diperbarui!")
        return redirect('/')
    return render(request, 'edit_event.html', {'event': event})


# === Hapus Event ===
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if request.POST.get('admin_pass') != ADMIN_PASSWORD:
            messages.error(request, "❌ Password admin salah.")
            return redirect('/')
        event.delete()
        messages.success(request, f"🗑️ Event '{event.title}' berhasil dihapus!")
        return redirect('/')
    return render(request, 'delete_event.html', {'event': event})
