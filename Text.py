# فایل: test1_open_browser.py

from selenium import webdriver
import time

print("🔵 شروع تست 1: باز کردن مرورگر")

# مسیر chromedriver
driver_path = "chromedriver.exe"  # کنار فایل پایتون باشه

# ساخت درایور
driver = webdriver.Chrome(executable_path=driver_path)

print("✅ مرورگر باز شد!")

# رفتن به گوگل برای تست
driver.get("https://www.google.com")

print("📍 رفتیم به گوگل")
print("⏰ 5 ثانیه صبر می‌کنیم...")

time.sleep(5)

# بستن مرورگر
driver.quit()
print("👋 مرورگر بسته شد")
