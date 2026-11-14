import os
from playwright.sync_api import sync_playwright

def main():
    os.makedirs('screenshots/audit', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # === DESKTOP 1440px ===
        page = browser.new_page(viewport={'width': 1440, 'height': 900})
        try:
            page.goto('http://127.0.0.1:8000', wait_until='networkidle', timeout=15000)
        except Exception:
            page.goto('http://127.0.0.1:8000', wait_until='domcontentloaded')
        page.wait_for_timeout(2500)

        # Full page
        page.screenshot(path='screenshots/audit/desktop_full.png', full_page=True)
        print("Desktop full saved")

        # Section-by-section: scroll and capture each
        sections = {
            'hero': 'header',
            'stats_bento': '#tentang',
            'donation_schemes': '#donasi',
            'activities': '#kegiatan',
            'testimonials': '#testimoni',
            'faq': '#faq',
        }
        for name, selector in sections.items():
            try:
                el = page.locator(selector).first
                if el.count() > 0:
                    el.scroll_into_view_if_needed()
                    page.wait_for_timeout(400)
                    el.screenshot(path=f'screenshots/audit/desktop_{name}.png')
                    print(f"Desktop {name} saved")
            except Exception as e:
                print(f"Desktop {name} failed: {e}")

        # Bottom CTA
        try:
            cta = page.locator('section.bg-\\[\\#FFFF55\\]').first
            if cta.count() > 0:
                cta.scroll_into_view_if_needed()
                page.wait_for_timeout(400)
                cta.screenshot(path='screenshots/audit/desktop_bottom_cta.png')
                print("Desktop bottom_cta saved")
        except Exception as e:
            print(f"Desktop bottom_cta failed: {e}")

        page.close()

        # === MOBILE 375px ===
        mobile = browser.new_page(viewport={'width': 375, 'height': 812})
        try:
            mobile.goto('http://127.0.0.1:8000', wait_until='networkidle', timeout=15000)
        except Exception:
            mobile.goto('http://127.0.0.1:8000', wait_until='domcontentloaded')
        mobile.wait_for_timeout(2500)

        mobile.screenshot(path='screenshots/audit/mobile_full.png', full_page=True)
        print("Mobile full saved")

        for name, selector in sections.items():
            try:
                el = mobile.locator(selector).first
                if el.count() > 0:
                    el.scroll_into_view_if_needed()
                    mobile.wait_for_timeout(400)
                    el.screenshot(path=f'screenshots/audit/mobile_{name}.png')
                    print(f"Mobile {name} saved")
            except Exception as e:
                print(f"Mobile {name} failed: {e}")

        try:
            cta = mobile.locator('section.bg-\\[\\#FFFF55\\]').first
            if cta.count() > 0:
                cta.scroll_into_view_if_needed()
                mobile.wait_for_timeout(400)
                cta.screenshot(path='screenshots/audit/mobile_bottom_cta.png')
                print("Mobile bottom_cta saved")
        except Exception as e:
            print(f"Mobile bottom_cta failed: {e}")

        mobile.close()
        browser.close()
        print("All audit screenshots done.")

if __name__ == '__main__':
    main()

