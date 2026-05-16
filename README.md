# 🎓 Sistem Prediksi Kelayakan PIP - SMAN 4 Padang

Aplikasi web untuk memprediksi kelayakan penerima Program Indonesia Pintar (PIP) menggunakan Machine Learning dengan algoritma Naïve Bayes.

## 📋 Persyaratan

- Python 3.7+
- pip (Python package manager)

## 🚀 Instalasi & Menjalankan

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Training Model (Lakukan 1x saja)

```bash
python model_training.py
```

Output yang diharapkan:
```
==================================================
PROSES TRAINING SELESAI!
==================================================

File yang dihasilkan:
  1. model_pip.pkl (Model Naive Bayes)
  2. encoders.pkl (Encoder untuk data)
```

### Step 3: Jalankan Aplikasi Web

```bash
python app.py
```

Buka browser dan akses: **http://localhost:5000**

## 📁 Struktur Folder

```
fazaha/
├── app.py                          # Flask server utama
├── model_training.py               # Script training model
├── requirements.txt                # Daftar library yang diperlukan
├── data_training.csv               # Data untuk training
├── model_pip.pkl                   # Model (auto-generated)
├── encoders.pkl                    # Encoder (auto-generated)
│
├── templates/
│   ├── index.html                  # Halaman prediksi
│   └── informasi.html              # Halaman informasi PIP
│
└── static/
    ├── css/
    │   └── style.css               # Styling website
    └── js/
        └── script.js               # JavaScript interaktif
```

## 🎯 Cara Menggunakan

1. **Buka website** di http://localhost:5000
2. **Isi form** dengan data siswa:
   - Penghasilan Orang Tua
   - Kondisi Rumah
   - Pekerjaan Orang Tua
   - Kepemilikan Rumah
   - Status Ekonomi
   - Penerima KKS
3. **Klik "Prediksi Kelayakan PIP"**
4. **Lihat hasil** dengan detail probabilitas

## 📊 Algoritma yang Digunakan

**Naïve Bayes** - Algoritma probabilistik yang menggunakan Bayes' Theorem:

```
P(Class|Features) = P(Features|Class) × P(Class) / P(Features)
```

Kelebihan:
- ✓ Cepat dan efisien
- ✓ Cocok untuk dataset kecil-menengah
- ✓ Mudah dipahami
- ✓ Hasil akurat untuk klasifikasi

## 📈 Akurasi

Model dilatih dengan 50+ data siswa dan mencapai akurasi **±90%**

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### Error: "model_pip.pkl not found"
```bash
python model_training.py
```

### Error: "Port 5000 already in use"
Ganti port di `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Ubah ke 5001
```

## 📞 Informasi

**Sekolah**: SMAN 4 Padang  
**Mata Pelajaran**: Penerapan Machine Learning  
**Topik**: Prediksi Kelayakan Penerima PIP  
**Algoritma**: Naïve Bayes

## 📝 Catatan

- Data training dapat ditambah/diedit di file `data_training.csv`
- Setelah mengubah data, jalankan `python model_training.py` lagi
- Website dapat diakses dari komputer manapun di jaringan yang sama dengan IP lokal

## ✅ Dibuat oleh

faathiralbar03-maker (2026)