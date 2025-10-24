# 🎓 Campus Event Registration Platform
UTS Mata Kuliah: Interoperability  
Nama: Hendra Maulana 
Nim: 2315354020 

---

## 📘 Deskripsi Proyek
Aplikasi web sederhana berbasis **Django** untuk registrasi event kampus.  
Pengguna dapat:
- Melihat daftar event
- Menambahkan event baru
- Mendaftar sebagai peserta
- Melihat daftar peserta tiap event

---

## ⚙️ Teknologi yang Digunakan
- **Backend:** Django 5.x (Python)
- **Database:** SQLite
- **Frontend:** HTML + CSS (native)
- **Tools:** Visual Studio Code, GitHub

---

## 🗃️ Struktur Database
### Tabel `events`
| Kolom | Tipe | Keterangan |
|--------|------|-------------|
| id | INT (PK) | Auto Increment |
| title | VARCHAR(100) | Nama Event |
| date | DATE | Tanggal Event |
| location | VARCHAR(100) | Lokasi Event |
| quota | INT | Kuota peserta |

### Tabel `participants`
| Kolom | Tipe | Keterangan |
|--------|------|-------------|
| id | INT (PK) | Auto Increment |
| name | VARCHAR(100) | Nama Peserta |
| email | VARCHAR(100) | Email Peserta |
| event_id | INT (FK) | Relasi ke Event |

---

## 🚀 Cara Menjalankan Aplikasi
1. Clone repository:
   ```bash
   git clone https://github.com/[username]/Campus_Event_Registration_Platform-[namamu].git
   cd Campus_Event_Registration_Platform-[namamu]
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   http://127.0.0.1:8000/
