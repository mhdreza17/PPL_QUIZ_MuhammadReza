# Test Strategy & Differentiators
## PPL Quiz - Muhammad Reza

---

## Test Design Strategy

### Struktur Test yang Berbeda

#### 1. **Test Organization**
- **Approach Kami**: Test dikelompokkan berdasarkan **requirements** (S1.1, S2.1, UI.1)
- **Class-based organization** yang jelas dengan 4 test classes utama:
  - `TestLoginValidation` (FT_001-FT_008)
  - `TestRegistrationValidation` (FT_009-FT_017)
  - `TestNavigationUI` (FT_018-FT_021)
  - `TestSecurityVulnerabilities` (SECURITY_001-SECURITY_008)

#### 2. **Screenshot Strategy**
```python
def take_screenshot(driver, test_id, step_name):
    """Capture screenshot dengan test ID dan step name"""
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{test_id}_{step_name}_{timestamp}.png"
    # Organized by test type dan dengan timestamp untuk tracking
```

- **Keunikan**: 
  - Named dengan format `TEST_ID_STEP_TIMESTAMP.png`
  - Lebih mudah untuk tracking progress setiap test case
  - Memudahkan debugging dengan step yang jelas

#### 3. **Test Case Mapping**
Setiap test case dipetakan langsung dari requirement document:

```
FT_001 → Verifikasi login berhasil dengan kredensial valid
FT_002 → Verifikasi sistem menolak login saat password kosong
...dst
```

---

## Fitur Unik Test Suite Kami

### 1. **Comprehensive Security Testing**
Tidak hanya functional test, tapi juga security testing yang mendalam:

```python
class TestSecurityVulnerabilities:
    - SQL Injection (3 test cases)
    - XSS Attack (1 test case)
    - Password Security (3 test cases)
    - Account Enumeration (1 test case)
    - Timing Attack Detection (1 test case)
```

**Keunikan**: Test menggunakan actual payloads seperti:
- `' OR '1'='1` (SQL injection)
- `<img src=x onerror='alert("XSS")'>` (XSS)
- Deteksi timing untuk user enumeration

### 2. **Flexible Test Execution**
```bash
# Run semua test
pytest test_authentication_ppl_quiz.py -v

# Run class tertentu saja
pytest test_authentication_ppl_quiz.py::TestLoginValidation -v

# Run test tertentu
pytest test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials -v

# Run dengan filter
pytest -k "FT_001 or SECURITY_001" -v
```

### 3. **Detailed Screenshot Capture**
- Setiap step penting diambil screenshot
- Organized folder structure: `screenshots/auth_testing/`
- Timestamp untuk easy tracking
- Total ~30+ screenshots per full run

### 4. **Dynamic Test Data**
```python
timestamp = int(time.time())
unique_user = f"newuser_{timestamp}"
unique_email = f"user_{timestamp}@example.com"
```

Tidak hardcoded, sehingga bisa run multiple times tanpa conflict

### 5. **Explicit Wait Handling**
```python
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
```

Menggunakan explicit wait dengan condition checking, bukan implicit wait saja

---

## Perbandingan dengan Pendekatan Umum

### Pendekatan Konvensional ❌
```python
def test_login():
    driver.get("http://localhost/login.php")
    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("pass")
    driver.find_element(By.NAME, "submit").click()
    assert "index.php" in driver.current_url
```

### Pendekatan Kami ✅
```python
def test_FT_001_login_valid_credentials(self, driver, base_url):
    """FT_001: Verify successful login with valid participant credentials"""
    driver.get(f"{base_url}/login.php")
    take_screenshot(driver, "FT_001", "initial_page")
    
    # Wait untuk element dengan explicit wait
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Fill form
    username_field.send_keys("testuser123")
    password_field = driver.find_element(By.ID, "InputPassword")
    password_field.send_keys("TestPassword123!")
    
    take_screenshot(driver, "FT_001", "form_filled")
    
    # Submit
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    time.sleep(2)
    
    take_screenshot(driver, "FT_001", "after_submit")
    
    # Assertion dengan deskripsi jelas
    assert "index.php" in driver.current_url or "dashboard" in driver.current_url.lower(), \
        f"Expected redirect to index/dashboard, but got {driver.current_url}"
```

**Perbedaan Kunci**:
- ✅ Dokumentasi test case ID (FT_001, SECURITY_001)
- ✅ Explicit wait dengan condition checking
- ✅ Multiple screenshots per test case
- ✅ Assertion message yang detailed
- ✅ Better error tracing
- ✅ Organized dalam class dengan naming convention

---

## Coverage Comparison

### Test Categories Kami:

```
┌─ Login Validation (8 tests)
│  ├─ Valid credentials ✓
│  ├─ Empty password ✓
│  ├─ Empty username ✓
│  ├─ Unregistered user ✓
│  ├─ Wrong password ✓
│  ├─ Mismatched credentials ✓
│  ├─ Rate limiting ✓
│  └─ Session expired ✓
│
├─ Registration Validation (9 tests)
│  ├─ Valid data ✓
│  ├─ Empty email ✓
│  ├─ Empty username ✓
│  ├─ Duplicate username ✓
│  ├─ Password mismatch ✓
│  ├─ Empty password ✓
│  ├─ Invalid email format ✓
│  ├─ Long password edge case ✓
│  └─ Special characters in username ✓
│
├─ Navigation & UI (4 tests)
│  ├─ Register link from login ✓
│  ├─ Register page → login redirect ✓
│  ├─ Login link on register ✓
│  └─ Logout & page protection ✓
│
└─ Security Testing (8 tests)
   ├─ SQL injection username ✓
   ├─ SQL injection password ✓
   ├─ SQL injection registration ✓
   ├─ XSS attack ✓
   ├─ Password visibility ✓
   ├─ Weak password detection ✓
   ├─ Timing attack detection ✓
   └─ Account enumeration ✓

TOTAL: 29 test cases
```

---

## Best Practices Implemented

### 1. **Test Isolation**
- Setiap test independen dan tidak bergantung pada test lain
- Dynamic data generation mencegah conflicts
- Session clearing untuk clean state

### 2. **Page Object Pattern Ready**
Struktur code siap untuk diperluas dengan Page Object Pattern:
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)
    
    def fill_password(self, password):
        self.driver.find_element(By.ID, "InputPassword").send_keys(password)
    
    def submit(self):
        self.driver.find_element(By.NAME, "submit").click()
```

### 3. **Comprehensive Error Handling**
```python
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "..."))
    )
except TimeoutException:
    print("Element not found within 5 seconds")
except NoSuchElementException:
    print("Element doesn't exist in DOM")
```

### 4. **Security-First Testing**
- Tidak hanya test happy path
- Test attack vectors (SQL injection, XSS)
- Test untuk account enumeration
- Test untuk timing attacks

### 5. **Documentation**
Setiap test punya:
- Test ID (FT_XXX atau SECURITY_XXX)
- Deskripsi dalam docstring
- Clear assertion messages
- Related requirement mapping

---

## Execution Examples

### Quick Start
```bash
# Setup
cd tests
pip install -r requirements.txt

# Run all
pytest test_authentication_ppl_quiz.py -v

# Output:
# test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials PASSED
# test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_002_login_empty_password PASSED
# ...
```

### Target Specific Tests
```bash
# Login tests only
pytest test_authentication_ppl_quiz.py::TestLoginValidation -v

# Security tests only
pytest test_authentication_ppl_quiz.py::TestSecurityVulnerabilities -v --tb=short

# Single test
pytest test_authentication_ppl_quiz.py::TestLoginValidation::test_FT_001_login_valid_credentials -v -s
```

### With Coverage Report
```bash
pytest test_authentication_ppl_quiz.py --cov --cov-report=html
# Generates htmlcov/index.html
```

---

## Unique Aspects vs Common Tests

| Aspek | Pendekatan Umum | Kami |
|-------|-----------------|-----|
| **Organization** | Single file atau random classes | Organized by requirement (S1.1, S2.1, UI.1) |
| **Test IDs** | No clear mapping | FT_001-FT_021 sesuai requirement doc |
| **Security** | Happy path only | 8+ security-specific test cases |
| **Screenshots** | Random atau tidak | Organized, timestamped, per-step |
| **Test Data** | Hardcoded | Dynamic dengan timestamp |
| **Wait Strategy** | Implicit wait | Explicit wait dengan conditions |
| **Error Messages** | Generic | Detailed dengan actual vs expected |
| **Naming** | test_login, test_register | test_FT_001_login_valid_credentials |
| **Documentation** | Minimal | Complete TEST_DOCUMENTATION.md |
| **Class Structure** | Flat | Organized into 4 purpose-specific classes |

---

## How to Differentiate Further

Jika ingin membuat test yang lebih unik lagi:

### 1. Tambah API Testing
```python
class TestAPIAuthentication:
    def test_login_api_endpoint(self, base_url):
        response = requests.post(f"{base_url}/api/login", 
                                json={"username": "test", "password": "pass"})
        assert response.status_code == 200
```

### 2. Database Assertion
```python
def test_registration_database(self, driver, base_url, db_connection):
    # Complete registration
    # Then verify in database
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (unique_user,))
    assert cursor.fetchone() is not None
```

### 3. Performance Testing
```python
def test_login_performance(self, driver, base_url):
    import time
    start = time.time()
    # Do login
    elapsed = time.time() - start
    assert elapsed < 2.0, f"Login should be < 2 seconds, took {elapsed}"
```

### 4. Accessibility Testing
```python
from axe_selenium_python import Axe

def test_login_accessibility(self, driver, base_url):
    driver.get(f"{base_url}/login.php")
    axe = Axe(driver)
    axe.inject()
    axe.run()
    results = axe.results()
    assert len(results["violations"]) == 0
```

---

## Summary

Test suite kami unik karena:

1. **Terstruktur jelas** dengan mapping ke requirement document
2. **Comprehensive coverage** mencakup functional + security testing
3. **Professional practices** dengan screenshot, logging, assertions
4. **Easy to maintain** dengan clear naming dan organization
5. **Easy to extend** dengan structure yang scalable
6. **Security-focused** dengan actual attack payloads
7. **Well documented** dengan detailed README dan inline comments

---

*Version 1.0 - January 2026*
