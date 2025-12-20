# فایل: test1_open_browser.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

print("🔵 شروع تست 1: باز کردن مرورگر")

driver_path = "chromedriver.exe"   # کنار test.py باشد

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

print("✅ مرورگر باز شد!")

driver.get("https://www.google.com")
print("📍 رفتیم به گوگل")

time.sleep(5)

driver.quit()
print("👋 مرورگر بسته شد")
