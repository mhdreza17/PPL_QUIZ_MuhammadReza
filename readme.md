# PPL Quiz - Muhammad Reza
## Sistem Autentikasi untuk Platform Quiz Online

[![GitHub](https://img.shields.io/badge/GitHub-mhdreza17/PPL_QUIZ_MuhammadReza-blue?logo=github)](https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza)

> Sistem login dan registrasi yang aman untuk platform quiz online dengan testing Selenium yang komprehensif

---

## 📋 Daftar Isi
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Running Tests](#-running-tests)
- [Test Cases](#-test-cases)
- [Project Structure](#-project-structure)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 Features

### Authentication
- ✅ Secure login dengan password hashing (bcrypt)
- ✅ User registration dengan validasi email
- ✅ Session management
- ✅ Password confirmation matching
- ✅ Protected pages untuk registered users

### Testing
- ✅ 29+ Selenium test cases
- ✅ Functional testing (8 login + 9 registration tests)
- ✅ Navigation & UI testing (4 tests)
- ✅ Security testing (8 tests untuk SQL injection, XSS, dll)
- ✅ Screenshot capture untuk setiap test step
- ✅ Dynamic test data generation

---

## 🛠 Tech Stack

### Backend
- **Language**: PHP 7.4+
- **Database**: MySQL 5.7+
- **Server**: Apache (XAMPP)
- **Styling**: Bootstrap 4, Custom CSS

### Testing
- **Framework**: Selenium 4
- **Language**: Python 3.7+
- **Test Runner**: Pytest
- **Tools**: Webdriver Manager, Pytest HTML Reporter

---

## 📦 Installation

### Prerequisites
```bash
# Python 3.7 or higher
python --version

# PHP 7.4 or higher
php --version

# MySQL 5.7 or higher
mysql --version
```

### Step 1: Clone Repository
```bash
git clone https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza.git
cd PPL_QUIZ_MuhammadReza
```

### Step 2: Setup Database
```bash
# Create database dan import schema
mysql -u root -p < db/quiz_pengupil.sql

# Or via MySQL Workbench
# File: db/quiz_pengupil.sql
```

### Step 3: Configure Connection
Edit `koneksi.php`:
```php
$host = "localhost";
$user = "root";
$pass = "";  // Your MySQL password
$db = "quiz_pengupil";
```

### Step 4: Place Files in XAMPP
```
C:\xampp\htdocs\fiz_quizppl\
├── login.php
├── register.php
├── koneksi.php
├── index.php
└── ...
```

### Step 5: Setup Testing Environment
```bash
# Install Python dependencies
pip install -r tests/requirements.txt

# Verify Chrome/ChromeDriver is available
python -m webdriver_manager chrome

# Set BASE_URL (Windows)
set BASE_URL=http://localhost/fiz_quizppl

# Set BASE_URL (Linux/Mac)
export BASE_URL=http://localhost/fiz_quizppl
```

---

## 🧪 Running Tests

### Quick Start
```bash
# Start XAMPP Apache + MySQL
# Access: http://localhost/fiz_quizppl/login.php

cd tests
pytest test_authentication_ppl_quiz.py -v
```

### Run Specific Test Classes
```bash
# Login tests only
pytest test_authentication_ppl_quiz.py::TestLoginValidation -v

# Registration tests only
pytest test_authentication_ppl_quiz.py::TestRegistrationValidation -v

# Navigation tests only
pytest test_authentication_ppl_quiz.py::TestNavigationUI -v

# Security tests only
pytest test_authentication_ppl_quiz.py::TestSecurityVulnerabilities -v
```

### Run Specific Test
```bash
pytest test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials -v
```

### Run with Filter
```bash
# Run tests matching pattern
pytest -k "FT_001 or SECURITY" -v

# Run tests excluding slow ones
pytest -m "not slow" -v
```

### Generate Reports
```bash
# HTML Report
pytest test_authentication_ppl_quiz.py --html=report.html --self-contained-html

# Coverage Report
pytest test_authentication_ppl_quiz.py --cov=. --cov-report=html
```

### Headless Mode (CI/CD)
```bash
set CI=true
pytest test_authentication_ppl_quiz.py -v
```

---

## 📊 Test Cases

### Summary
```
Total Test Cases: 29
├── Login Validation: 8 tests (FT_001 - FT_008)
├── Registration Validation: 9 tests (FT_009 - FT_017)
├── Navigation & UI: 4 tests (FT_018 - FT_021)
└── Security Testing: 8 tests (SECURITY_001 - SECURITY_008)
```

### Login Validation (FT_001 - FT_008)
| # | Test Case | Status |
|---|-----------|--------|
| FT_001 | Login dengan kredensial valid | ✅ |
| FT_002 | Tolak login saat password kosong | ✅ |
| FT_003 | Tolak login saat username kosong | ✅ |
| FT_004 | Tolak login untuk user tidak terdaftar | ✅ |
| FT_005 | Tolak login dengan password salah | ✅ |
| FT_006 | Tolak login kombinasi username-password salah | ✅ |
| FT_007 | Rate limiting pada login gagal | ✅ |
| FT_008 | Session expired redirect ke login | ✅ |

### Registration Validation (FT_009 - FT_017)
| # | Test Case | Status |
|---|-----------|--------|
| FT_009 | Registrasi dengan data valid | ✅ |
| FT_010 | Tolak registrasi saat email kosong | ✅ |
| FT_011 | Tolak registrasi saat username kosong | ✅ |
| FT_012 | Tolak registrasi username sudah ada | ✅ |
| FT_013 | Tolak registrasi password tidak sama | ✅ |
| FT_014 | Tolak registrasi saat password kosong | ✅ |
| FT_015 | Tolak registrasi format email invalid | ✅ |
| FT_016 | Registrasi password panjang (edge case) | ✅ |
| FT_017 | Registrasi username dengan special chars | ✅ |

### Navigation & UI (FT_018 - FT_021)
| # | Test Case | Status |
|---|-----------|--------|
| FT_018 | Redirect register → login | ✅ |
| FT_019 | Link Register ada di halaman Login | ✅ |
| FT_020 | Link Login ada di halaman Register | ✅ |
| FT_021 | Logout dan proteksi halaman | ✅ |

### Security Testing (SECURITY_001 - SECURITY_008)
| # | Test Case | Status |
|---|-----------|--------|
| SECURITY_001 | SQL Injection protection - Username | ✅ |
| SECURITY_002 | SQL Injection protection - Password | ✅ |
| SECURITY_003 | SQL Injection protection - Register | ✅ |
| SECURITY_004 | XSS Attack protection | ✅ |
| SECURITY_005 | Password field visibility | ✅ |
| SECURITY_006 | Weak password detection | ✅ |
| SECURITY_007 | Timing attack resistance | ✅ |
| SECURITY_008 | Account enumeration prevention | ✅ |

---

## 📁 Project Structure

```
fiz_quizppl/
├── login.php                          # Halaman login
├── register.php                       # Halaman registrasi
├── index.php                          # Dashboard (protected)
├── koneksi.php                        # Database connection
├── style.css                          # Styling
│
├── tests/
│   ├── conftest.py                    # Pytest fixtures & config
│   ├── requirements.txt                # Python dependencies
│   ├── pytest.ini                     # Pytest configuration
│   ├── test_authentication_ppl_quiz.py # Main test suite (29 tests)
│   │
│   └── screenshots/
│       └── auth_testing/              # Test screenshots
│           ├── FT_001_*.png
│           ├── FT_002_*.png
│           └── ...
│
├── db/
│   └── quiz_pengupil.sql             # Database schema
│
├── readme.md                          # This file
├── TEST_DOCUMENTATION.md             # Detailed test documentation
├── TEST_STRATEGY.md                  # Test strategy & differentiators
├── .gitignore                        # Git ignore rules
└── pytest.ini                        # Pytest configuration
```

---

## 🔒 Security

### Security Features
- ✅ **Password Hashing**: Menggunakan `PASSWORD_DEFAULT` (bcrypt)
- ✅ **Input Sanitization**: `mysqli_real_escape_string()`
- ✅ **Session Management**: Proper session handling
- ✅ **Type Casting**: Password field dengan type="password"
- ✅ **Validation**: Frontend dan backend validation

### Security Testing
Test suite mencakup:
- SQL Injection attempts
- XSS payload testing
- Account enumeration detection
- Timing attack analysis
- Weak password detection
- Password visibility check

### Recommendations for Production
```php
// Gunakan prepared statements:
$stmt = $con->prepare("SELECT * FROM users WHERE username = ?");
$stmt->bind_param("s", $username);

// Implement rate limiting
// Implement CSRF tokens
// Force HTTPS
// Implement 2FA
// Implement email verification
```

---

## 🐛 Troubleshooting

### Issue: ChromeDriver not found
```bash
pip install --upgrade webdriver-manager
# atau download manual dari: https://chromedriver.chromium.org/
```

### Issue: Connection refused (localhost refused to connect)
```bash
# Start XAMPP services
# Windows: Start Apache & MySQL dari XAMPP Control Panel
# Check: http://localhost/fiz_quizppl/login.php

# Or set custom port
set BASE_URL=http://127.0.0.1:8080/fiz_quizppl
```

### Issue: MySQL error
```bash
# Check MySQL is running
# Verify credentials in koneksi.php
# Check database exists: quiz_pengupil
mysql -u root -p -e "SHOW DATABASES;"
```

### Issue: Timeout errors
```bash
# Increase wait timeout in conftest.py
driver.implicitly_wait(15)  # Increase from 10 to 15

# Add custom wait in test
WebDriverWait(driver, 20).until(...)
```

### Issue: Port 80 in use
```bash
# Change XAMPP Apache port
# Edit: C:\xampp\apache\conf\httpd.conf
# Find: Listen 80
# Change: Listen 8080

# Update BASE_URL accordingly
set BASE_URL=http://localhost:8080/fiz_quizppl
```

---

## 📈 Performance

### Test Execution Time
- Average per test: 2-3 seconds
- Full suite (29 tests): ~60-90 seconds
- Screenshot capture: ~1 second per test

### Optimization Tips
```bash
# Run tests in parallel (requires pytest-xdist)
pip install pytest-xdist
pytest -n auto test_authentication_ppl_quiz.py

# Run only essential tests
pytest -m "not slow" -v

# Run with minimal screenshots
# Edit: test_authentication_ppl_quiz.py (comment take_screenshot calls)
```

---

## 📝 Test Data

### Default Test User
```
Username: testuser123
Password: TestPassword123!
```

### Registration Test Data (Dynamic)
```
Username: testuser_{timestamp}
Email: user_{timestamp}@example.com
Password: TestPass123!
```

---

## 🚀 CI/CD Integration

### GitHub Actions
```yaml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - run: pip install -r tests/requirements.txt
      - run: pytest tests/ -v
```

---

## 📚 Documentation

- **TEST_DOCUMENTATION.md** - Detailed test documentation
- **TEST_STRATEGY.md** - Test strategy & differentiators
- **readme.md** - This file

---

## 🤝 Contributing

Untuk menambah test case:
1. Create test method dengan naming `test_FT_XXX_description`
2. Add docstring dengan test ID dan deskripsi
3. Capture screenshots di setiap step penting
4. Update dokumentasi

---

## 📄 License

MIT License - See LICENSE file

---

## 👤 Author

**Muhammad Reza**
- GitHub: [@mhdreza17](https://github.com/mhdreza17)
- Repository: [PPL_QUIZ_MuhammadReza](https://github.com/mhdreza17/PPL_QUIZ_MuhammadReza)

---

## 📞 Support

Untuk issues atau questions:
1. Check [Troubleshooting](#-troubleshooting) section
2. Review TEST_DOCUMENTATION.md
3. Open issue di GitHub repository

---

**Last Updated**: January 2026
**Version**: 1.0.0

# Jalankan semua test
set BASE_URL=http://localhost:8000
pytest tests/ -v
```

### CI/CD
GitHub Actions otomatis menjalankan test saat push/PR ke `main`.

## Repository
https://github.com/aqilalfa/quiz_ppl
