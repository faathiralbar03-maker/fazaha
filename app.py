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
