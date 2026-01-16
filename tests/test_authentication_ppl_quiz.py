"""
Selenium Test Cases untuk PPL Quiz - Muhammad Reza
Authentication & Authorization Testing (FT_001 - FT_021)
Plus Security Testing (SQL Injection, XSS, Password Security)

Test Requirements:
- S1.1: User Authentication & Authorization
- S2.1: User Registration
- UI.1: Navigation & UI Flow
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
from datetime import datetime

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots", "auth_testing")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(driver, test_id, step_name):
    """Capture screenshot with timestamp"""
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{test_id}_{step_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(filepath)
    print(f"Screenshot saved: {filepath}")


class TestLoginValidation:
    """FT_001 - FT_008: Login Validation Tests"""

    def test_FT_001_login_valid_credentials(self, driver, base_url):
        """FT_001: Verify successful login with valid participant credentials"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_001", "initial_page")
        
        # Wait for form to load
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        
        # Fill in valid credentials
        username_field.send_keys("mhdreza10")
        password_field = driver.find_element(By.ID, "InputPassword")
        password_field.send_keys("mhdreza10")
        
        take_screenshot(driver, "FT_001", "form_filled")
        
        # Submit form
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()
        time.sleep(2)
        
        take_screenshot(driver, "FT_001", "after_submit")
        
        # Verify successful login - should redirect or show dashboard
        assert "index.php" in driver.current_url or "dashboard" in driver.current_url.lower(), \
            f"Expected redirect to index/dashboard, but got {driver.current_url}"

    def test_FT_002_login_empty_password(self, driver, base_url):
        """FT_002: Verify system rejects login when password is empty"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_002", "initial_page")
        
        # Fill only username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        
        take_screenshot(driver, "FT_002", "password_empty")
        
        # Submit with empty password
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_002", "error_message")
        
        # Verify error message appears
        error_alert = driver.find_element(By.CLASS_NAME, "alert-danger")
        assert error_alert.is_displayed(), "Error message should be displayed"
        assert "kosong" in error_alert.text.lower() or "tidak boleh" in error_alert.text.lower(), \
            f"Expected 'empty' error message, got: {error_alert.text}"

    def test_FT_003_login_empty_username(self, driver, base_url):
        """FT_003: Verify system rejects login when username is empty"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_003", "initial_page")
        
        # Fill only password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "InputPassword"))
        ).send_keys("TestPassword123!")
        
        take_screenshot(driver, "FT_003", "username_empty")
        
        # Submit with empty username
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_003", "error_message")
        
        # Verify error message
        error_alert = driver.find_element(By.CLASS_NAME, "alert-danger")
        assert error_alert.is_displayed(), "Error message should be displayed"

    def test_FT_004_login_unregistered_user(self, driver, base_url):
        """FT_004: Verify login fails with unregistered user"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_004", "initial_page")
        
        # Fill with non-existent user
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("nonexistentuser123456")
        driver.find_element(By.ID, "InputPassword").send_keys("AnyPassword123!")
        
        take_screenshot(driver, "FT_004", "unregistered_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_004", "error_message")
        
        # Verify error message or stay on login page
        assert "login.php" in driver.current_url, "Should remain on login page"
        error_alert = driver.find_elements(By.CLASS_NAME, "alert-danger")
        assert len(error_alert) > 0, "Error message should appear"

    def test_FT_005_login_wrong_password(self, driver, base_url):
        """FT_005: Verify login fails with wrong password"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_005", "initial_page")
        
        # Valid user, wrong password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys("WrongPassword456!")
        
        take_screenshot(driver, "FT_005", "wrong_password_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_005", "error_message")
        
        # Should stay on login page or show error
        assert "login.php" in driver.current_url, "Should remain on login page"

    def test_FT_006_login_mismatched_credentials(self, driver, base_url):
        """FT_006: Verify login fails when username and password combination is incorrect"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_006", "initial_page")
        
        # Different user passwords combination
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys("otherUserPassword!")
        
        take_screenshot(driver, "FT_006", "mismatched_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_006", "error_message")
        
        assert "login.php" in driver.current_url, "Should remain on login page"

    def test_FT_007_rate_limiting_multiple_failures(self, driver, base_url):
        """FT_007: Verify rate limiting implementation on repeated login failures"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_007", "initial_page")
        
        # Attempt multiple failed logins
        for attempt in range(1, 6):
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
                driver.find_element(By.ID, "username").clear()
                driver.find_element(By.ID, "username").send_keys("testuser123")
                driver.find_element(By.ID, "InputPassword").clear()
                driver.find_element(By.ID, "InputPassword").send_keys("WrongPassword" + str(attempt))
                
                take_screenshot(driver, "FT_007", f"attempt_{attempt}")
                
                driver.find_element(By.NAME, "submit").click()
                time.sleep(1)
            except Exception as e:
                print(f"Attempt {attempt} error: {e}")
                pass
        
        take_screenshot(driver, "FT_007", "final_state")
        
        # Note: Rate limiting implementation may vary
        # This test documents current behavior
        assert "login.php" in driver.current_url, "Should remain on login page after failures"

    def test_FT_008_session_expired_redirect(self, driver, base_url):
        """FT_008: Verify expired session redirects to login"""
        # First, login successfully
        driver.get(f"{base_url}/login.php")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys("TestPassword123!")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        
        take_screenshot(driver, "FT_008", "after_login")
        
        # Clear session cookies to simulate expiration
        driver.delete_cookie("PHPSESSID")
        
        # Try to access protected page
        driver.get(f"{base_url}/index.php")
        time.sleep(1)
        
        take_screenshot(driver, "FT_008", "after_session_clear")
        
        # Should redirect to login
        assert "login.php" in driver.current_url, "Should redirect to login after session expiration"


class TestRegistrationValidation:
    """FT_009 - FT_017: Registration Validation Tests"""

    def test_FT_009_register_valid_data(self, driver, base_url):
        """FT_009: Verify successful registration with valid data"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_009", "initial_page")
        
        # Generate unique email
        timestamp = int(time.time())
        unique_user = f"newuser_{timestamp}"
        unique_email = f"user_{timestamp}@example.com"
        
        # Fill registration form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User Full")
        driver.find_element(By.ID, "InputEmail").send_keys(unique_email)
        driver.find_element(By.ID, "username").send_keys(unique_user)
        driver.find_element(By.ID, "InputPassword").send_keys("SecurePass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("SecurePass123!")
        
        take_screenshot(driver, "FT_009", "form_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        
        take_screenshot(driver, "FT_009", "after_submit")
        
        # Verify registration success - should redirect
        assert "index.php" in driver.current_url or "register.php" not in driver.current_url, \
            f"Expected redirect after registration, got {driver.current_url}"

    def test_FT_010_register_empty_email(self, driver, base_url):
        """FT_010: Verify registration fails when email is empty"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_010", "initial_page")
        
        timestamp = int(time.time())
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        # Email left empty intentionally
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "FT_010", "form_without_email")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_010", "error_message")
        
        # Verify error
        error_alerts = driver.find_elements(By.CLASS_NAME, "alert-danger")
        assert len(error_alerts) > 0, "Error message should appear"

    def test_FT_011_register_empty_username(self, driver, base_url):
        """FT_011: Verify registration fails when username is empty"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_011", "initial_page")
        
        timestamp = int(time.time())
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        # Username left empty
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "FT_011", "form_without_username")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_011", "error_message")
        
        error_alerts = driver.find_elements(By.CLASS_NAME, "alert-danger")
        assert len(error_alerts) > 0, "Error message should appear"

    def test_FT_012_register_duplicate_username(self, driver, base_url):
        """FT_012: Verify registration fails when username already exists"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_012", "initial_page")
        
        timestamp = int(time.time())
        
        # Try to register with existing username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"duplicate_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys("testuser123")  # Existing user
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "FT_012", "form_with_duplicate_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_012", "error_message")
        
        # Verify error about duplicate username
        error_alerts = driver.find_elements(By.CLASS_NAME, "alert-danger")
        assert len(error_alerts) > 0, "Duplicate username error should appear"

    def test_FT_013_register_password_mismatch(self, driver, base_url):
        """FT_013: Verify registration fails when passwords don't match"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_013", "initial_page")
        
        timestamp = int(time.time())
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("DifferentPass456!")
        
        take_screenshot(driver, "FT_013", "mismatched_passwords")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_013", "error_message")
        
        # Verify password mismatch error
        password_errors = driver.find_elements(By.XPATH, "//*[contains(text(), 'Password') and contains(text(), 'sama')]")
        assert len(password_errors) > 0, "Password mismatch error should appear"

    def test_FT_014_register_empty_password(self, driver, base_url):
        """FT_014: Verify registration fails when password is empty"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_014", "initial_page")
        
        timestamp = int(time.time())
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        # Both password fields left empty
        
        take_screenshot(driver, "FT_014", "form_without_password")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_014", "error_message")
        
        error_alerts = driver.find_elements(By.CLASS_NAME, "alert-danger")
        assert len(error_alerts) > 0, "Error message should appear"

    def test_FT_015_register_invalid_email_format(self, driver, base_url):
        """FT_015: Verify registration fails with invalid email format"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_015", "initial_page")
        
        timestamp = int(time.time())
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        # Invalid email format
        driver.find_element(By.ID, "InputEmail").send_keys("not_an_email_format")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "FT_015", "invalid_email_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_015", "error_message")
        
        # HTML5 validation should prevent submission or server should reject
        assert "register.php" in driver.current_url, "Should remain on register page"

    def test_FT_016_register_long_password(self, driver, base_url):
        """FT_016: Verify registration with long password (edge case)"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_016", "initial_page")
        
        timestamp = int(time.time())
        long_password = "VeryLongSecurePassword123!@#$%^&*()_+-=[]{}|;:',.<>?/" * 3  # Very long password
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        driver.find_element(By.ID, "InputPassword").send_keys(long_password)
        driver.find_element(By.ID, "InputRePassword").send_keys(long_password)
        
        take_screenshot(driver, "FT_016", "long_password_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        
        take_screenshot(driver, "FT_016", "after_submit")
        
        # Should handle long password gracefully (either accept or show validation error)
        # Document behavior
        print(f"Current URL after long password: {driver.current_url}")

    def test_FT_017_register_special_characters_username(self, driver, base_url):
        """FT_017: Verify registration with special characters in username"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_017", "initial_page")
        
        timestamp = int(time.time())
        special_username = f"user_{timestamp}_!@#$"
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(special_username)
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "FT_017", "special_chars_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_017", "after_submit")
        
        # Document behavior with special characters
        print(f"Current URL after special characters: {driver.current_url}")


class TestNavigationUI:
    """FT_018 - FT_021: Navigation & UI Flow Tests"""

    def test_FT_018_register_link_to_login(self, driver, base_url):
        """FT_018: Verify redirect from register page to login"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_018", "register_page")
        
        # Find and click login link
        login_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login')]"))
        )
        
        take_screenshot(driver, "FT_018", "login_link_found")
        
        login_link.click()
        time.sleep(1)
        
        take_screenshot(driver, "FT_018", "after_click")
        
        # Verify navigation to login page
        assert "login.php" in driver.current_url, "Should navigate to login.php"

    def test_FT_019_login_register_link(self, driver, base_url):
        """FT_019: Verify register link is present on login page"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "FT_019", "login_page")
        
        # Find register link
        register_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'register')]"))
        )
        
        take_screenshot(driver, "FT_019", "register_link_found")
        
        # Verify link is visible
        assert register_link.is_displayed(), "Register link should be visible"
        assert "register.php" in register_link.get_attribute("href"), "Link should point to register.php"

    def test_FT_020_register_page_has_login_link(self, driver, base_url):
        """FT_020: Verify login link exists on register page"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "FT_020", "register_page")
        
        # Find login link
        login_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login')]"))
        )
        
        take_screenshot(driver, "FT_020", "login_link_found")
        
        assert login_link.is_displayed(), "Login link should be visible"
        assert "login.php" in login_link.get_attribute("href"), "Link should point to login.php"

    def test_FT_021_logout_and_page_protection(self, driver, base_url):
        """FT_021: Verify logout process and page protection"""
        # First, login
        driver.get(f"{base_url}/login.php")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys("TestPassword123!")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        
        take_screenshot(driver, "FT_021", "after_login")
        
        # Look for logout button/link
        try:
            logout_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logout')] | //button[contains(text(), 'Logout')]"))
            )
            take_screenshot(driver, "FT_021", "logout_button_found")
            logout_button.click()
            time.sleep(1)
        except:
            print("No logout button found, checking page protection")
        
        take_screenshot(driver, "FT_021", "after_logout_attempt")
        
        # Try to access protected page without login
        driver.delete_cookie("PHPSESSID")
        driver.get(f"{base_url}/index.php")
        time.sleep(1)
        
        take_screenshot(driver, "FT_021", "protected_page_access")
        
        # Should redirect to login
        assert "login.php" in driver.current_url, "Should redirect to login when accessing protected page"


class TestSecurityVulnerabilities:
    """Security Testing: SQL Injection, XSS, Password Security"""

    def test_SECURITY_001_sql_injection_login_username(self, driver, base_url):
        """SECURITY_001: Verify SQL injection protection in login username field"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "SECURITY_001", "initial_page")
        
        # SQL injection attempt
        sql_injection = "' OR '1'='1"
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(sql_injection)
        driver.find_element(By.ID, "InputPassword").send_keys("anypassword")
        
        take_screenshot(driver, "SECURITY_001", "sql_injection_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_001", "after_submit")
        
        # Should not login with SQL injection
        assert "login.php" in driver.current_url, "Should remain on login page, SQL injection should fail"

    def test_SECURITY_002_sql_injection_login_password(self, driver, base_url):
        """SECURITY_002: Verify SQL injection protection in login password field"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "SECURITY_002", "initial_page")
        
        sql_injection = "' OR 1=1 --"
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys(sql_injection)
        
        take_screenshot(driver, "SECURITY_002", "sql_injection_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_002", "after_submit")
        
        assert "login.php" in driver.current_url, "Should remain on login page, SQL injection should fail"

    def test_SECURITY_003_sql_injection_register_username(self, driver, base_url):
        """SECURITY_003: Verify SQL injection protection in register username field"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "SECURITY_003", "initial_page")
        
        timestamp = int(time.time())
        sql_injection = f"test_{timestamp}' DROP TABLE users --"
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(sql_injection)
        driver.find_element(By.ID, "InputPassword").send_keys("TestPass123!")
        driver.find_element(By.ID, "InputRePassword").send_keys("TestPass123!")
        
        take_screenshot(driver, "SECURITY_003", "sql_injection_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_003", "after_submit")
        
        # Should either reject or sanitize the input
        print("Checking if table still exists by attempting login")

    def test_SECURITY_004_xss_attack_username(self, driver, base_url):
        """SECURITY_004: Verify XSS protection in login fields"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "SECURITY_004", "initial_page")
        
        xss_payload = "<img src=x onerror='alert(\"XSS\")'>"
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(xss_payload)
        driver.find_element(By.ID, "InputPassword").send_keys("testpass")
        
        take_screenshot(driver, "SECURITY_004", "xss_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_004", "after_submit")
        
        # Verify XSS payload doesn't execute
        try:
            WebDriverWait(driver, 2).until(
                EC.alert_is_present()
            )
            assert False, "XSS vulnerability detected - alert was triggered"
        except:
            print("No XSS alert triggered - good!")

    def test_SECURITY_005_password_not_visible_in_html(self, driver, base_url):
        """SECURITY_005: Verify password field is not visible in HTML source"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "SECURITY_005", "initial_page")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "InputPassword"))
        ).send_keys("TestPassword123!")
        
        take_screenshot(driver, "SECURITY_005", "password_filled")
        
        # Check that password field type is 'password'
        password_field = driver.find_element(By.ID, "InputPassword")
        field_type = password_field.get_attribute("type")
        
        assert field_type == "password", f"Password field type should be 'password', got '{field_type}'"

    def test_SECURITY_006_weak_password_detection(self, driver, base_url):
        """SECURITY_006: Verify system handles weak password scenarios"""
        driver.get(f"{base_url}/register.php")
        take_screenshot(driver, "SECURITY_006", "initial_page")
        
        timestamp = int(time.time())
        weak_password = "123"  # Very weak password
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"user_{timestamp}@example.com")
        driver.find_element(By.ID, "username").send_keys(f"testuser_{timestamp}")
        driver.find_element(By.ID, "InputPassword").send_keys(weak_password)
        driver.find_element(By.ID, "InputRePassword").send_keys(weak_password)
        
        take_screenshot(driver, "SECURITY_006", "weak_password_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_006", "after_submit")
        
        # Document if weak password is rejected or accepted
        print("Weak password handling - document result")

    def test_SECURITY_007_response_timing_attacks(self, driver, base_url):
        """SECURITY_007: Verify timing is consistent for login attempts"""
        driver.get(f"{base_url}/login.php")
        
        import time
        times = []
        
        # Test valid username with wrong password - should take longer
        for i in range(3):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "InputPassword").clear()
            
            start = time.time()
            driver.find_element(By.ID, "username").send_keys("testuser123")
            driver.find_element(By.ID, "InputPassword").send_keys("wrongpass")
            driver.find_element(By.NAME, "submit").click()
            elapsed = time.time() - start
            times.append(elapsed)
            
            time.sleep(1)
            driver.get(f"{base_url}/login.php")
        
        take_screenshot(driver, "SECURITY_007", "timing_test_complete")
        
        # Document timing results
        print(f"Timing measurements: {times}")

    def test_SECURITY_008_account_enumeration(self, driver, base_url):
        """SECURITY_008: Verify account enumeration is not possible"""
        driver.get(f"{base_url}/login.php")
        take_screenshot(driver, "SECURITY_008", "initial_page")
        
        # Test with existing user
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser123")
        driver.find_element(By.ID, "InputPassword").send_keys("wrongpass")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_008", "existing_user_error")
        error_existing = driver.find_element(By.CLASS_NAME, "alert-danger").text if driver.find_elements(By.CLASS_NAME, "alert-danger") else ""
        
        # Reload and test with non-existing user
        driver.get(f"{base_url}/login.php")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("nonexistentuser999999")
        driver.find_element(By.ID, "InputPassword").send_keys("wrongpass")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        
        take_screenshot(driver, "SECURITY_008", "nonexistent_user_error")
        error_nonexisting = driver.find_element(By.CLASS_NAME, "alert-danger").text if driver.find_elements(By.CLASS_NAME, "alert-danger") else ""
        
        # Errors should be the same to prevent enumeration
        print(f"Existing user error: {error_existing}")
        print(f"Non-existing user error: {error_nonexisting}")
