# Portofolio Django — Firman Brilian

Website portofolio satu-halaman (Data Engineer) dibangun dengan Django.
Semua konten (pengalaman, skill, sertifikasi, dll) disimpan di `portfolio/data.py`
sehingga mudah diubah tanpa menyentuh template.

## Struktur

```
portfolio_project/
├── manage.py
├── requirements.txt
├── portfolio_project/       # konfigurasi project (settings, urls, wsgi)
└── portfolio/                # app utama
    ├── data.py                # <- edit CV/konten di sini
    ├── views.py
    ├── urls.py
    ├── templates/portfolio/index.html
    └── static/portfolio/css/style.css
```

## 1. Menjalankan secara lokal

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Buka http://127.0.0.1:8000

## 2. Mengubah isi CV

Buka `portfolio/data.py` dan edit dict/list di sana (nama, pengalaman kerja,
skill, sertifikasi, pendidikan, mentoring, speaking). Template otomatis akan
mengikuti karena menggunakan `{% for %}` loop dari data ini.

## 3. Deploy (hosting gratis/murah)

Django butuh server Python yang berjalan terus — tidak seperti file HTML statis.
Beberapa opsi termudah:

### Opsi A — Railway.app (paling mudah, ada free trial)
1. Push project ini ke repo GitHub.
2. Buat akun di https://railway.app, klik "New Project" → "Deploy from GitHub repo".
3. Railway otomatis mendeteksi Django. Set environment variable:
   - `DJANGO_SECRET_KEY` = (string acak panjang)
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `*.up.railway.app` (atau domain custom kamu)
4. Set start command: `gunicorn portfolio_project.wsgi --log-file -`
5. Sebelum deploy pertama, jalankan `python manage.py collectstatic` (bisa lewat
   Railway's build command) agar file CSS ter-serve oleh whitenoise.

### Opsi B — Render.com (free tier tersedia)
1. Push ke GitHub, buat "New Web Service" di https://render.com dan hubungkan repo.
2. Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
3. Start command: `gunicorn portfolio_project.wsgi`
4. Set environment variables sama seperti di atas.

### Opsi C — PythonAnywhere (gratis, cocok untuk pemula)
1. Upload project via Git atau file manager mereka.
2. Ikuti wizard "Web" → "Manual configuration" → Django, arahkan ke
   `portfolio_project/wsgi.py`.
3. Set virtualenv & `DJANGO_ALLOWED_HOSTS` sesuai subdomain `username.pythonanywhere.com`.

## 4. Sebelum production

- Ganti `DJANGO_SECRET_KEY` dengan string acak yang aman (jangan pakai default di settings.py).
- Set `DJANGO_DEBUG=False`.
- Set `DJANGO_ALLOWED_HOSTS` sesuai domain kamu.
- Jalankan `python manage.py collectstatic` supaya CSS ter-bundle oleh whitenoise.

## Kustomisasi desain

Semua styling ada di satu file: `portfolio/static/portfolio/css/style.css`.
Warna, font, dan layout diatur lewat CSS variables di bagian `:root` paling atas file.
# firman-brilian-portfolio
# firman-brilian-portfolio
