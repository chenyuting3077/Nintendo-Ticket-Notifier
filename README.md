<h1 align="center">🎟 Nintendo-Ticket-Notifier </h1>

<p align="center">
  自動檢查任天堂博物館票務網站是否開放售票，並透過 Discord Webhook 即時通知！
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Selenium-Automation-brightgreen" alt="Selenium">
  <img src="https://img.shields.io/badge/Discord-Webhook-blueviolet" alt="Discord Webhook">
</p>

---

## ✨ 功能介紹

- ⏰ 每兩分鐘自動檢查一次票務狀態
- 🖥 使用 Selenium 模擬瀏覽器操作並抓取資料
- 🔍 BeautifulSoup 解析售票資訊
- 📣 發現開賣時自動透過 Discord Webhook 通知你

## 🔧 安裝與使用

### 1. 安裝依賴套件

```bash
pip install selenium webdriver-manager beautifulsoup4 requests
```

### 2. 設定 Discord Webhook

編輯 `main.py`，將以下變數替換為你自己的 Discord Webhook：

```python
DISCORD_WEBHOOK_URL = '你的 Discord Webhook URL'
```

### 3. 執行程式

```bash
python main.py
```

程式會開啟瀏覽器、前往任天堂博物館票務頁面，並每兩分鐘檢查一次是否開賣，有票就會即時通知！

## 🧠 技術細節

- **Selenium**：操作與模擬瀏覽器行為
- **BeautifulSoup**：解析 HTML 結構
- **webdriver-manager**：自動管理 ChromeDriver
- **requests**：與 Discord Webhook 溝通

## ⚠️ 注意事項

- 須具備 Chrome 瀏覽器環境
- 程式會開啟瀏覽器視窗，如需無頭模式請自行修改 Chrome Options 設定
- 網站結構若改動可能會影響爬蟲功能

## 📜 License

本專案使用 MIT License 授權，歡迎自由使用與修改。

---

> 對這個工具有任何建議或問題，歡迎開 issue 或 pull request！
