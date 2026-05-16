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

// ===== UTILITY FUNCTIONS =====

// Format teks
function formatLabel(text) {
    return text
        .replace(/_/g, ' ')
        .replace(/\b\w/g, l => l.toUpperCase());
}

// Check API health
function checkApiHealth() {
    fetch('/api/health')
        .then(response => response.json())
        .then(data => {
            console.log('API Status:', data);
        })
        .catch(error => {
            console.error('API tidak tersedia:', error);
        });
}

// Jalankan health check saat loading
window.addEventListener('load', function() {
    checkApiHealth();
});
