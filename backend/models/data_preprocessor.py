import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

class DataPreprocessor:
    """
    Kelas untuk preprocessing data input sebelum klasifikasi
    """
    
    def __init__(self):
        self.scaler = None
        self.label_encoders = {}
        self.feature_names = None
        
    def fit(self, X, y=None):
        """
        Fit preprocessor dengan training data
        
        Args:
            X: DataFrame dengan fitur
            y: Series dengan target (opsional)
        """
        # Inisialisasi scaler
        self.scaler = StandardScaler()
        self.scaler.fit(X)
        
        # Simpan nama fitur
        self.feature_names = X.columns.tolist()
        
        return self
    
    def transform(self, X):
        """
        Transform data menggunakan fitted preprocessor
        
        Args:
            X: DataFrame dengan fitur
            
        Returns:
            numpy array hasil scaling
        """
        if self.scaler is None:
            raise ValueError("Preprocessor belum di-fit. Panggil fit() terlebih dahulu")
        
        X_scaled = self.scaler.transform(X)
        return X_scaled
    
    def fit_transform(self, X, y=None):
        """
        Fit dan transform dalam satu langkah
        """
        self.fit(X, y)
        return self.transform(X)
    
    def save(self, scaler_path, feature_names_path):
        """
        Simpan preprocessor ke file
        """
        joblib.dump(self.scaler, scaler_path)
        joblib.dump(self.feature_names, feature_names_path)
        
    def load(self, scaler_path, feature_names_path):
        """
        Load preprocessor dari file
        """
        self.scaler = joblib.load(scaler_path)
        self.feature_names = joblib.load(feature_names_path)
        return self


class FeatureValidator:
    """
    Kelas untuk validasi dan transformasi fitur input
    """
    
    REQUIRED_FEATURES = [
        'penghasilan_orang_tua',      # Kategori: Rendah, Menengah, Tinggi
        'jumlah_tanggungan',           # Numerik: 1-10
        'kondisi_rumah',               # Kategori: Buruk, Sedang, Baik
        'status_kerja_ayah',           # Kategori: Tidak Bekerja, Bekerja Informal, Bekerja Formal
        'status_kerja_ibu',            # Kategori: Tidak Bekerja, Bekerja Informal, Bekerja Formal
        'prestasi_akademik',           # Numerik: 0-100 (nilai rata-rata)
        'aset_keluarga',               # Kategori: Tidak Ada, Terbatas, Memadai
        'akses_pendidikan'             # Kategori: Tidak Ada, Terbatas, Baik
    ]
    
    CATEGORICAL_MAPPINGS = {
        'penghasilan_orang_tua': {'rendah': 0, 'menengah': 1, 'tinggi': 2},
        'kondisi_rumah': {'buruk': 0, 'sedang': 1, 'baik': 2},
        'status_kerja_ayah': {'tidak_bekerja': 0, 'informal': 1, 'formal': 2},
        'status_kerja_ibu': {'tidak_bekerja': 0, 'informal': 1, 'formal': 2},
        'aset_keluarga': {'tidak_ada': 0, 'terbatas': 1, 'memadai': 2},
        'akses_pendidikan': {'tidak_ada': 0, 'terbatas': 1, 'baik': 2}
    }
    
    @classmethod
    def validate(cls, features_dict):
        """
        Validasi input features
        
        Args:
            features_dict: Dictionary dengan nama fitur sebagai key
            
        Returns:
            Tuple (is_valid, error_message)
        """
        # Check required features
        missing = [f for f in cls.REQUIRED_FEATURES if f not in features_dict]
        if missing:
            return False, f"Fitur yang hilang: {', '.join(missing)}"
        
        # Validate numerical features
        try:
            jumlah_tanggungan = int(features_dict['jumlah_tanggungan'])
            if not (1 <= jumlah_tanggungan <= 10):
                return False, "Jumlah tanggungan harus antara 1-10"
        except ValueError:
            return False, "Jumlah tanggungan harus berupa angka"
        
        try:
            prestasi_akademik = float(features_dict['prestasi_akademik'])
            if not (0 <= prestasi_akademik <= 100):
                return False, "Prestasi akademik harus antara 0-100"
        except ValueError:
            return False, "Prestasi akademik harus berupa angka"
        
        return True, None
    
    @classmethod
    def transform_features(cls, features_dict):
        """
        Transform input features menjadi format yang siap untuk model
        
        Args:
            features_dict: Dictionary dengan input features
            
        Returns:
            Dictionary dengan fitur yang sudah ditransform
        """
        transformed = {}
        
        for feature_name, value in features_dict.items():
            if feature_name in cls.CATEGORICAL_MAPPINGS:
                # Transform categorical features
                mapping = cls.CATEGORICAL_MAPPINGS[feature_name]
                value_lower = str(value).lower()
                if value_lower in mapping:
                    transformed[feature_name] = mapping[value_lower]
                else:
                    raise ValueError(f"Nilai tidak valid untuk {feature_name}: {value}")
            else:
                # Keep numerical features as is
                transformed[feature_name] = float(value)
        
        return transformed
