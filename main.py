# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time

# Discord Webhook URL (請替換成你的實際 URL)
DISCORD_WEBHOOK_URL = '你的 Discord Webhook URL'

# 目標網址
URL = 'https://museum-tickets.nintendo.com/en/calendar'


def send_discord_notify(message: str) -> None:
    """發送通知到 Discord Webhook"""
    payload = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("✅ Discord 通知成功")
        else:
            print(f"⚠️ Discord 通知失敗：{response.status_code}, {response.text}")
    except Exception as e:
        print(f"⚠️ Discord 通知例外：{e}")


def check_tickets(driver) -> None:
    """檢查票務狀態，若有票則發送通知"""
    print("🔍 檢查中...")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sale_dates = []

    # 找出所有月份區塊
    month_blocks = soup.find_all('div', class_='swiper-slide')
    for month_block in month_blocks:
        # 找出所有日期的 td 標籤
        date_cells = month_block.find_all('td')
        for cell in date_cells:
            aria_label = cell.get('data-date')
            if not aria_label:
                continue
            ticket_div = cell.find('div', class_='fc-event-main')
            if not ticket_div:
                continue
            span = ticket_div.find('span')
            if not span:
                continue
            classes = span.get("class", [])
            # 有 "sale" class 就代表有票
            if "sale" in classes:
                sale_dates.append(aria_label)

    if sale_dates:
        notify_message = "🎉 Nintendo Museum 有票啦！\n" + "\n".join(sale_dates)
        print("✅ 有票，通知發送中！")
        send_discord_notify(notify_message)
    else:
        print("❌ 沒有票！")

    print("🔍 檢查結束！")


def main():
    send_discord_notify("🔔 開始檢查票務狀態...")
    # 設定 Chrome Driver (自動管理 driver 版本)
    options = Options()
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(URL)
        time.sleep(5)  # 等待頁面及 JS 載入
        while True:
            driver.refresh()
            time.sleep(5)
            check_tickets(driver)
            time.sleep(120)  # 每2分鐘檢查一次
    except Exception as e:
        print("⚠️ 發生錯誤：", e)
    finally:
        if 'driver' in locals():
            driver.quit()
        send_discord_notify("🔔 停止檢查票務狀態...")


if __name__ == "__main__":
    main()
