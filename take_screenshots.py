import os
import sys
from playwright.sync_api import sync_playwright

def main():
    os.makedirs('screenshots', exist_ok=True)
    with sync_playwright() as p:
        # Launch Chromium (or system Edge/Chrome if needed)
        try:
            browser = p.chromium.launch(headless=True)
        except Exception as e:
            print(f"Standard chromium launch failed ({e}), trying channel msedge or chrome...")
            try:
                browser = p.chromium.launch(channel="msedge", headless=True)
            except Exception:
                browser = p.chromium.launch(channel="chrome", headless=True)

        # 1. Desktop Screenshot (1440px width)
        desktop_page = browser.new_page(viewport={'width': 1440, 'height': 900})
        print("Navigating to Desktop view (1440px)...")
        try:
            desktop_page.goto('http://127.0.0.1:8000', wait_until='networkidle', timeout=15000)
        except Exception:
            desktop_page.goto('http://127.0.0.1:8000', wait_until='domcontentloaded')
        desktop_page.wait_for_timeout(2500)
        
        # Capture full page and specific sections
        desktop_path = os.path.abspath('screenshots/desktop_1440.png')
        desktop_page.screenshot(path=desktop_path, full_page=True)
        print(f"Desktop screenshot saved to {desktop_path}")
        
        # Hero specific screenshot
        hero_elem = desktop_page.locator('header').first
        if hero_elem.count() > 0:
            hero_elem.screenshot(path=os.path.abspath('screenshots/desktop_hero_1440.png'))
            print("Desktop Hero screenshot saved")

        # Bottom CTA banner specific screenshot
        sections = desktop_page.locator('section').all()
        # Bottom banner is the section with bg-[#FFFF55]
        bottom_banner = desktop_page.locator('section.bg-\\[\\#FFFF55\\]').first
        if bottom_banner.count() > 0:
            bottom_banner.screenshot(path=os.path.abspath('screenshots/desktop_bottom_cta_1440.png'))
            print("Desktop Bottom CTA screenshot saved")
        desktop_page.close()

        # 2. Mobile Screenshot (375px width, iPhone-like viewport)
        mobile_page = browser.new_page(viewport={'width': 375, 'height': 812})
        print("Navigating to Mobile view (375px)...")
        try:
            mobile_page.goto('http://127.0.0.1:8000', wait_until='networkidle', timeout=15000)
        except Exception:
            mobile_page.goto('http://127.0.0.1:8000', wait_until='domcontentloaded')
        mobile_page.wait_for_timeout(2500)
        
        mobile_path = os.path.abspath('screenshots/mobile_375.png')
        mobile_page.screenshot(path=mobile_path, full_page=True)
        print(f"Mobile screenshot saved to {mobile_path}")

        mobile_hero = mobile_page.locator('header').first
        if mobile_hero.count() > 0:
            mobile_hero.screenshot(path=os.path.abspath('screenshots/mobile_hero_375.png'))
            print("Mobile Hero screenshot saved")

        mobile_bottom_banner = mobile_page.locator('section.bg-\\[\\#FFFF55\\]').first
        if mobile_bottom_banner.count() > 0:
            mobile_bottom_banner.screenshot(path=os.path.abspath('screenshots/mobile_bottom_cta_375.png'))
            print("Mobile Bottom CTA screenshot saved")
        mobile_page.close()

        browser.close()
        print("Done capturing all screenshots.")

if __name__ == '__main__':
    main()

