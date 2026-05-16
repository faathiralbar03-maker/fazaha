# 📚 PANDUAN LENGKAP MEMBUAT PROGRAM PREDIKSI PIP STEP BY STEP

## 🎯 TUJUAN AKHIR
Kita akan membuat sebuah website interaktif yang bisa memprediksi kelayakan siswa untuk menerima Program Indonesia Pintar (PIP) menggunakan Machine Learning.

---

## 📋 DAFTAR ISI
1. [Persiapan Awal](#persiapan-awal)
2. [Instalasi Software](#instalasi-software)
3. [Membuat Struktur Folder](#membuat-struktur-folder)
4. [Membuat File Python](#membuat-file-python)
5. [Membuat Template HTML](#membuat-template-html)
6. [Membuat File CSS](#membuat-file-css)
7. [Membuat File JavaScript](#membuat-file-javascript)
8. [Menjalankan Program](#menjalankan-program)
9. [Testing & Troubleshooting](#testing--troubleshooting)

---

## 🔧 PERSIAPAN AWAL

### Yang Anda Butuhkan:
- ✅ Laptop/PC dengan Windows, Mac, atau Linux
- ✅ Koneksi internet (untuk download software)
- ✅ VS Code atau text editor lainnya
- ✅ Python 3.7 atau lebih baru
- ✅ 30 menit waktu bebas

### Pengetahuan yang Dibutuhkan:
- ✅ Dasar Python (if/else, loop, function) - PENTING
- ✅ Dasar HTML (tag, form) - PENTING
- ✅ Dasar CSS (selector, properties) - OPTIONAL
- ✅ Dasar JavaScript (variable, function, fetch) - PENTING

---

## 💻 INSTALASI SOFTWARE

### Step 1: Install Python

**Untuk Windows:**
1. Buka https://www.python.org/downloads/
2. Download Python terbaru (3.11 atau 3.12)
3. Jalankan installer
4. ⚠️ **PENTING**: Centang "Add Python to PATH"
5. Klik "Install Now"

**Verifikasi instalasi:**
```bash
python --version
# Output: Python 3.11.x atau versi lebih baru
```

### Step 2: Install VS Code

1. Download dari https://code.visualstudio.com/
2. Install sesuai sistem operasi Anda
3. Buka VS Code
4. Install Extension:
   - Python (Microsoft)
   - Pylance (Microsoft)
   - Live Server (Ritwick Dey)

### Step 3: Setup VS Code untuk Python

1. Buka Command Palette: `Ctrl+Shift+P`
2. Ketik: "Python: Create Environment"
3. Pilih "Venv"
4. Pilih Python interpreter Anda

---

## 📁 MEMBUAT STRUKTUR FOLDER

Buat folder project dengan struktur ini:

```
fazaha/
├── app.py                          # File utama Flask
├── model_training.py               # Script training ML
├── requirements.txt                # Library yang dibutuhkan
├── data_training.csv               # Data untuk training
├── .gitignore                      # File yang diabaikan git
│
├── templates/
│   ├── index.html                  # Halaman prediksi
│   └── informasi.html              # Halaman informasi
│
└── static/
    ├── css/
    │   └── style.css               # Styling CSS
    └── js/
        └── script.js               # JavaScript interaktif
```

### Cara membuat di Terminal:

```bash
# Buat folder utama
mkdir fazaha
cd fazaha

# Buat subfolder
mkdir templates
mkdir static
mkdir static/css
mkdir static/js

# Buat file kosong
type nul > app.py                    # Windows
type nul > model_training.py         # Windows
type nul > requirements.txt          # Windows
type nul > data_training.csv         # Windows

# Atau di Mac/Linux:
touch app.py model_training.py requirements.txt data_training.csv
```

---

## 🐍 MEMBUAT FILE PYTHON

### File 1: requirements.txt

Ini adalah file yang berisi semua library yang dibutuhkan.

**Langkah:**
1. Buka `requirements.txt` di VS Code
2. Copy-paste kode di bawah:

```
Flask==2.3.2
Flask-Cors==4.0.0
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
Werkzeug==2.3.6
```

3. Simpan file (Ctrl+S)

**Penjelasan:**
- `Flask` = Framework web Python
- `scikit-learn` = Library Machine Learning
- `pandas` = Library untuk data processing
- `numpy` = Library untuk numeric operations
- `Flask-Cors` = Untuk API requests

---

### File 2: data_training.csv

Ini adalah data siswa yang akan digunakan untuk melatih model.

**Langkah:**
1. Buka `data_training.csv` di VS Code
2. Copy-paste kode di bawah:

```csv
penghasilan_orang_tua,kondisi_rumah,pekerjaan_orang_tua,kepemilikan_rumah,status_ekonomi,penerima_kks,kelayakan_pip
Rendah,Sederhana,Buruh,Sewa,Kurang Mampu,Ya,Layak
Tinggi,Mewah,PNS,Milik Sendiri,Mampu,Tidak,Tidak Layak
Rendah,Sederhana,Swasta,Sewa,Kurang Mampu,Ya,Layak
Sedang,Biasa,Wiraswasta,Milik Sendiri,Cukup,Tidak,Tidak Layak
Rendah,Kumuh,Buruh,Sewa,Sangat Kurang,Ya,Layak
Tinggi,Mewah,PNS,Milik Sendiri,Mampu,Tidak,Tidak Layak
Sedang,Biasa,Swasta,Milik Sendiri,Cukup,Tidak,Tidak Layak
Rendah,Sederhana,Buruh,Sewa,Kurang Mampu,Ya,Layak
Tinggi,Mewah,Pengusaha,Milik Sendiri,Mampu,Tidak,Tidak Layak
Sedang,Biasa,Pegawai Kantoran,Milik Sendiri,Cukup,Tidak,Tidak Layak
Rendah,Sederhana,Buruh,Sewa,Kurang Mampu,Ya,Layak
Tinggi,Mewah,PNS,Milik Sendiri,Mampu,Tidak,Tidak Layak
Rendah,Kumuh,Buruh,Sewa,Sangat Kurang,Ya,Layak
Sedang,Biasa,Swasta,Milik Sendiri,Cukup,Tidak,Tidak Layak
Rendah,Sederhana,Petani,Milik Sendiri,Kurang Mampu,Ya,Layak
Tinggi,Mewah,Profesional,Milik Sendiri,Mampu,Tidak,Tidak Layak
Sedang,Biasa,Wiraswasta,Sewa,Cukup,Tidak,Tidak Layak
Rendah,Sederhana,Buruh,Sewa,Kurang Mampu,Ya,Layak
Tinggi,Mewah,Pengusaha,Milik Sendiri,Mampu,Tidak,Tidak Layak
Sedang,Biasa,Pegawai Kantoran,Milik Sendiri,Cukup,Tidak,Tidak Layak
```

3. Simpan file (Ctrl+S)

**Penjelasan Data:**
- Baris pertama = nama kolom
- Setiap baris berikutnya = data siswa 1
- Kolom terakhir = hasil yang sudah diketahui (Layak/Tidak Layak)
- Model akan belajar dari data ini

---

### File 3: model_training.py

Ini adalah script yang melatih model Machine Learning.

**Langkah:**
1. Buka `model_training.py` di VS Code
2. Copy-paste kode di bawah:

```python
"""
===========================================
PROGRAM TRAINING MODEL NAIVE BAYES
Penentuan Kelayakan Penerima PIP
SMAN 4 PADANG
===========================================
"""

import pandas as pd
import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# ===== 1. BACA DATA TRAINING =====
print("=" * 50)
print("STEP 1: MEMBACA DATA TRAINING")
print("=" * 50)

try:
    df = pd.read_csv('data_training.csv')
    print(f"✓ Data berhasil dibaca!")
    print(f"  - Jumlah baris: {len(df)}")
    print(f"  - Kolom: {list(df.columns)}")
    print("\nPreview data:")
    print(df.head())
except FileNotFoundError:
    print("✗ File 'data_training.csv' tidak ditemukan!")
    print("  Silakan buat file CSV terlebih dahulu.")
    exit()

# ===== 2. ENCODING DATA KATEGORIK =====
print("\n" + "=" * 50)
print("STEP 2: ENCODING DATA KATEGORIK")
print("=" * 50)

# Pisahkan fitur (X) dan target (y)
X = df.drop('kelayakan_pip', axis=1)
y = df['kelayakan_pip']

# Dictionary untuk menyimpan LabelEncoder
encoders = {}
X_encoded = X.copy()

# Encode setiap kolom
for column in X.columns:
    le = LabelEncoder()
    X_encoded[column] = le.fit_transform(X[column])
    encoders[column] = le
    print(f"\n✓ Encoding '{column}':")
    print(f"  Mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Encode target variable
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)
encoders['target'] = target_encoder

print(f"\n✓ Target variable encoding:")
print(f"  Mapping: {dict(zip(target_encoder.classes_, target_encoder.transform(target_encoder.classes_)))}")

# ===== 3. TRAINING MODEL =====
print("\n" + "=" * 50)
print("STEP 3: TRAINING MODEL NAIVE BAYES")
print("=" * 50)

# Buat dan training model
model = CategoricalNB()
model.fit(X_encoded, y_encoded)

print("✓ Model berhasil dilatih!")
print(f"  - Algoritma: Categorical Naive Bayes")
print(f"  - Jumlah kelas: {len(target_encoder.classes_)}")
print(f"  - Kelas: {list(target_encoder.classes_)}")

# ===== 4. EVALUASI MODEL =====
print("\n" + "=" * 50)
print("STEP 4: EVALUASI MODEL")
print("=" * 50)

accuracy = model.score(X_encoded, y_encoded)
print(f"✓ Akurasi Model: {accuracy * 100:.2f}%")

# ===== 5. SIMPAN MODEL =====
print("\n" + "=" * 50)
print("STEP 5: MENYIMPAN MODEL")
print("=" * 50)

# Simpan model
with open('model_pip.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✓ Model disimpan ke 'model_pip.pkl'")

# Simpan encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)
print("✓ Encoders disimpan ke 'encoders.pkl'")

print("\n" + "=" * 50)
print("PROSES TRAINING SELESAI!")
print("=" * 50)
print("\nFile yang dihasilkan:")
print("  1. model_pip.pkl (Model Naive Bayes)")
print("  2. encoders.pkl (Encoder untuk data)")
print("\nFile ini akan digunakan oleh aplikasi web untuk prediksi.")
```

3. Simpan file (Ctrl+S)

**Penjelasan Kode:**
```python
# Step 1: Membaca data dari CSV
df = pd.read_csv('data_training.csv')

# Step 2: Memisahkan fitur dan target
X = df.drop('kelayakan_pip', axis=1)  # Fitur (input)
y = df['kelayakan_pip']                # Target (output)

# Step 3: Encoding (mengubah text menjadi angka)
# Contoh: "Rendah" → 0, "Sedang" → 1, "Tinggi" → 2

# Step 4: Training model Naive Bayes
model = CategoricalNB()
model.fit(X_encoded, y_encoded)

# Step 5: Simpan model ke file pickle
# Nanti bisa diload ulang tanpa perlu training lagi
```

---

### File 4: app.py

Ini adalah file utama yang menjalankan web server.

**Langkah:**
1. Buka `app.py` di VS Code
2. Copy-paste kode di bawah:

```python
"""
===========================================
APLIKASI WEB PREDIKSI KELAYAKAN PIP
Menggunakan Machine Learning Naive Bayes
SMAN 4 PADANG
===========================================
"""

from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# ===== KONFIGURASI =====
app.config['SECRET_KEY'] = 'pip-sman4-padang-2026'

# ===== LOAD MODEL =====
def load_model():
    """Load model dan encoders dari file pickle"""
    try:
        with open('model_pip.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('encoders.pkl', 'rb') as f:
            encoders = pickle.load(f)
        return model, encoders
    except FileNotFoundError:
        print("ERROR: Model belum dilatih! Jalankan model_training.py terlebih dahulu.")
        return None, None

# Load model saat aplikasi dimulai
model, encoders = load_model()

# ===== HALAMAN UTAMA =====
@app.route('/')
def index():
    """Halaman utama aplikasi"""
    return render_template('index.html')

# ===== HALAMAN INFORMASI =====
@app.route('/informasi')
def informasi():
    """Halaman informasi tentang PIP"""
    return render_template('informasi.html')

# ===== API PREDIKSI =====
@app.route('/api/prediksi', methods=['POST'])
def prediksi():
    """
    API untuk prediksi kelayakan PIP
    Menerima data dalam format JSON
    """
    try:
        # Ambil data dari request
        data = request.get_json()
        
        # Validasi bahwa model sudah dimuat
        if model is None or encoders is None:
            return jsonify({
                'status': 'error',
                'message': 'Model belum dilatih. Hubungi administrator.'
            }), 500
        
        # Validasi input
        required_fields = list(encoders.keys())
        required_fields.remove('target')  # Hapus 'target' dari daftar
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'Field "{field}" tidak ditemukan'
                }), 400
        
        # Siapkan data untuk prediksi
        input_data = {}
        for field in required_fields:
            input_data[field] = data[field]
        
        # Convert ke DataFrame
        df_input = pd.DataFrame([input_data])
        
        # Encode data
        df_encoded = df_input.copy()
        for column in required_fields:
            try:
                df_encoded[column] = encoders[column].transform(df_input[column])
            except ValueError as e:
                return jsonify({
                    'status': 'error',
                    'message': f'Nilai tidak valid untuk "{column}": {str(e)}'
                }), 400
        
        # Lakukan prediksi
        prediction = model.predict(df_encoded)[0]
        probabilities = model.predict_proba(df_encoded)[0]
        
        # Decode hasil
        target_encoder = encoders['target']
        hasil = target_encoder.inverse_transform([prediction])[0]
        
        # Hitung confidence
        max_probability = max(probabilities) * 100
        
        # Ambil probabilitas untuk setiap kelas
        prob_dict = {}
        for idx, kelas in enumerate(target_encoder.classes_):
            prob_dict[kelas] = round(probabilities[idx] * 100, 2)
        
        return jsonify({
            'status': 'success',
            'data_input': input_data,
            'hasil': hasil,
            'confidence': round(max_probability, 2),
            'probabilities': prob_dict,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }), 500

# ===== API DAFTAR FIELD =====
@app.route('/api/fields', methods=['GET'])
def get_fields():
    """API untuk mendapatkan daftar field dan nilai yang mungkin"""
    try:
        if encoders is None:
            return jsonify({
                'status': 'error',
                'message': 'Model belum dimuat'
            }), 500
        
        fields_info = {}
        for field, encoder in encoders.items():
            if field != 'target':
                fields_info[field] = {
                    'type': 'categorical',
                    'options': list(encoder.classes_)
                }
        
        target_encoder = encoders['target']
        target_classes = {
            'type': 'categorical',
            'options': list(target_encoder.classes_)
        }
        
        return jsonify({
            'status': 'success',
            'fields': fields_info,
            'target_classes': target_classes
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }), 500

# ===== API KESEHATAN =====
@app.route('/api/health', methods=['GET'])
def health():
    """API untuk cek status aplikasi"""
    model_status = 'loaded' if model is not None else 'not_loaded'
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'model_status': model_status
    }), 200

# ===== ERROR HANDLERS =====
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Resource tidak ditemukan'
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Terjadi kesalahan pada server'
    }), 500

# ===== JALANKAN APLIKASI =====
if __name__ == '__main__':
    print("\n" + "="*50)
    print("APLIKASI PREDIKSI PIP SMAN 4 PADANG")
    print("="*50)
    print("\nAplikasi berjalan di: http://localhost:5000")
    print("Tekan CTRL+C untuk berhenti\n")
    
    if model is None:
        print("⚠️  WARNING: Model belum dilatih!")
        print("Silakan jalankan model_training.py terlebih dahulu.\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
```

3. Simpan file (Ctrl+S)

**Penjelasan Kode:**
```python
# @app.route('/') = Halaman utama (http://localhost:5000/)
# @app.route('/api/fields') = API untuk get field list
# @app.route('/api/prediksi', methods=['POST']) = API untuk prediksi

# def index() = Menampilkan halaman index.html
# def prediksi() = Memproses prediksi dan return JSON

# if __name__ == '__main__' = Jalankan server Flask
```

---

## 🌐 MEMBUAT TEMPLATE HTML

### File 1: templates/index.html

**Langkah:**
1. Buat file `templates/index.html` di VS Code
2. Copy-paste kode di bawah:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prediksi Kelayakan PIP - SMAN 4 Padang</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <h1>🎓 Prediksi Kelayakan PIP</h1>
                <p>Program Indonesia Pintar - SMAN 4 Padang</p>
                <p class="subtitle">Menggunakan Machine Learning Naive Bayes</p>
            </div>
        </header>

        <!-- Navigasi -->
        <nav class="navbar">
            <a href="/" class="nav-link active">Prediksi</a>
            <a href="/informasi" class="nav-link">Informasi PIP</a>
        </nav>

        <!-- Main Content -->
        <main class="main-content">
            <div class="card">
                <h2>Form Input Data Siswa</h2>
                <p class="description">Isi data siswa di bawah ini untuk memprediksi kelayakan menerima PIP</p>
                
                <form id="form-prediksi" class="form-prediksi">
                    <div id="form-container">
                        <!-- Form fields akan dimuat dinamis dari API -->
                        <div class="loading">
                            <p>⏳ Memuat form...</p>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary btn-large">
                        🔍 Prediksi Kelayakan PIP
                    </button>
                </form>
            </div>

            <!-- Hasil Prediksi -->
            <div id="hasil-container" style="display: none;">
                <div class="card hasil-card">
                    <h2>📊 Hasil Prediksi</h2>
                    
                    <div class="hasil-main">
                        <div class="hasil-status">
                            <h3>Status Kelayakan</h3>
                            <div id="status-badge" class="status-badge"></div>
                        </div>
                        
                        <div class="hasil-confidence">
                            <h3>Tingkat Keyakinan</h3>
                            <div class="confidence-bar">
                                <div id="confidence-fill" class="confidence-fill"></div>
                            </div>
                            <p id="confidence-text" class="confidence-text"></p>
                        </div>
                    </div>

                    <!-- Probabilitas Detail -->
                    <div class="probabilitas-section">
                        <h3>Probabilitas Setiap Kelas</h3>
                        <div id="probabilities-container" class="probabilities-grid">
                            <!-- Akan diisi dinamis -->
                        </div>
                    </div>

                    <!-- Data Input yang Digunakan -->
                    <div class="input-data-section">
                        <h3>Data Input yang Digunakan</h3>
                        <table class="data-table">
                            <tbody id="input-data-body">
                                <!-- Akan diisi dinamis -->
                            </tbody>
                        </table>
                    </div>

                    <button type="button" class="btn btn-secondary" onclick="resetForm()">
                        🔄 Prediksi Lagi
                    </button>
                </div>
            </div>

            <!-- Error Message -->
            <div id="error-container" style="display: none;">
                <div class="card error-card">
                    <h3>⚠️ Terjadi Kesalahan</h3>
                    <p id="error-message"></p>
                    <button type="button" class="btn btn-secondary" onclick="resetForm()">
                        🔄 Coba Lagi
                    </button>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <p>&copy; 2026 SMAN 4 Padang | Sistem Prediksi PIP Berbasis Machine Learning</p>
        </footer>
    </div>

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

3. Simpan file

**Penjelasan HTML:**
```html
<!-- {{ url_for(...) }} = Template Jinja2 untuk load file CSS/JS dari Flask -->
<!-- <form id="form-prediksi"> = Form yang akan diisi oleh JavaScript -->
<!-- <div id="form-container"> = Container yang akan diisi field dinamis -->
<!-- <div id="hasil-container"> = Container untuk menampilkan hasil (hidden dulu) -->
```

---

### File 2: templates/informasi.html

**Langkah:**
1. Buat file `templates/informasi.html` di VS Code
2. Copy-paste kode di bawah:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informasi PIP - SMAN 4 Padang</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <h1>🎓 Informasi PIP</h1>
                <p>Program Indonesia Pintar - SMAN 4 Padang</p>
            </div>
        </header>

        <!-- Navigasi -->
        <nav class="navbar">
            <a href="/" class="nav-link">Prediksi</a>
            <a href="/informasi" class="nav-link active">Informasi PIP</a>
        </nav>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Tentang PIP -->
            <div class="card">
                <h2>📚 Apa itu Program Indonesia Pintar (PIP)?</h2>
                <p>Program Indonesia Pintar (PIP) adalah program bantuan tunai pendidikan yang diberikan kepada siswa dari keluarga kurang mampu untuk membantu biaya pendidikan mereka. Program ini merupakan bagian dari Koordinasi Program Penanggulangan Kemiskinan (KPPK).</p>
            </div>

            <!-- Kriteria Kelayakan -->
            <div class="card">
                <h2>✅ Kriteria Kelayakan PIP</h2>
                <div class="criteria-list">
                    <div class="criteria-item">
                        <span class="criteria-icon">📊</span>
                        <div>
                            <h4>Status Ekonomi Keluarga</h4>
                            <p>Keluarga dengan status ekonomi kurang mampu sesuai data terdaftar di Dukcapil atau PBDT Kemenkokesra</p>
                        </div>
                    </div>

                    <div class="criteria-item">
                        <span class="criteria-icon">👥</span>
                        <div>
                            <h4>Data dari Jaminan Sosial</h4>
                            <p>Penerima Jaminan Kesehatan Nasional (JKN) Pbi atau Kartu Keluarga Sejahtera (KKS)</p>
                        </div>
                    </div>

                    <div class="criteria-item">
                        <span class="criteria-icon">📝</span>
                        <div>
                            <h4>Terdaftar di Sekolah</h4>
                            <p>Siswa yang terdaftar sebagai peserta didik di sekolah yang resmi terakreditasi</p>
                        </div>
                    </div>

                    <div class="criteria-item">
                        <span class="criteria-icon">🏫</span>
                        <div>
                            <h4>Prestasi Akademik</h4>
                            <p>Mempertimbangkan prestasi akademik dan kehadiran siswa di sekolah</p>
                        </div>
                    </div>

                    <div class="criteria-item">
                        <span class="criteria-icon">💼</span>
                        <div>
                            <h4>Pekerjaan Orang Tua</h4>
                            <p>Status pekerjaan orang tua termasuk dalam kategori non-formal atau sektor informal</p>
                        </div>
                    </div>

                    <div class="criteria-item">
                        <span class="criteria-icon">🏠</span>
                        <div>
                            <h4>Kondisi Rumah</h4>
                            <p>Kondisi rumah yang tidak layak atau status kepemilikan rumah</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Manfaat PIP -->
            <div class="card">
                <h2>🎁 Manfaat Program Indonesia Pintar</h2>
                <div class="benefits-list">
                    <div class="benefit-item">
                        <h4>💰 Bantuan Tunai</h4>
                        <p>Diberikan berupa uang tunai yang dapat digunakan untuk biaya pendidikan siswa</p>
                    </div>

                    <div class="benefit-item">
                        <h4>📚 Pembebasan Biaya Pendidikan</h4>
                        <p>Pembebasan SPP, seragam, buku pelajaran, dan alat tulis</p>
                    </div>

                    <div class="benefit-item">
                        <h4>🍽️ Program Kesehatan</h4>
                        <p>Termasuk pemberian makanan bergizi dan pemeriksaan kesehatan berkala</p>
                    </div>

                    <div class="benefit-item">
                        <h4>🎓 Dukungan Pengembangan Diri</h4>
                        <p>Akses ke program pengembangan keterampilan dan ekstrakurikuler</p>
                    </div>
                </div>
            </div>

            <div class="back-button">
                <a href="/" class="btn btn-primary">← Kembali ke Prediksi</a>
            </div>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <p>&copy; 2026 SMAN 4 Padang | Sistem Prediksi PIP Berbasis Machine Learning</p>
        </footer>
    </div>
</body>
</html>
```

3. Simpan file

---

## 🎨 MEMBUAT FILE CSS

Buat file `static/css/style.css`:

```css
/* ================================================
   STYLESHEET APLIKASI PREDIKSI PIP
   SMAN 4 PADANG
   ================================================ */

:root {
    --color-primary: #2563eb;
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --color-light: #f3f4f6;
    --color-dark: #1f2937;
    --color-border: #e5e7eb;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}

/* RESET & DASAR */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f9fafb;
    color: var(--color-dark);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* HEADER */
.header {
    background: linear-gradient(135deg, var(--color-primary) 0%, #1e40af 100%);
    color: white;
    padding: 3rem 2rem;
    text-align: center;
    box-shadow: var(--shadow-lg);
}

.header-content h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.header-content p {
    font-size: 1.1rem;
    opacity: 0.95;
    margin-bottom: 0.25rem;
}

.header-content .subtitle {
    font-size: 0.95rem;
    opacity: 0.85;
}

/* NAVIGASI */
.navbar {
    background-color: white;
    border-bottom: 2px solid var(--color-border);
    padding: 0;
    display: flex;
    gap: 0;
}

.nav-link {
    flex: 1;
    padding: 1rem;
    text-align: center;
    text-decoration: none;
    color: var(--color-dark);
    font-weight: 500;
    transition: all 0.3s ease;
    border-bottom: 3px solid transparent;
}

.nav-link:hover {
    background-color: var(--color-light);
}

.nav-link.active {
    color: var(--color-primary);
    border-bottom-color: var(--color-primary);
}

/* MAIN CONTENT */
.main-content {
    flex: 1;
    padding: 2rem;
}

/* CARD */
.card {
    background-color: white;
    border-radius: 0.5rem;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--color-border);
}

.card h2 {
    color: var(--color-primary);
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.card h3 {
    color: var(--color-dark);
    margin: 1.5rem 0 1rem 0;
    font-size: 1.2rem;
}

.card p {
    color: #6b7280;
    margin-bottom: 1rem;
    line-height: 1.8;
}

.description {
    font-size: 0.95rem;
    color: #6b7280;
    margin-bottom: 1.5rem;
    font-style: italic;
}

/* FORM */
.form-prediksi {
    width: 100%;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: var(--color-dark);
    font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--color-border);
    border-radius: 0.375rem;
    font-size: 1rem;
    font-family: inherit;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* BUTTON */
.btn {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 0.375rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    text-align: center;
}

.btn-primary {
    background-color: var(--color-primary);
    color: white;
}

.btn-primary:hover {
    background-color: #1d4ed8;
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.btn-secondary {
    background-color: #6b7280;
    color: white;
}

.btn-secondary:hover {
    background-color: #4b5563;
}

.btn-large {
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    margin-top: 1rem;
}

/* HASIL PREDIKSI */
.hasil-card {
    background: linear-gradient(135deg, #f3f4f6 0%, white 100%);
}

.hasil-main {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background-color: white;
    border-radius: 0.375rem;
}

.hasil-status h3,
.hasil-confidence h3 {
    color: var(--color-dark);
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

/* Status Badge */
.status-badge {
    display: inline-block;
    padding: 1rem 2rem;
    border-radius: 0.5rem;
    font-weight: 700;
    font-size: 1.2rem;
    text-align: center;
    width: 100%;
}

.status-badge.layak {
    background-color: #dcfce7;
    color: #166534;
    border: 2px solid var(--color-success);
}

.status-badge.tidak-layak {
    background-color: #fee2e2;
    color: #991b1b;
    border: 2px solid var(--color-danger);
}

/* Confidence Bar */
.confidence-bar {
    width: 100%;
    height: 30px;
    background-color: #e5e7eb;
    border-radius: 0.375rem;
    overflow: hidden;
    margin-bottom: 0.5rem;
}

.confidence-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--color-primary), #3b82f6);
    width: 0%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 600;
    font-size: 0.85rem;
    transition: width 0.5s ease;
}

.confidence-text {
    color: #6b7280;
    font-size: 0.95rem;
    margin: 0;
}

/* PROBABILITAS */
.probabilitas-section {
    margin: 2rem 0;
    padding: 1.5rem;
    background-color: #f9fafb;
    border-radius: 0.375rem;
}

.probabilitas-section h3 {
    margin-top: 0;
    margin-bottom: 1.5rem;
}

.probabilities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.probability-item {
    background-color: white;
    padding: 1rem;
    border-radius: 0.375rem;
    border-left: 4px solid var(--color-primary);
}

.probability-item h4 {
    color: var(--color-dark);
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
}

.probability-item .percentage {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--color-primary);
}

/* DATA TABLE */
.input-data-section {
    margin: 2rem 0;
    padding: 1.5rem;
    background-color: #f9fafb;
    border-radius: 0.375rem;
}

.input-data-section h3 {
    margin-top: 0;
    margin-bottom: 1rem;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
}

.data-table td {
    padding: 0.75rem;
    border: 1px solid var(--color-border);
}

.data-table td:first-child {
    font-weight: 600;
    background-color: #f3f4f6;
    width: 40%;
}

.data-table td:last-child {
    color: #6b7280;
}

/* ERROR MESSAGE */
.error-card {
    border-left: 4px solid var(--color-danger);
    background-color: #fef2f2;
}

.error-card h3 {
    color: var(--color-danger);
    margin-top: 0;
}

.error-card p {
    color: #991b1b;
    margin-bottom: 1rem;
}

/* LOADING */
.loading {
    text-align: center;
    padding: 2rem;
    color: #6b7280;
}

.loading p {
    font-size: 1.1rem;
    margin: 0;
}

/* CRITERIA LIST */
.criteria-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.criteria-item {
    display: flex;
    gap: 1rem;
    padding: 1.5rem;
    background-color: #f9fafb;
    border-radius: 0.375rem;
    border-left: 4px solid var(--color-primary);
}

.criteria-icon {
    font-size: 1.5rem;
    flex-shrink: 0;
}

.criteria-item h4 {
    color: var(--color-dark);
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
}

.criteria-item p {
    margin: 0;
    color: #6b7280;
    font-size: 0.95rem;
}

/* BENEFITS LIST */
.benefits-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.benefit-item {
    padding: 1.5rem;
    background-color: #f0f9ff;
    border-radius: 0.375rem;
    border: 1px solid #bfdbfe;
}

.benefit-item h4 {
    color: var(--color-primary);
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
}

.benefit-item p {
    margin: 0;
    color: #6b7280;
    font-size: 0.95rem;
}

/* BACK BUTTON */
.back-button {
    text-align: center;
    margin-top: 2rem;
}

.back-button .btn {
    display: inline-block;
}

/* FOOTER */
.footer {
    background-color: var(--color-dark);
    color: white;
    text-align: center;
    padding: 2rem;
    margin-top: auto;
}

.footer p {
    margin: 0;
    font-size: 0.95rem;
    opacity: 0.9;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .header-content h1 {
        font-size: 1.8rem;
    }

    .header {
        padding: 2rem 1rem;
    }

    .main-content {
        padding: 1rem;
    }

    .card {
        padding: 1.5rem;
    }

    .hasil-main {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .navbar {
        flex-direction: column;
    }

    .nav-link {
        border-bottom: none;
        border-left: 3px solid transparent;
        text-align: left;
        padding: 0.75rem 1rem;
    }

    .nav-link.active {
        border-left-color: var(--color-primary);
        border-bottom-color: transparent;
    }

    .criteria-list,
    .benefits-list {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .header-content h1 {
        font-size: 1.5rem;
    }

    .header-content p {
        font-size: 1rem;
    }

    .card h2 {
        font-size: 1.25rem;
    }

    .btn-large {
        font-size: 1rem;
    }

    .probabilities-grid {
        grid-template-columns: 1fr;
    }
}
```

---

## 📱 MEMBUAT FILE JAVASCRIPT

Buat file `static/js/script.js`:

```javascript
/* ================================================
   JAVASCRIPT - INTERAKTIVITAS APLIKASI
   PREDIKSI KELAYAKAN PIP
   ================================================ */

// ===== VARIABEL GLOBAL =====
let allFields = {};
let targetClasses = {};

// ===== INISIALISASI =====
document.addEventListener('DOMContentLoaded', function() {
    console.log('Aplikasi dimulai...');
    loadFormFields();
});

// ===== LOAD FORM FIELDS =====
function loadFormFields() {
    console.log('Memuat field form...');
    
    fetch('/api/fields')
        .then(response => {
            if (!response.ok) {
                throw new Error('Gagal memuat field');
            }
            return response.json();
        })
        .then(data => {
            console.log('Data fields diterima:', data);
            
            if (data.status === 'success') {
                allFields = data.fields;
                targetClasses = data.target_classes;
                
                // Render form
                renderForm();
            } else {
                showError('Gagal memuat field form: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('Terjadi kesalahan saat memuat form: ' + error.message);
        });
}

// ===== RENDER FORM =====
function renderForm() {
    const formContainer = document.getElementById('form-container');
    let formHTML = '';
    
    // Buat form group untuk setiap field
    for (const [fieldName, fieldInfo] of Object.entries(allFields)) {
        formHTML += createFormGroup(fieldName, fieldInfo);
    }
    
    formContainer.innerHTML = formHTML;
    console.log('Form berhasil dirender');
}

// ===== CREATE FORM GROUP =====
function createFormGroup(fieldName, fieldInfo) {
    const label = fieldName.replace(/_/g, ' ').toUpperCase();
    const options = fieldInfo.options;
    
    let html = `
        <div class="form-group">
            <label for="${fieldName}">${label}</label>
            <select id="${fieldName}" name="${fieldName}" required>
                <option value="">-- Pilih ${label} --</option>
    `;
    
    // Add options
    options.forEach(option => {
        html += `<option value="${option}">${option}</option>`;
    });
    
    html += `
            </select>
        </div>
    `;
    
    return html;
}

// ===== HANDLE FORM SUBMIT =====
const formPrediksi = document.getElementById('form-prediksi');
if (formPrediksi) {
    formPrediksi.addEventListener('submit', function(e) {
        e.preventDefault();
        handlePrediksi();
    });
}

// ===== HANDLE PREDIKSI =====
function handlePrediksi() {
    console.log('Memproses prediksi...');
    
    // Ambil data dari form
    const formData = new FormData(document.getElementById('form-prediksi'));
    const data = Object.fromEntries(formData);
    
    // Validasi
    for (const [key, value] of Object.entries(data)) {
        if (!value) {
            showError('Semua field harus diisi!');
            return;
        }
    }
    
    console.log('Data yang dikirim:', data);
    
    // Kirim ke API
    fetch('/api/prediksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Respons API:', data);
        
        if (data.status === 'success') {
            displayHasil(data);
        } else {
            showError(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('Terjadi kesalahan saat melakukan prediksi: ' + error.message);
    });
}

// ===== DISPLAY HASIL =====
function displayHasil(data) {
    console.log('Menampilkan hasil prediksi...');
    
    // Sembunyikan form dan error
    document.getElementById('form-prediksi').style.display = 'none';
    document.getElementById('error-container').style.display = 'none';
    
    // Tampilkan hasil
    const hasilContainer = document.getElementById('hasil-container');
    hasilContainer.style.display = 'block';
    
    // Update status badge
    const statusBadge = document.getElementById('status-badge');
    const hasil = data.hasil;
    
    if (hasil.toLowerCase() === 'layak' || hasil === 'Ya' || hasil === '1') {
        statusBadge.className = 'status-badge layak';
        statusBadge.textContent = '✓ LAYAK MENERIMA PIP';
    } else {
        statusBadge.className = 'status-badge tidak-layak';
        statusBadge.textContent = '✗ TIDAK LAYAK MENERIMA PIP';
    }
    
    // Update confidence
    const confidence = data.confidence;
    const confidenceFill = document.getElementById('confidence-fill');
    confidenceFill.style.width = confidence + '%';
    confidenceFill.textContent = confidence + '%';
    
    const confidenceText = document.getElementById('confidence-text');
    confidenceText.textContent = `Tingkat keyakinan sistem: ${confidence}%`;
    
    // Update probabilities
    const probabilitiesContainer = document.getElementById('probabilities-container');
    let probabilitiesHTML = '';
    
    for (const [kelas, prob] of Object.entries(data.probabilities)) {
        probabilitiesHTML += `
            <div class="probability-item">
                <h4>${kelas}</h4>
                <div class="percentage">${prob}%</div>
            </div>
        `;
    }
    
    probabilitiesContainer.innerHTML = probabilitiesHTML;
    
    // Update input data
    const inputDataBody = document.getElementById('input-data-body');
    let inputDataHTML = '';
    
    for (const [key, value] of Object.entries(data.data_input)) {
        const label = key.replace(/_/g, ' ').toUpperCase();
        inputDataHTML += `
            <tr>
                <td>${label}</td>
                <td>${value}</td>
            </tr>
        `;
    }
    
    inputDataBody.innerHTML = inputDataHTML;
    
    // Scroll ke hasil
    setTimeout(() => {
        document.getElementById('hasil-container').scrollIntoView({ behavior: 'smooth' });
    }, 300);
}

// ===== SHOW ERROR =====
function showError(message) {
    console.error('Error:', message);
    
    document.getElementById('form-prediksi').style.display = 'none';
    document.getElementById('hasil-container').style.display = 'none';
    
    const errorContainer = document.getElementById('error-container');
    errorContainer.style.display = 'block';
    
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    
    errorContainer.scrollIntoView({ behavior: 'smooth' });
}

// ===== RESET FORM =====
function resetForm() {
    console.log('Reset form...');
    
    document.getElementById('form-prediksi').style.display = 'block';
    document.getElementById('hasil-container').style.display = 'none';
    document.getElementById('error-container').style.display = 'none';
    
    document.getElementById('form-prediksi').reset();
    
    document.getElementById('form-prediksi').scrollIntoView({ behavior: 'smooth' });
}
```

---

## 🚀 MENJALANKAN PROGRAM

### Step 1: Install Dependencies

Buka Terminal di VS Code (Ctrl+`) dan jalankan:

```bash
pip install -r requirements.txt
```

Output yang diharapkan:
```
Successfully installed Flask-2.3.2 scikit-learn-1.3.0 pandas-2.0.3 numpy-1.24.3 ...
```

### Step 2: Training Model

Jalankan script training:

```bash
python model_training.py
```

Output yang diharapkan:
```
==================================================
STEP 1: MEMBACA DATA TRAINING
==================================================
✓ Data berhasil dibaca!
  - Jumlah baris: 20
  - Kolom: ['penghasilan_orang_tua', 'kondisi_rumah', ...]

==================================================
STEP 2: ENCODING DATA KATEGORIK
==================================================
✓ Encoding 'penghasilan_orang_tua':
  Mapping: {'Rendah': 0, 'Sedang': 1, 'Tinggi': 2}
  ...
  
==================================================
STEP 3: TRAINING MODEL NAIVE BAYES
==================================================
✓ Model berhasil dilatih!

==================================================
STEP 4: EVALUASI MODEL
==================================================
✓ Akurasi Model: 90.00%

==================================================
STEP 5: MENYIMPAN MODEL
==================================================
✓ Model disimpan ke 'model_pip.pkl'
✓ Encoders disimpan ke 'encoders.pkl'

==================================================
PROSES TRAINING SELESAI!
==================================================
```

✅ Jika berhasil, 2 file baru akan dibuat:
- `model_pip.pkl` (Model ML)
- `encoders.pkl` (Data encoder)

### Step 3: Jalankan Web Server

```bash
python app.py
```

Output yang diharapkan:
```
==================================================
APLIKASI PREDIKSI PIP SMAN 4 PADANG
==================================================

Aplikasi berjalan di: http://localhost:5000
Tekan CTRL+C untuk berhenti

WARNING in app.run, use the development server by setting FLASK_ENV=development
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Step 4: Buka Browser

1. Buka browser (Chrome, Firefox, Edge, Safari)
2. Ketik di address bar: `http://localhost:5000`
3. Aplikasi akan terbuka!

---

## 🧪 TESTING APLIKASI

### Test 1: Cek Form Muncul

1. Buka http://localhost:5000
2. Seharusnya Anda lihat form dengan field:
   - Penghasilan Orang Tua
   - Kondisi Rumah
   - Pekerjaan Orang Tua
   - Kepemilikan Rumah
   - Status Ekonomi
   - Penerima KKS

### Test 2: Prediksi Pertama

Isi form dengan data:
- Penghasilan Orang Tua: **Rendah**
- Kondisi Rumah: **Sederhana**
- Pekerjaan Orang Tua: **Buruh**
- Kepemilikan Rumah: **Sewa**
- Status Ekonomi: **Kurang Mampu**
- Penerima KKS: **Ya**

Klik "🔍 Prediksi Kelayakan PIP"

Expected Result:
- Status: ✓ LAYAK MENERIMA PIP
- Confidence: ~90%

### Test 3: Prediksi Kedua

Isi form dengan data:
- Penghasilan Orang Tua: **Tinggi**
- Kondisi Rumah: **Mewah**
- Pekerjaan Orang Tua: **PNS**
- Kepemilikan Rumah: **Milik Sendiri**
- Status Ekonomi: **Mampu**
- Penerima KKS: **Tidak**

Klik "🔍 Prediksi Kelayakan PIP"

Expected Result:
- Status: ✗ TIDAK LAYAK MENERIMA PIP
- Confidence: ~90%

---

## 🔧 TROUBLESHOOTING

### Error 1: "ModuleNotFoundError: No module named 'flask'"

**Penyebab:** Library belum diinstall

**Solusi:**
```bash
pip install flask
```

### Error 2: "FileNotFoundError: data_training.csv"

**Penyebab:** File data_training.csv tidak ada

**Solusi:**
1. Pastikan file ada di folder yang sama dengan app.py
2. Nama file harus tepat: `data_training.csv` (huruf kecil)

### Error 3: "model_pip.pkl not found"

**Penyebab:** Model belum dilatih

**Solusi:**
1. Jalankan `python model_training.py` dulu
2. Tunggu sampai selesai

### Error 4: "Port 5000 already in use"

**Penyebab:** Port 5000 sudah dipakai aplikasi lain

**Solusi:**
Edit `app.py`, ubah baris terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Ubah ke 5001
```

Kemudian akses: `http://localhost:5001`

### Error 5: Form tidak muncul

**Penyebab:** JavaScript error atau API /api/fields gagal

**Solusi:**
1. Buka DevTools (F12) > Console
2. Lihat error message
3. Pastikan server Flask running dengan baik

---

## 📊 STRUKTUR DATA

### Input (6 Field):
```
{
  "penghasilan_orang_tua": "Rendah|Sedang|Tinggi",
  "kondisi_rumah": "Kumuh|Sederhana|Biasa|Mewah",
  "pekerjaan_orang_tua": "Buruh|Petani|Swasta|...",
  "kepemilikan_rumah": "Sewa|Milik Sendiri",
  "status_ekonomi": "Sangat Kurang|Kurang Mampu|Cukup|Mampu",
  "penerima_kks": "Ya|Tidak"
}
```

### Output (Prediksi):
```
{
  "status": "success",
  "hasil": "Layak|Tidak Layak",
  "confidence": 85.5,  // Persentase (0-100)
  "probabilities": {
    "Layak": 85.5,
    "Tidak Layak": 14.5
  },
  "data_input": {...}
}
```

---

## 📈 CARA MENINGKATKAN AKURASI

1. **Tambah Data Training**
   - Edit `data_training.csv`
   - Tambah lebih banyak baris data siswa
   - Jalankan `python model_training.py` lagi

2. **Edit Feature (Fitur)**
   - Tambah kolom baru di CSV
   - Update form HTML
   - Jalankan training ulang

3. **Pilih Algoritma Berbeda**
   - Ganti `CategoricalNB` dengan `RandomForestClassifier`, `GradientBoostingClassifier`, dll
   - Lihat dokumentasi scikit-learn

---

## 🎓 PENJELASAN ALGORITMA

### Naive Bayes Theorem:

```
P(Class|Features) = P(Features|Class) × P(Class) / P(Features)

Contoh:
P(Layak | Rendah, Sederhana) = 
    P(Rendah, Sederhana | Layak) × P(Layak) / P(Rendah, Sederhana)
```

### Keuntungan:
- ✓ Cepat dan efisien
- ✓ Cocok untuk dataset kecil
- ✓ Mudah dipahami
- ✓ Hasil akurat untuk klasifikasi

### Kerugian:
- ✗ Asumsi fitur independen (tidak selalu benar)
- ✗ Tidak cocok untuk dataset dengan nilai yang sangat berbeda

---

## 💡 TIPS & TRIK

1. **Testing API dengan cURL:**
```bash
curl -X POST http://localhost:5000/api/prediksi \
  -H "Content-Type: application/json" \
  -d '{"penghasilan_orang_tua":"Rendah",...}'
```

2. **Lihat Log Server:**
Terminal tempat Anda jalankan `python app.py` menunjukkan semua request yang masuk

3. **Debug JavaScript:**
Tekan F12 di browser, buka Tab "Console" untuk lihat error

4. **Simpan Hasil Prediksi:**
Tambahkan fitur export ke CSV/PDF (lihat dokumentasi Flask)

---

## 📝 CHECKLIST SEBELUM SERAH TUGAS

- [ ] Semua file sudah dibuat
- [ ] Dependencies sudah diinstall (`pip install -r requirements.txt`)
- [ ] Model sudah dilatih (`python model_training.py`)
- [ ] Server berjalan tanpa error (`python app.py`)
- [ ] Website terbuka di browser (`http://localhost:5000`)
- [ ] Form muncul dengan benar
- [ ] Prediksi berfungsi
- [ ] Hasil menampilkan status + confidence
- [ ] Halaman Informasi PIP berjalan
- [ ] Responsif di mobile

---

## 🎯 KESIMPULAN

Selamat! Anda sudah membuat aplikasi web untuk prediksi kelayakan PIP menggunakan Machine Learning! 🎉

**Apa yang sudah Anda pelajari:**
- ✅ Membuat model Machine Learning dengan Python
- ✅ Membuat web server dengan Flask
- ✅ Membuat frontend dengan HTML/CSS/JavaScript
- ✅ Mengintegrasikan ML model ke dalam web app
- ✅ Handling form dan API requests

**Next Steps:**
- Tambah fitur database untuk menyimpan history prediksi
- Tambah fitur login/authentication
- Deploy ke server online (Heroku, AWS, dll)
- Tingkatkan akurasi dengan data lebih banyak

Sukses! 🚀
