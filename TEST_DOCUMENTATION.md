# PPL Quiz - Muhammad Reza
## Sistem Autentikasi & Registrasi untuk Platform Quiz

Repository: https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza

### Deskripsi Project
Project ini adalah sistem autentikasi dan registrasi untuk platform quiz online yang dibangun dengan:
- **Backend**: PHP (Native)
- **Database**: MySQL
- **Frontend**: HTML/CSS/Bootstrap
- **Testing**: Python Selenium

---

## Struktur Project

```
fiz_quizppl/
├── login.php              # Halaman login
├── register.php           # Halaman registrasi
├── koneksi.php            # Koneksi database
├── style.css              # Stylesheet
├── index.php              # Halaman dashboard (protected)
├── db/
│   └── quiz_pengupil.sql  # Database schema
├── tests/
│   ├── conftest.py        # Konfigurasi pytest & fixtures
│   ├── requirements.txt    # Dependencies Python
│   ├── pytest.ini          # Konfigurasi pytest
│   ├── test_authentication_ppl_quiz.py  # Test case komprehensif
│   └── screenshots/       # Hasil screenshot test
├── readme.md              # Dokumentasi
└── .gitignore
```

---

## Requirements

### Backend
- Apache Server (XAMPP)
- MySQL 5.7 atau lebih baru
- PHP 7.0 atau lebih baru

### Testing
- Python 3.7+
- Selenium 4.0+
- ChromeDriver
- webdriver-manager

---

## Instalasi & Setup

### 1. Setup Database
```sql
-- Import file db/quiz_pengupil.sql ke MySQL
mysql -u root -p < db/quiz_pengupil.sql
```

### 2. Konfigurasi Koneksi Database
Edit file `koneksi.php`:
```php
$host = "localhost";
$user = "root";
$pass = "";  // Sesuaikan password MySQL Anda
$db = "quiz_pengupil";
```

### 3. Setup Testing Environment
```bash
# Install dependencies
pip install -r tests/requirements.txt

# Set environment variable untuk base URL
set BASE_URL=http://localhost/fiz_quizppl
# atau di Linux/Mac:
export BASE_URL=http://localhost/fiz_quizppl
```

---

## Menjalankan Test

### Semua Test
```bash
cd tests
pytest test_authentication_ppl_quiz.py -v
```

### Test Kategori Tertentu
```bash
# Login tests saja
pytest test_authentication_ppl_quiz.py::TestLoginValidation -v

# Registration tests saja
pytest test_authentication_ppl_quiz.py::TestRegistrationValidation -v

# Navigation tests saja
pytest test_authentication_ppl_quiz.py::TestNavigationUI -v

# Security tests saja
pytest test_authentication_ppl_quiz.py::TestSecurityVulnerabilities -v
```

### Test Dengan Screenshot
Screenshot akan otomatis tersimpan di `tests/screenshots/auth_testing/`

### Mode Headless (CI/CD)
```bash
set CI=true
pytest test_authentication_ppl_quiz.py -v
```

---

## Test Cases

### 1. Login Validation (FT_001 - FT_008)

| ID | Test Case | Deskripsi |
|----|-----------|-----------|
| FT_001 | Login Berhasil | Verifikasi login dengan kredensial valid |
| FT_002 | Password Kosong | Sistem menolak login saat password kosong |
| FT_003 | Username Kosong | Sistem menolak login saat username kosong |
| FT_004 | User Tidak Terdaftar | Login gagal untuk user yang tidak ada |
| FT_005 | Password Salah | Login gagal dengan password yang salah |
| FT_006 | Kredensial Tidak Cocok | Login gagal saat kombinasi username-password salah |
| FT_007 | Rate Limiting | Penerapan rate limiting pada login gagal berulang |
| FT_008 | Session Expired | Session expired mengarahkan ke halaman login |

### 2. Registration Validation (FT_009 - FT_017)

| ID | Test Case | Deskripsi |
|----|-----------|-----------|
| FT_009 | Registrasi Berhasil | Verifikasi registrasi dengan data valid |
| FT_010 | Email Kosong | Registrasi gagal saat email kosong |
| FT_011 | Username Kosong | Registrasi gagal saat username kosong |
| FT_012 | Username Duplikat | Registrasi gagal saat username sudah ada |
| FT_013 | Password Tidak Sama | Registrasi gagal saat password tidak cocok |
| FT_014 | Password Kosong | Registrasi gagal saat password kosong |
| FT_015 | Format Email Invalid | Registrasi gagal dengan format email tidak valid |
| FT_016 | Password Panjang | Registrasi dengan password panjang (edge case) |
| FT_017 | Karakter Spesial Username | Registrasi dengan special characters pada username |

### 3. Navigation & UI Flow (FT_018 - FT_021)

| ID | Test Case | Deskripsi |
|----|-----------|-----------|
| FT_018 | Redirect Register → Login | Verifikasi redirect dari halaman register ke login |
| FT_019 | Link Register di Login | Verifikasi link Register ada di halaman Login |
| FT_020 | Link Login di Register | Verifikasi link Login ada di halaman Register |
| FT_021 | Logout & Proteksi | Verifikasi proses logout dan proteksi halaman |

### 4. Security Testing (SECURITY_001 - SECURITY_008)

| ID | Test Case | Deskripsi |
|----|-----------|-----------|
| SECURITY_001 | SQL Injection - Username | Proteksi SQL injection di field username login |
| SECURITY_002 | SQL Injection - Password | Proteksi SQL injection di field password login |
| SECURITY_003 | SQL Injection - Register | Proteksi SQL injection di form registrasi |
| SECURITY_004 | XSS Attack | Proteksi XSS attack di form login |
| SECURITY_005 | Password Visibility | Password field tidak terlihat di HTML |
| SECURITY_006 | Weak Password Detection | Deteksi dan handling password lemah |
| SECURITY_007 | Timing Attacks | Timing konsisten untuk mencegah timing attacks |
| SECURITY_008 | Account Enumeration | Mencegah account enumeration attacks |

---

## Test Data

### Akun Test Default
```
Username: testuser123
Password: TestPassword123!
```

### Test Data untuk Registrasi
Test akan membuat akun baru dengan format:
- Username: `testuser_{timestamp}`
- Email: `user_{timestamp}@example.com`
- Password: `TestPass123!`

---

## Fitur Keamanan yang Diuji

### 1. Password Security
- ✅ Password hashing dengan bcrypt/PASSWORD_DEFAULT
- ✅ Validasi password tidak kosong
- ✅ Konfirmasi password harus sama
- ✅ Password field type="password"

### 2. Input Validation
- ✅ SQL Injection protection (mysqli_real_escape_string + prepared statements)
- ✅ Email validation
- ✅ Username validation
- ✅ XSS protection (output escaping)

### 3. Session Management
- ✅ Session protection untuk halaman protected
- ✅ Redirect ke login saat session expired
- ✅ Session cookie handling

### 4. Error Handling
- ✅ Generic error messages untuk mencegah enumeration
- ✅ Validasi di frontend dan backend
- ✅ Error message display

---

## Hasil Test

### Screenshot Locations
```
tests/screenshots/auth_testing/
├── FT_001_*.png  (Login tests)
├── FT_002_*.png
├── ...
├── SECURITY_001_*.png (Security tests)
└── ...
```

### Test Report
```bash
# Generate HTML report
pytest test_authentication_ppl_quiz.py --html=report.html

# Generate dengan coverage
pytest test_authentication_ppl_quiz.py --cov=. --cov-report=html
```

---

## Troubleshooting

### Driver Chrome tidak ditemukan
```bash
pip install --upgrade webdriver-manager
```

### Timeout Error
Tambah wait time di conftest.py:
```python
driver.implicitly_wait(15)  # Naikkan dari 10 menjadi 15 detik
```

### Base URL tidak terhubung
```bash
# Pastikan XAMPP running
# Check: http://localhost/fiz_quizppl/login.php

# Set custom BASE_URL jika diperlukan
set BASE_URL=http://127.0.0.1:80/fiz_quizppl
```

### Port konflik
Jika port 80 sudah dipakai, gunakan port lain di XAMPP Apache configuration.

---

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:5.7
        env:
          MYSQL_DATABASE: quiz_pengupil
          MYSQL_ROOT_PASSWORD: root
    steps:
      - uses: actions/checkout@v2
      - name: Start Apache
        run: |
          sudo apt-get install apache2 php mysql-server
          sudo service apache2 start
          sudo service mysql start
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      
      - name: Install Dependencies
        run: pip install -r tests/requirements.txt
      
      - name: Run Tests
        env:
          BASE_URL: http://localhost/fiz_quizppl
          CI: true
        run: pytest tests/test_authentication_ppl_quiz.py -v
```

---

## Metrics

### Test Coverage
- **Login Functionality**: 8 test cases
- **Registration Functionality**: 9 test cases
- **Navigation & UI**: 4 test cases
- **Security Testing**: 8 test cases
- **Total**: 29+ test cases

### Performance
- Average test execution time: ~2-3 detik per test
- Total suite execution: ~60-90 detik (tergantung system)

---

## Kontribusi & Dokumentasi

Untuk menambah test case baru:

1. Buat method baru di class yang sesuai
2. Ikuti naming convention: `test_FT_XXX_description` atau `test_SECURITY_XXX_description`
3. Tambahkan screenshot untuk setiap step penting
4. Update dokumentasi di README.md

### Naming Convention
```python
def test_FT_001_login_valid_credentials(self, driver, base_url):
    """FT_001: Deskripsi test case"""
    pass
```

---

## Dependencies

### Python Packages (requirements.txt)
```
selenium>=4.0.0
webdriver-manager>=3.8.0
pytest>=7.0.0
pytest-html>=3.1.0
pytest-cov>=4.0.0
```

### PHP Extensions
- mysqli atau PDO MySQL
- session

### MySQL
- Character set: utf8mb4
- Collation: utf8mb4_unicode_ci

---

## Notes Pengembangan

### Security Best Practices
- ✅ Menggunakan password hashing (PASSWORD_DEFAULT)
- ✅ Input escaping dengan mysqli_real_escape_string
- ✅ Session management proper
- ⚠️ Pertimbangkan prepared statements untuk lebih aman
- ⚠️ Implementasi rate limiting untuk brute force protection
- ⚠️ HTTPS enforcement di production

### Future Improvements
- [ ] Implementasi prepared statements
- [ ] Rate limiting untuk login attempts
- [ ] Email verification untuk registrasi
- [ ] Two-factor authentication
- [ ] Password reset functionality
- [ ] Account activation via email
- [ ] CSRF token protection

---

## License
MIT License

## Contact
GitHub: https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza

---

*Last Updated: January 2026*
