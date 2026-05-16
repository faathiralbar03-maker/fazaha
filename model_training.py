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
