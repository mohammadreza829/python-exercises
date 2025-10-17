import keyboard # type: ignore

print("لطفاً دکمه‌ی Win رو فشار بده... (برای خروج، دکمه‌ی Esc رو بزن)")

while True:
    if keyboard.is_pressed('windows'):
        print("✅ دکمه‌ی Win شناسایی شد!")
        break
    elif keyboard.is_pressed('esc'):
        print("⛔️ خروج از برنامه.")
        break

