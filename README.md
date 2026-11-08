<div align="center">
  <img src="assets/images/logo.svg" alt="Hiddify Personal Edition logo" width="88" />
  <h1>Hiddify Personal Edition</h1>
  <p>Open-source VPN and proxy client for Android, Windows, macOS, Linux, and iPhone</p>
  <p>Powered by sing-box · VLESS · VMess · Reality · Trojan · Shadowsocks · Hysteria2 · TUIC · WireGuard</p>
  <p>
    <a href="https://hiddify.org">Website</a> ·
    <a href="https://hiddify.org/help">Help and install guide</a> ·
    <a href="https://t.me/HiddifyConfig">Telegram channel</a> ·
    <a href="https://github.com/HiddifyApp/hiddify-app">Source code</a>
  </p>
</div>

<div align="center">

[![Latest release](https://img.shields.io/github/v/release/HiddifyApp/hiddify-app?style=flat-square&logo=github)](https://github.com/HiddifyApp/hiddify-app/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/HiddifyApp/hiddify-app/total?style=flat-square&logo=github)](https://github.com/HiddifyApp/hiddify-app/releases)
[![Telegram](https://img.shields.io/badge/Telegram-%40HiddifyConfig-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/HiddifyConfig)

</div>

<a id="english"></a>
## English

Hiddify Personal Edition is an independent, open-source VPN and proxy client based on the [Hiddify app](https://github.com/hiddify/hiddify-app) and [sing-box](https://github.com/SagerNet/sing-box). Import a proxy link or subscription, choose a server, and connect from one app on Android, Windows, macOS, or Linux.

This personal distribution keeps its own branding, release versions, download links, website, and support channel. It is not the official Hiddify distribution and is not published to the official app stores.

### Download Hiddify

| Platform | Recommended download |
| --- | --- |
| Android | [Universal APK](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Android-universal.apk) |
| Windows 10/11 | [Setup (installer)](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) · [Portable ZIP](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Windows-Portable-x64.zip) |
| macOS | [Universal DMG](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg) |
| Linux | [AppImage](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Linux-x64-AppImage.AppImage) · [Debian package](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Debian-x64.deb) |
| iPhone | [IPA for TrollStore / jailbreak](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa) · [App source](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json) — see [iPhone install](#iphone-install) |

[All downloads, checksums, and multilingual installation guides](https://github.com/HiddifyApp/hiddify-app/releases/latest)

### Install and connect

- **Android:** Open the downloaded APK and allow installation if prompted.
- **Windows:** Run the Setup and follow the installer; the app then updates itself. Or extract the Portable ZIP and run `Hiddify.exe`. These builds are unsigned: if SmartScreen warns, choose **More info → Run anyway**.
- **macOS:** Open the DMG and move Hiddify to Applications.
- **Linux:** Make the AppImage executable and run it. Debian users can install the DEB package.
- **iPhone:** see [iPhone install](#iphone-install) below.
- Add your proxy subscription or configuration link, select a server, and tap **Connect**.

<a id="iphone-install"></a>
### iPhone install

Apple only lets VPN apps run when they are signed with a certificate that allows Network Extensions. Pick the way that matches your iPhone:

| Your iPhone | How to install | Lasts |
| --- | --- | --- |
| iOS 14.0 – 16.6.1, 16.7 RC or 17.0 with **TrollStore** | In TrollStore tap **+ → Install from URL** and paste `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa` | Permanent, free |
| **Jailbroken** iPhone | Download the [IPA](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa) and install it with Filza / AppSync | Permanent, free |
| Any iOS with **ESign, Feather, Scarlet, SideStore or AltStore** and your own certificate | Open **Sources → +**, add `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json`, then install Hiddify from the list. Updates show up there too. | As long as your certificate (usually 1 year) |

- With a certificate, the VPN connects only if that certificate supports **Network Extension / VPN**. Ask before you buy one.
- Free Apple-ID sideloading (7-day signing) cannot run VPN apps.
- Avoid "certificate sellers" and app stores you don't trust: a modified VPN app can read all your traffic.

### Features

- Automatic server selection and connection testing
- Remote subscriptions with automatic profile updates
- TUN/VPN mode and per-profile traffic and expiry information
- Support for VLESS, VMess, Reality, Trojan, Shadowsocks, Hysteria, Hysteria2, TUIC, WireGuard, SSH, and compatible sing-box profiles
- Open-source code with scheduled upstream app and core updates

### Automatic updates

GitHub Actions checks the upstream app and core every six hours. Compatible upstream app changes are merged into this fork, assigned a unique personal version, and released with this fork's branding. If upstream changes conflict with personal edits, syncing stops instead of overwriting them.

<a id="persian"></a>
## فارسی

Hiddify Personal Edition یک کلاینت متن‌باز VPN و پراکسی بر پایه‌ی sing-box است. لینک یا اشتراک پراکسی خود را اضافه کنید، سرور را انتخاب کنید و در Android، Windows، macOS، Linux یا آیفون متصل شوید.

این نسخه مستقل است و لینک دانلود، شماره نسخه، وب‌سایت و پشتیبانی اختصاصی خودش را دارد؛ نسخه‌ی رسمی Hiddify نیست و در فروشگاه‌های رسمی منتشر نمی‌شود.

- **دانلود:** [آخرین نسخه و فایل‌های همه‌ی سیستم‌عامل‌ها](https://github.com/HiddifyApp/hiddify-app/releases/latest)
- **نصب:** APK را در Android باز کنید؛ در Windows (۱۰ و ۱۱) فایل [Setup](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe) را اجرا کنید تا نصب شود و بعد خودش به‌روز می‌شود (یا Portable را از حالت فشرده خارج و `Hiddify.exe` را اجرا کنید)؛ در macOS فایل DMG را به Applications منتقل کنید؛ در Linux، AppImage را اجرایی کنید یا بسته‌ی Debian را نصب کنید.
- **اتصال:** لینک یا اشتراک را اضافه کنید، سرور را برگزینید و **اتصال** را بزنید.
- **پروتکل‌ها:** VLESS، VMess، Reality، Trojan، Shadowsocks، Hysteria، Hysteria2، TUIC، WireGuard و SSH.

### نصب روی آیفون

اپل فقط وقتی اجازه اجرای برنامه VPN را می‌دهد که با گواهی‌ای امضا شده باشد که اجازه Network Extension دارد. روش مناسب گوشی خود را انتخاب کنید:

| آیفون شما | روش نصب | مدت اعتبار |
| --- | --- | --- |
| iOS 14.0 تا 16.6.1، 16.7 RC یا 17.0 با **TrollStore** | در TrollStore روی **+ ← Install from URL** بزنید و این لینک را وارد کنید: `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa` | دائمی و رایگان |
| آیفون **جیلبریک‌شده** | [فایل IPA](https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa) را دانلود و با Filza / AppSync نصب کنید | دائمی و رایگان |
| هر نسخه iOS با **ESign، Feather، Scarlet، SideStore یا AltStore** و گواهی شخصی | به **Sources ← +** بروید، این آدرس را اضافه کنید: `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json` و Hiddify را از فهرست نصب کنید؛ آپدیت‌ها هم همان‌جا می‌آیند | تا وقتی گواهی شما معتبر است (معمولاً یک سال) |

- اگر با گواهی نصب می‌کنید، VPN فقط وقتی وصل می‌شود که گواهی از **Network Extension / VPN** پشتیبانی کند؛ قبل از خرید حتماً بپرسید.
- نصب با Apple ID رایگان (امضای ۷ روزه) برنامه VPN را اجرا نمی‌کند.
- از فروشندگان گواهی و فروشگاه‌های ناشناس دوری کنید؛ نسخه دست‌کاری‌شده VPN می‌تواند همه ترافیک شما را ببیند.

[راهنما و پشتیبانی](https://hiddify.org/help) · [کانال تلگرام](https://t.me/HiddifyConfig) · [کد منبع](https://github.com/HiddifyApp/hiddify-app)

<a id="burmese"></a>
## မြန်မာ

Hiddify Personal Edition သည် sing-box ကို အခြေခံထားသော open-source VPN နှင့် proxy client ဖြစ်သည်။ Proxy link သို့မဟုတ် subscription ကို ထည့်ပြီး Android၊ Windows၊ macOS နှင့် Linux တွင် server ရွေးချယ်ကာ ချိတ်ဆက်နိုင်သည်။

ဤသည် ကိုယ်ပိုင် branding၊ version၊ download link နှင့် support channel ပါသော သီးခြား build ဖြစ်ပြီး တရားဝင် Hiddify ဖြန့်ချိမှု သို့မဟုတ် official app store ထုတ်ဝေမှု မဟုတ်ပါ။

- **ဒေါင်းလုဒ်:** [နောက်ဆုံးဗားရှင်းနှင့် platform ဖိုင်များ](https://github.com/HiddifyApp/hiddify-app/releases/latest)
- **ထည့်သွင်းရန်:** Android တွင် APK ကိုဖွင့်ပါ။ Windows တွင် Setup ကိုဖွင့်၍ ထည့်သွင်းပါ (သို့မဟုတ် Portable ZIP ကိုဖြည်ပြီး `Hiddify.exe` ကိုဖွင့်ပါ)။ macOS တွင် DMG ကိုဖွင့်ပြီး Applications ထဲသို့ ရွှေ့ပါ။ Linux တွင် AppImage ကို executable လုပ်ပါ သို့မဟုတ် Debian package ကိုထည့်သွင်းပါ။
- **iPhone:** TrollStore (iOS 14–17.0) ဖြင့် **Install from URL** တွင် `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa` ကိုထည့်ပါ။ ESign/Feather/SideStore အသုံးပြုသူများ source `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json` ကိုထည့်ပါ။ [အသေးစိတ်](#iphone-install)
- **ချိတ်ဆက်ရန်:** Subscription သို့မဟုတ် proxy link ထည့်ပြီး server ရွေးကာ **Connect** ကိုနှိပ်ပါ။
- **ပံ့ပိုးသော protocol များ:** VLESS၊ VMess၊ Reality၊ Trojan၊ Shadowsocks၊ Hysteria၊ Hysteria2၊ TUIC၊ WireGuard နှင့် SSH။

[အကူအညီ](https://hiddify.org/help) · [Telegram](https://t.me/HiddifyConfig) · [Source code](https://github.com/HiddifyApp/hiddify-app)

<a id="chinese"></a>
## 简体中文

Hiddify Personal Edition 是一款基于 sing-box 的开源 VPN 与代理客户端。添加代理链接或订阅后，即可在 Android、Windows、macOS 和 Linux 上选择服务器并连接。

这是拥有独立品牌、版本、下载地址和支持渠道的个人发行版，并非 Hiddify 官方发行版，也不发布在官方应用商店。

- **下载：**[最新版及各平台文件](https://github.com/HiddifyApp/hiddify-app/releases/latest)
- **安装：**Android 打开 APK；Windows 运行 Setup 安装（或解压 Portable ZIP 并运行 `Hiddify.exe`）；macOS 打开 DMG 并将应用拖入 Applications；Linux 为 AppImage 添加可执行权限，或安装 Debian 包。
- **iPhone：**TrollStore（iOS 14–17.0）中选择 **Install from URL** 并粘贴 `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa`；ESign/Feather/SideStore 用户添加源 `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json`。[详情](#iphone-install)
- **连接：**添加订阅或代理链接，选择服务器，然后点击**连接**。
- **支持协议：**VLESS、VMess、Reality、Trojan、Shadowsocks、Hysteria、Hysteria2、TUIC、WireGuard 和 SSH。

[帮助与安装指南](https://hiddify.org/help) · [Telegram 频道](https://t.me/HiddifyConfig) · [源代码](https://github.com/HiddifyApp/hiddify-app)

<a id="turkmen"></a>
## Türkmençe

Hiddify Personal Edition, sing-box esasynda döredilen açyk kodly VPN we proksi müşderisidir. Proksi salgysyny ýa-da abunalygy goşuň, serweri saýlaň we Android, Windows, macOS ýa-da Linux arkaly birigiň.

Bu öz brendi, wersiýasy, ýükläp almak salgylary we goldaw kanaly bolan şahsy paýlanyşdyr. Resmi Hiddify wersiýasy däl we resmi programma dükanlarynda çap edilmeýär.

- **Ýüklemek:** [Soňky wersiýa we ähli platforma faýllary](https://github.com/HiddifyApp/hiddify-app/releases/latest)
- **Gurnamak:** Android-de APK-ny açyň. Windows-da Setup faýlyny işledip gurnaň (ýa-da Portable ZIP-i çykaryp `Hiddify.exe`-ni işlediň). macOS-da DMG-ni açyp programmany Applications bukjasyna geçiriň. Linux-da AppImage faýlyna işletmek rugsadyny beriň ýa-da Debian paketini gurnap bilersiňiz.
- **iPhone:** TrollStore-da (iOS 14–17.0) **Install from URL** saýlap `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/Hiddify-iOS-Jailbreak.ipa` goýuň. ESign/Feather/SideStore ulanyjylary `https://github.com/HiddifyApp/hiddify-app/releases/latest/download/hiddify-ios-source.json` çeşmesini goşsun. [Giňişleýin](#iphone-install)
- **Birikmek:** Abunalygy ýa-da proksi salgysyny goşuň, serweri saýlaň we **Connect** düwmesine basyň.
- **Protokollar:** VLESS, VMess, Reality, Trojan, Shadowsocks, Hysteria, Hysteria2, TUIC, WireGuard we SSH.

[Kömek we gurnama gollanmasy](https://hiddify.org/help) · [Telegram kanaly](https://t.me/HiddifyConfig) · [Çeşme kody](https://github.com/HiddifyApp/hiddify-app)