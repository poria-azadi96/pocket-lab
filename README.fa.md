<div align="center">

# 📱 Pocket Lab | آزمایشگاه محاسباتی در جیب
### شبیه‌سازی‌های علمی و مدل‌سازی ریاضی، مستقیم روی پردازنده گوشی هوشمند

[English](README.md) • [فارسی](README.fa.md)

[![GitHub Profile](https://img.shields.io/badge/GitHub-poria--azadi96-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/poria-azadi96)
[![Telegram Channel](https://img.shields.io/badge/Telegram-The%20Maze-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/the_maze2022)
[![Instagram](https://img.shields.io/badge/Instagram-poria__azadi__official-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/poria_azadi_official/)
[![YouTube](https://img.shields.io/badge/YouTube-PoriaAzadi__official-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@PoriaAzadi_official)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Poria%20Azadi-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Poria-Azadi-2)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![OS](https://img.shields.io/badge/Env-Termux%20%7C%20Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://termux.dev/)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Colab-4CAF50?style=flat-square)](https://github.com/poria-azadi96/pocket-lab)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

<p align="center">
  <b>«گوشی هوشمند در جیب شما صرفاً ابزاری برای مصرف محتوا نیست؛ می‌تواند یک بستر واقعی برای مدل‌سازی و شبیه‌سازی پدیده‌های شگفت‌انگیز جهان باشد.»</b>
</p>

[درباره پروژه](#about) •
[فهرست اپیزودها](#episodes) •
[راه‌اندازی سریع](#quickstart) •
[ساختار فایل‌ها](#structure) •
[کانال تلگرام](https://t.me/the_maze2022)

---

</div>

<div dir="rtl">

<a id="about"></a>
## 🧬 درباره پروژه

گوشی‌های هوشمند امروزی مجهز به پردازنده‌های چند‌هسته‌ای قدرتمندی هستند که توان محاسباتی آن‌ها از کامپیوترهای غول‌آسای نسل‌های پیشین فراتر است. هدف پروژه **Pocket Lab** این است که نشان دهد برای ورود به دنیای فیزیک محاسباتی، نظریه آشوب، و پویایی سیستم‌های غیرخطی، لزوماً نیازی به کلاسترهای پردازشی یا لپ‌تاپ‌های گران‌قیمت ندارید.

در این سری آموزشی، بدون ساده‌سازی‌های غیرعلمی، دستگاه معادلات دیفرانسیل و الگوریتم‌های پیچیده طبیعت را مستقیماً روی بستر لینوکس بومی موبایل اجرا و انیمیت می‌کنیم.

---

<a id="episodes"></a>
## 🎬 فهرست شبیه‌سازی‌ها (Episodes)

| # | عنوان شبیه‌سازی | پدیده علمی | وضعیت | سورس کد | اجرای ابری |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **00** | **راه‌اندازی کارگاه جیبی** | راه‌اندازی لینوکس اوبونتو و پایتون بومی روی ترموکس | ✅ تکمیل | [راهنما](episodes/ep00-environment-setup/) | — |
| **01** | **آونگ دوتایی (Double Pendulum)** | نظریه آشوب معین و حساسیت به شرایط اولیه (۱° اختلاف) | ✅ تکمیل | [کد پایتون](episodes/ep01-double-pendulum/double_pendulum.py) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| **02** | **پرواز هماهنگ پرندگان (Boids)** | برآیش (Emergence) و هوش جمعی خودسامانده | ✅ تکمیل | [کد پایتون](episodes/ep02-boids-flocking/boids_simulation_20s.py) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| **03** | **بازی زندگی کانوی (Game of Life)** | اتوماتای سلولی و خلق حیات از دل قوانین ساده | ⏳ به‌زودی | — | — |
| **04** | **دینامیک بیماری‌ها (SIR Model)** | مدل‌سازی ریاضی انتقال ویروس و شکست زنجیره | ⏳ به‌زودی | — | — |

---

<a id="quickstart"></a>
## 🚀 شروع سریع (Quick Start)

### مسیر اول: اجرای بومی در اندروید (آفلاین و بدون نیاز به اینترنت)

۱. نرم‌افزار **Termux** را حتماً از [نسخه‌های رسمی گیت‌هاب](https://github.com/termux/termux-app/releases) یا F-Droid دانلود و نصب کنید (از گوگل‌پلی دانلود نکنید).

۲. محیط لینوکس اوبونتو را نصب کرده و وارد آن شوید:
```bash
pkg install proot-distro -y
proot-distro install ubuntu
proot-distro login ubuntu
```

۳. بسته‌های اصلی پایتون و رندر نمودارها را نصب کنید:
```bash
apt update && apt install python3 python3-numpy python3-matplotlib python3-pil -y
```

۴. اسکریپت شبیه‌سازی هر اپیزود را اجرا کنید:
```bash
# اجرای اپیزود ۱: آشوب آونگ دوتایی
python3 episodes/ep01-double-pendulum/double_pendulum.py

# اجرای اپیزود ۲: هوش جمعی و پرواز پرندگان
python3 episodes/ep02-boids-flocking/boids_simulation_20s.py
```

### مسیر دوم: اجرای تک‌کلیک ابری (iOS و مرورگر)

کاربران آیفون یا دوستانی که بدون درگیر شدن با ترمینال می‌خواهند کدها را اجرا کنند، کافی است روی نشان **Open in Colab** در جدول بالا کلیک کرده و اسکریپت را آنلاین اجرا کنند.

---

<a id="structure"></a>
## 📁 ساختار فایل‌ها

```text
pocket-lab/
│
├── README.md                   # مستندات انگلیسی مخزن
├── README.fa.md                # مستندات فارسی مخزن
├── LICENSE                     # پروانه استفاده متن‌باز (MIT)
│
└── episodes/
    ├── ep00-environment-setup/ # راهنمای راه‌اندازی زیرساخت لینوکس
    │   └── README.md
    │
    ├── ep01-double-pendulum/    # شبیه‌سازی آونگ دوتایی و نظریه آشوب
    │   ├── double_pendulum.py  # اسکریپت اصلی حل معادلات و رندر گیف
    │   ├── README.md           # تحلیل فیزیکی و استخراج معادلات لاگرانژ (EN)
    │   └── README.fa.md        # راهنمای جامع و تحلیل علمی به زبان فارسی (FA)
    │
    ├── ep02-boids-flocking/    # شبیه‌سازی پرواز جمعی بویدز و پدیداری
    │   ├── boids_simulation_20s.py # موتور محاسباتی برداری و رندر HUD
    │   ├── README.md           # مبانی نظری و فرمول‌های برداری رینولدز (EN)
    │   └── README.fa.md        # راهنمای جامع و تحلیل فازهای دینامیکی (FA)
    │
    ├── ep03-game-of-life/      # اتوماتای سلولی کانوی (به‌زودی)
    └── ep04-epidemic-sir/      # مدل‌سازی ریاضی شیوع بیماری (به‌زودی)
```

---

## 🌐 ارتباط، دریافت فایل‌ها و پشتیبانی

* 📢 **کانال تلگرام:** دانلود اسکریپت‌های آماده، فایل‌های متنی کپی‌پیست و رفع ارورها  
  👉 [ورود به کانال تلگرام The Maze (@the_maze2022)](https://t.me/the_maze2022)

* 📸 **اینستاگرام:** تماشای ریلزها و پیش‌نمایش ویدئویی شبیه‌سازی‌ها  
  👉 [صفحه رسمی پوریا آزادی (@poria_azadi_official)](https://www.instagram.com/poria_azadi_official/)

* 🎥 **یوتیوب:** ویدیوهای تحلیلی و آموزشی جامع‌تر  
  👉 [کانال یوتیوب (@PoriaAzadi_official)](https://www.youtube.com/@PoriaAzadi_official)

* 🔬 **ریسرچ‌گیت:** مقالات و سوابق دانشگاهی  
  👉 [پروفایل ResearchGate پوریا آزادی](https://www.researchgate.net/profile/Poria-Azadi-2)

</div>

---

<div align="center">
  <sub>طراحی و توسعه توسط <b>پوریا آزادی</b> • منتشر شده تحت پروانه <a href="LICENSE">MIT</a></sub>
</div>
