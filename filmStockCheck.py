import requests
from bs4 import BeautifulSoup
import time
import random

def film_stock_check(sites_config):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"\n====== 开始检查 (共 {len(sites_config)} 个目标) ======\n")

    for item in sites_config:
        url = item['url']
        site_name = item['website_name']
        film_name = item['film_name']
        # make sure selector is in item in tracking list, otherwise, crash down. Or use item.get('selector')
        selector = item['selector']

        time.sleep(random.uniform(1, 3))

        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # the most significant part of this html
                element = soup.select_one(selector)
                if element:
                    text = element.get_text().strip().lower()
                    #print(f"   (调试: 抓取到的文字是 '{text}')")
                    bad_words = ["out of stock", "sold out", "backordered", "notify when", "unavailable", "special", "in store"]
                    is_out_of_stock = any(w in text for w in bad_words)
                    if not is_out_of_stock:
                        print(f"✅ [有货] {film_name} @ {site_name}")
                        print(f"      🔗: {url}\n")
                    else:
                        print(f"❌ [无货] {film_name} @ {site_name}\n")
                else:
                    print(f"⚠️  [结构变动] {site_name}: 找不到选择器 '{selector}'。网站可能改版了？\n")
        except Exception as e:
            print(f"⚠️ [出错] {site_name}: {e}")
    print("\n========== 检查完成 ==========\n")


tracking_list = [
    ########## Provia 100F ##########
    {
        "id": 1,
        "website_name": "Dodd Camera",
        "film_name": "Provia 100F",
        "url": "https://doddcamera.com/fuji-rdp-iii-provia-100f-135-36-single-roll",
        "selector": ".stock"
    },
    {
        "id": 2,
        "website_name": "Samy's Camera",
        "film_name": "Provia 100F",
        "url": "https://www.samys.com/p/Film/16326028/Fujifilm-Fujichrome-Provia-100F-Professional-RDP-III-Color-Transparency-Film-35mm-Roll-Film,-36-Exposures/207062.html",
        "selector": ".availability-value"
    },
    {
        "id": 3,
        "website_name": "B&H",
        "film_name": "Provia 100F",
        "url": "https://www.bhphotovideo.com/c/product/181489-USA/Fujifilm_14883175_RDP_III_135_36_Fujichrome_Provia.html",
        "selector": "[data-selenium='stockStatus']"
    },
    {
        "id": 4,
        "website_name": "Henry's",
        "film_name": "Provia 100F",
        "url": "https://www.henrys.com/fujichrome-provia-100f-135-36/5637232795.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-label" 
    },
    {
        "id": 5,
        "website_name": "Unique Photo",
        "film_name": "Provia 100F",
        "url": "https://www.uniquephoto.com/product/fujifilmrdpiii13536provia100f14981733",
        "selector": ".chakra-badge"
    },
    {
        "id": 6,
        "website_name": "Freestyle",
        "film_name": "Provia 100F",
        "url": "https://www.freestylephoto.com/16326028",
        "selector": "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    },
    {
        "id": 7,
        "website_name": "Tempe camera",
        "film_name": "Provia 100F",
        "url": "https://www.tempecamera.biz/Fujifilm_1759_p/1759.htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 8,
        "website_name": "Retrospekt",
        "film_name": "Provia 100F",
        "url": "https://retrospekt.com/products/fujifilm-provia-100f-35mm-color-reversal-film",
        "selector": ".buy-buttons button"
    },
    {
        "id": 9,
        "website_name": "Photo Warehouse",
        "film_name": "Provia 100F",
        "url": "https://www.ultrafineonline.com/fuproprrdp10.html",
        "selector": ".add-to-cart"
    },
    {
        "id": 10,
        "website_name": "The Photo Center",
        "film_name": "Provia 100F",
        "url": "https://thephotocenter.com/shop/fujifilm-provia-100f-professional-135-36/5c50798b-9597-4b63-bf21-0dda2bd84a8a",
        "selector": ".d-product-price-in-store-text"
    },
    {
        "id": 11,
        "website_name": "B&C Camera",
        "film_name": "Provia 100F",
        "url": "https://store.bandccamera.com/products/fuji-pro-rdpiii-135-36",
        "selector": ".product-form__inventory"
    },
    {
        "id": 12,
        "website_name": "theFINDlab",
        "film_name": "Provia 100F",
        "url": "https://thefindlab.ecwid.com/Fujichrome-Provia-100F-35mm-36-Exposures-p356363044",
        "selector": ".label__text"
    },
    {
        "id": 13,
        "website_name": "Legacy Photo Lab",
        "film_name": "Provia 100F",
        "url": "https://legacy-photolab.com/products/fuji-provia-100f-100-iso-35mm-x-36-exp",
        "selector": ".product__badge"
    },
    {
        "id": 14,
        "website_name": "District Camera",
        "film_name": "Provia 100F",
        "url": "https://www.districtcamera.com/products/fujifilm-provia-100-36f-professional-fujichrome-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".product-form__add-button"
    },
    {
        "id": 15,
        "website_name": "Stewarts Photo",
        "film_name": "Provia 100F",
        "url": "https://www.stewartsphoto.com/fujifilm-provia-100-pro-rdpiii-135-36.html",
        "selector": ".out-of-stock"
    },
    ########## Velvia 100 ##########
    {
        "id": 40,
        "website_name": "Henry's",
        "film_name": "Velvia 100",
        "url": "https://www.henrys.com/fujifilmchrome-velvia-100-rvp-35mm-film/5637223937.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-label"
    },
    {
        "id": 41,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 100",
        "url": "https://legacy-photolab.com/products/fuji-fujichrome-velvia-100-iso-35mm-x-36-exp",
        "selector": ".product__badge"
    },
    ########## Velvia 50 ##########
    {
        "id": 80,
        "website_name": "Unique Photo",
        "film_name": "Velvia 50",
        "url": "https://www.uniquephoto.com/product/fujifilmrvp1353650asa15942265",
        "selector": ".chakra-badge"
    },
    {
        "id": 81,
        "website_name": "Retrospekt",
        "film_name": "Velvia 50",
        "url": "https://retrospekt.com/products/fujifilm-velvia-50-35mm-black-and-white-film",
        "selector": ".buy-buttons button"
    },
    {
        "id": 82,
        "website_name": "Samy's Camera",
        "film_name": "Velvia 50",
        "url": "https://www.samys.com/p/Film/16329161/Fujifilm-RVP-Fujichrome-Velvia-50-135-36-Professional-Color-Slide-Transparency-Film-ISO-50---Single-Roll/14510.html",
        "selector": ".availability-value"
    },
    {
        "id": 83,
        "website_name": "B&C Camera",
        "film_name": "Velvia 50",
        "url": "https://store.bandccamera.com/products/fujifilm-fujichrome-velvia-rvp-50-color-film-35mm-roll-36-exp",
        "selector": ".product-form__inventory"
    },
    {
        "id": 84,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 50",
        "url": "https://legacy-photolab.com/products/fujichrome-velvia-50-35mm-color-positive-film",
        "selector": ".product__badge"
    },
    ########## KODAK E100 ##########
    {
        "id": 100,
        "website_name": "Dodd Camera",
        "film_name": "KODAK E100",
        "url": "https://doddcamera.com/kodak-professional-ektachrome-e100-color-reversal-film-135-36",
        "selector": ".stock"
    },
    {
        "id": 101,
        "website_name": "Samy's Camera",
        "film_name": "KODAK E100",
        "url": "https://www.samys.com/p/Film/1884576/Ektachrome-E100-Color-Transparency-Film-35mm-Roll-Film,-36-Exposures/205598.html",
        "selector": ".availability-value"
    },
    {
        "id": 102,
        "website_name": "B&H",
        "film_name": "KODAK E100",
        "url": "https://www.bhphotovideo.com/c/product/274846-USA/Kodak_1884576_E100G_135_36_Ektachrome_Professional.html",
        "selector": "[data-selenium='stockStatus']!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    },
    {
        "id": 103,
        "website_name": "Henry's",
        "film_name": "KODAK E100",
        "url": "https://www.henrys.com/kodak-ektachrome-e100g-135-36-100iso/5637232799.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-label"
    },
    ########## FLIC FILM Chrome 100 ##########
    {
        "id": 105,
        "website_name": "Unique Photo",
        "film_name": "Flic Film Chrome 100",
        "url": "https://www.uniquephoto.com/product/flic-film-chrome-100-35mm-36-ex",
        "selector": ".chakra-badge"
    },
        {
        "id": 106,
        "website_name": "B&C Camera",
        "film_name": "Flic Film Chrome 100",
        "url": "https://store.bandccamera.com/products/flic-film-chrome-100-35mm-roll-film-36-exposures",
        "selector": ".product-form__inventory"
    }
]


velvia50_urls = [
    "https://www.freestylephoto.com/02303205",
]


film_stock_check(tracking_list)
