# 🚀 Quick Start Guide

## 5 Menit Setup

### 1️⃣ Setup Database (2 menit)
```bash
# Buka MySQL Command Line atau MySQL Workbench
mysql -u root -p

# Jalankan:
mysql> SOURCE db/quiz_pengupil.sql;
mysql> SHOW TABLES FROM quiz_pengupil;  # Verifikasi
mysql> EXIT;
```

### 2️⃣ Setup Python Environment (2 menit)
```bash
# Masuk ke folder tests
cd tests

# Install dependencies
pip install -r requirements.txt

# Verifikasi
pip list | findstr selenium pytest
```

### 3️⃣ Start XAMPP (1 menit)
```
1. Buka XAMPP Control Panel
2. Klik "Start" pada Apache
3. Klik "Start" pada MySQL
4. Verifikasi: http://localhost/fiz_quizppl/login.php
```

### 4️⃣ Run Tests
```bash
# Di folder tests, jalankan:
pytest test_authentication_ppl_quiz.py -v

# Lihat hasil di terminal
# Screenshots tersimpan di: tests/screenshots/auth_testing/
```

---

## Test Categories (Pilih Saja)

```bash
# Login Tests (8 tests)
pytest test_authentication_ppl_quiz.py::TestLoginValidation -v

# Register Tests (9 tests)
pytest test_authentication_ppl_quiz.py::TestRegistrationValidation -v

# Navigation Tests (4 tests)
pytest test_authentication_ppl_quiz.py::TestNavigationUI -v

# Security Tests (8 tests)
pytest test_authentication_ppl_quiz.py::TestSecurityVulnerabilities -v

# Satu test aja
pytest test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials -v
```

---

## Default Test User

```
Username: testuser123
Password: TestPassword123!
```

⚠️ **Pastikan user ini sudah ada di database sebelum test login!**

---

## 🔍 Lihat Hasil

### Screenshots
```
tests/screenshots/auth_testing/
├── FT_001_initial_page_*.png
├── FT_001_form_filled_*.png
├── FT_001_after_submit_*.png
└── ... (ribuan screenshot untuk 29 test cases)
```

### Test Report (Optional)
```bash
# Generate HTML report
pytest test_authentication_ppl_quiz.py --html=report.html --self-contained-html

# Buka: report.html di browser
```

---

## ⚡ Common Commands

| Command | Fungsi |
|---------|--------|
| `pytest -v` | Run dengan verbose output |
| `pytest -s` | Show print statements |
| `pytest -k "FT_001"` | Run test tertentu saja |
| `pytest --co` | List semua test (no run) |
| `pytest -x` | Stop di test pertama yang fail |
| `pytest --tb=short` | Short traceback format |
| `pytest -m "not slow"` | Skip slow tests |

---

## 🆘 Troubleshooting 3 Masalah Umum

### ❌ "Connection refused"
```bash
# Cek XAMPP running
# Pastikan Apache & MySQL hidup

# Atau gunakan port lain
set BASE_URL=http://127.0.0.1:8000/fiz_quizppl

# Update port di koneksi.php jika perlu
```

### ❌ "ChromeDriver error"
```bash
pip install --upgrade webdriver-manager

# Clear cache
python -m webdriver_manager chrome --cleanup
```

### ❌ "Test timeout"
```bash
# Edit conftest.py, ubah:
driver.implicitly_wait(10)  → driver.implicitly_wait(15)

# Atau run dengan longer timeout:
pytest --tb=long -v
```

---

## 📊 Expected Output

```
test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials PASSED [  3%]
test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_002_login_empty_password PASSED [  6%]
test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_003_login_empty_username PASSED [ 10%]
...
test_authentication_ppl_quiz.py::TestSecurityVulnerabilities::test_SECURITY_008_account_enumeration PASSED [100%]

========================= 29 passed in 85.34s ==========================
```

---

## 📝 Next Steps

1. ✅ Setup selesai? Bagus!
2. 📖 Baca `TEST_DOCUMENTATION.md` untuk detail test cases
3. 🔒 Cek `TEST_STRATEGY.md` untuk perbedaan dengan test lain
4. 🐙 Push ke GitHub: https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza

---

## 💡 Tips

- Jalankan test ketika server sedang sepi (less I/O overhead)
- Gunakan headless mode untuk CI/CD: `set CI=true`
- Screenshot berguna untuk documentation, tapi bisa comment untuk speed
- Test berjalan sequential, tidak parallel (untuk stability)

---

**Happy Testing! 🎉**

Pertanyaan? Lihat TEST_DOCUMENTATION.md atau README.md
