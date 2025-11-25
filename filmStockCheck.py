import requests
from bs4 import BeautifulSoup
import time
import random

def film_stock_check(sites_config):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    in_stock_count = 0
    out_of_stock_count = 0
    need_fix = 0

    print(f"\n====== 开始检查 (共 {len(sites_config)} 个目标) ======\n")

    for item in sites_config:
        id = item['id']
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
                    if element.name == 'input':
                        raw_text = element.get('value', '')
                    else:
                        # 如果是普通标签 (div, span, button)，文字在标签中间
                        raw_text = element.get_text()

                    text = " ".join(raw_text.split()).lower()

                    print(f"   (调试: 抓取到 '{text}')")
                    bad_words = ["out of stock", "sold out", "backordered", "notify when", "unavailable", "special", "call store", "coming back soon", "eta 4 weeks"]
                    is_out_of_stock = any(w in text for w in bad_words)
                    if not is_out_of_stock:
                        print(f"🟢 [有货] {film_name} @ {site_name}")
                        print(f"      🔗: {url}\n")
                        in_stock_count += 1
                    else:
                        print(f"🔴 [无货] {film_name} @ {site_name}\n")
                        out_of_stock_count += 1
                else:
                    print(f"🟡  [变动] {site_name}: 找不到选择器 '{selector}'。网站可能改版了？\n")
                    print(f"       🔗: {url}\n")
                    need_fix += 1
        except Exception as e:
            print(f"⚠️ [出错] {site_name}: {e}")

    print(f"\n========== 检查完成。{in_stock_count} 个有货，{out_of_stock_count} 个无货，{need_fix} 需要维护 ==========\n")


tracking_list = [
    ########## FUJICHROME Provia 100F ##########
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
        "selector": ".availability-container"
    },
    {
        "id": 3,
        "website_name": "Henry's",
        "film_name": "Provia 100F",
        "url": "https://www.henrys.com/fujichrome-provia-100f-135-36/5637232795.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-container" 
    },
    {
        "id": 4,
        "website_name": "Unique Photo",
        "film_name": "Provia 100F",
        "url": "https://www.uniquephoto.com/product/fujifilmrdpiii13536provia100f14981733",
        "selector": ".chakra-heading"
    },
    {
        "id": 5,
        "website_name": "Tempe camera",
        "film_name": "Provia 100F",
        "url": "https://www.tempecamera.biz/Fujifilm_1759_p/1759.htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 6,
        "website_name": "Retrospekt",
        "film_name": "Provia 100F",
        "url": "https://retrospekt.com/products/fujifilm-provia-100f-35mm-color-reversal-film",
        "selector": ".buy-buttons"
    },
    {
        "id": 7,
        "website_name": "Photo Warehouse",
        "film_name": "Provia 100F",
        "url": "https://www.ultrafineonline.com/fuproprrdp10.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 8,
        "website_name": "B&C Camera",
        "film_name": "Provia 100F",
        "url": "https://store.bandccamera.com/products/fuji-pro-rdpiii-135-36",
        "selector": ".product-form__inventory"
    },
    {
        "id": 9,
        "website_name": "theFINDlab",
        "film_name": "Provia 100F",
        "url": "https://thefindlab.ecwid.com/Fujichrome-Provia-100F-35mm-36-Exposures-p356363044",
        "selector": ".label__text"
    },
    {
        "id": 10,
        "website_name": "Legacy Photo Lab",
        "film_name": "Provia 100F",
        "url": "https://legacy-photolab.com/products/fuji-provia-100f-100-iso-35mm-x-36-exp",
        "selector": ".atc-button--text"
    },
    {
        "id": 11,
        "website_name": "District Camera",
        "film_name": "Provia 100F",
        "url": "https://www.districtcamera.com/products/fujifilm-provia-100-36f-professional-fujichrome-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".product-form__add-button"
    },
    {
        "id": 12,
        "website_name": "Stewarts Photo",
        "film_name": "Provia 100F",
        "url": "https://www.stewartsphoto.com/fujifilm-provia-100-pro-rdpiii-135-36.html",
        "selector": ".out-of-stock"
    },
    {
        "id": 13,
        "website_name": "Film Supply Club",
        "film_name": "Provia 100F",
        "url": "https://filmsupply.club/products/fujfilm-provia-100-35mm-color-positive-film-single-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 14,
        "website_name": "OC Camera",
        "film_name": "Provia 100F",
        "url": "https://www.occamera.com/product-p/16326028(32616).htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 15,
        "website_name": "Nelson",
        "film_name": "Provia 100F",
        "url": "https://nelsonphotoandvideo.com/products/fuji-pro-rdpiii-135-36",
        "selector": ".product-info__add-button"
    },
    {
        "id": 16,
        "website_name": "Austin Camera",
        "film_name": "Provia 100F",
        "url": "https://austincamera.com/products/fujifilm-fujichrome-provia-100f-professiona-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 17,
        "website_name": "Reformed Film Lab",
        "film_name": "Provia 100F",
        "url": "https://reformedfilmlab.com/products/fuji-provia-100f-35mm-36-exposure-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 18,
        "website_name": "Poto Care",
        "film_name": "Provia 100F",
        "url": "https://www.fotocare.com/FUJIFILM_PROVIA_RDP_III_135_36_p/16380.htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 19,
        "website_name": "Ace Photo",
        "film_name": "Provia 100F",
        "url": "https://acephoto.net/do-not-use/fuji-provia-100f-35mm-36-exp/",
        "selector": ".productView-options"
    },
    {
        "id": 20,
        "website_name": "District Camera",
        "film_name": "Provia 100F",
        "url": "https://www.districtcamera.com/products/fujifilm-provia-100-36f-professional-fujichrome-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".product-form__add-button"
    },
    {
        "id": 21,
        "website_name": "Essential Photo Supply",
        "film_name": "Provia 100F",
        "url": "https://essentialphotosupply.com/products/fujifilm-fujichrome-provia-100f-professional-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".AddtoCart"
    },
    {
        "id": 22,
        "website_name": "ArtByPino",
        "film_name": "Provia 100F",
        "url": "https://artbypino.com/products/fujifilm-fujichrome-provia-rdp-iii-100f-color-e6-slide-35mm-36-exp-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 23,
        "website_name": "Hunt's Photo & Video",
        "film_name": "Provia 100F",
        "url": "https://www.huntsphotoandvideo.com/detail_page.cfm?productid=16326028",
        "selector": ".g-color-gray-dark-v2"
    },
    {
        "id": 24,
        "website_name": "Bedford Camera & Video",
        "film_name": "Provia 100F",
        "url": "https://www.bedfords.com/4547410247626",
        "selector": ".g-color-gray-dark-v2"
    },
    {
        "id": 25,
        "website_name": "Hillvale Photo (AU)",
        "film_name": "Provia 100F",
        "url": "https://hillvale.com.au/collections/slide-film/products/fujifilm-provia-100f-35mm",
        "selector": "#AddToCartText"
    },
    {
        "id": 26,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Provia 100F",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-provia-100f-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
        {
        "id": 27,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Provia 100F",
        "url": "https://www.bristolcameras.co.uk/product/fuji-provia-100f-36-exposure-35mm-film/",
        "selector": ".stock"
    },
    {
        "id": 28,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Provia 100F",
        "url": "https://analoguewonderland.co.uk/products/fuji-provia-100f-film-35mm-colour-iso-100",
        "selector": ".product-form__add-button"
    },
    {
        "id": 29,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Provia 100",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-provia-100f-35mm-film-36-exposures-14-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 30,
        "website_name": "Sutck in Film (UK)",
        "film_name": "Provia 100F",
        "url": "https://stuckinfilm.co.uk/products/fujifilm-provia-100f-35mm-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 31,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Provia 100F",
        "url": "https://parallaxphotographic.coop/shop/fuji-provia-100f-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## FUJICHROME Velvia 100 ##########
    {
        "id": 100,
        "website_name": "Henry's",
        "film_name": "Velvia 100",
        "url": "https://www.henrys.com/fujifilmchrome-velvia-100-rvp-35mm-film/5637223937.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-container"
    },
    {
        "id": 101,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 100",
        "url": "https://legacy-photolab.com/products/fuji-fujichrome-velvia-100-iso-35mm-x-36-exp",
        "selector": ".product__badge"
    },
    {
        "id": 102,
        "website_name": "Camera House (AU)",
        "film_name": "Velvia 100",
        "url": "https://www.camerahouse.com.au/fujifilm-fujichrome-velvia-100-35mm-36-exposure-pro-colour-transparency-film-1",
        "selector": ".stock"
    },
    {
        "id": 103,
        "website_name": "Hillvale Photo (AU)",
        "film_name": "Velvia 100",
        "url": "https://hillvale.com.au/collections/slide-film/products/fujifilm-velvia-100-35mm",
        "selector": "#AddToCartText"
    },
    {
        "id": 104,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Velvia 100",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-velvia-100-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
    {
        "id": 105,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Velvia 100",
        "url": "https://www.bristolcameras.co.uk/product/fuji-velvia-100-36-exposure-35mm-film/",
        "selector": ".stock"
    },
    {
        "id": 106,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Velvia 100",
        "url": "https://analoguewonderland.co.uk/products/fuji-velvia-film-35mm-colour-iso-100",
        "selector": ".product-form__add-button"
    },
    {
        "id": 107,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Velvia 100",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-velvia-50-35mm-film-36-exposures-15-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 108,
        "website_name": "Sutck in Film (UK)",
        "film_name": "Velvia 100",
        "url": "https://stuckinfilm.co.uk/products/copy-of-fujifilm-velvia-100-120-film-5-pack",
        "selector": ".product-form__submit"
    },
    {
        "id": 109,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Velvia 100",
        "url": "https://parallaxphotographic.coop/shop/fuji-velvia-100-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## FUJICHROME Velvia 50 ##########
    {
        "id": 200,
        "website_name": "Unique Photo",
        "film_name": "Velvia 50",
        "url": "https://www.uniquephoto.com/product/fujifilmrvp1353650asa15942265",
        "selector": ".chakra-heading"
    },
    {
        "id": 201,
        "website_name": "Retrospekt",
        "film_name": "Velvia 50",
        "url": "https://retrospekt.com/products/fujifilm-velvia-50-35mm-black-and-white-film",
        "selector": ".buy-buttons"
    },
    {
        "id": 202,
        "website_name": "Samy's Camera",
        "film_name": "Velvia 50",
        "url": "https://www.samys.com/p/Film/16329161/Fujifilm-RVP-Fujichrome-Velvia-50-135-36-Professional-Color-Slide-Transparency-Film-ISO-50---Single-Roll/14510.html",
        "selector": ".availability-container"
    },
    {
        "id": 203,
        "website_name": "B&C Camera",
        "film_name": "Velvia 50",
        "url": "https://store.bandccamera.com/products/fujifilm-fujichrome-velvia-rvp-50-color-film-35mm-roll-36-exp",
        "selector": ".product-form__inventory"
    },
    {
        "id": 204,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 50",
        "url": "https://legacy-photolab.com/products/fujichrome-velvia-50-35mm-color-positive-film",
        "selector": ".product__badge"
    },
    {
        "id": 205,
        "website_name": "Film Supply Club",
        "film_name": "Velvia 50",
        "url": "https://filmsupply.club/products/fujfilm-velvia-50-35mm-color-positive-film-single-roll-purchase",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 206,
        "website_name": "OC Camera",
        "film_name": "Velvia 50",
        "url": "https://www.occamera.com/product-p/16329161(122).htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 207,
        "website_name": "Reformed Film Lab",
        "film_name": "Velvia 50",
        "url": "https://reformedfilmlab.com/products/fujifilm-velvia-50-35mm-36-exposure-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 208,
        "website_name": "Coastal Film Lab",
        "film_name": "Velvia 50",
        "url": "https://www.coastalfilmlab.com/products/fujifilm-velvia-50-36exp-35mm-color-positive-film",
        "selector": ".price__badge-sold-out"
    },
    {
        "id": 209,
        "website_name": "Essential Photo Supply",
        "film_name": "Velvia 50",
        "url": "https://essentialphotosupply.com/products/velvia_50_135-36",
        "selector": ".AddtoCart"
    },
    {
        "id": 210,
        "website_name": "Austin Camera",
        "film_name": "Velvia 50",
        "url": "https://austincamera.com/products/fujifilm-fujichrome-velvia-rvp-50-color-slide-film-35mm-roll-film-36-exposures",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 211,
        "website_name": "ArtByPino",
        "film_name": "Velvia 50",
        "url": "https://artbypino.com/products/fujifilm-fujichrome-professional-velvia-50-35mm-color-reversal-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 212,
        "website_name": "Stewarts Photo",
        "film_name": "Velvia 50",
        "url": "https://www.stewartsphoto.com/fujifilm-pro-rvp-50-135-36-velvia.html",
        "selector": ".out-of-stock"
    },
    {
        "id": 213,
        "website_name": "Camera House (AU)",
        "film_name": "Velvia 50",
        "url": "https://www.camerahouse.com.au/fujifilm-fujichrome-velvia-50-135-36",
        "selector": ".stock"
    },
    {
        "id": 214,
        "website_name": "Hillvale Photo (AU)",
        "film_name": "Velvia 50",
        "url": "https://hillvale.com.au/collections/slide-film/products/fujifilm-velvia-50-35mm",
        "selector": "#AddToCartText"
    },
    {
        "id": 215,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Velvia 50",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-velvia-50-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
    {
        "id": 216,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Velvia 50",
        "url": "https://www.bristolcameras.co.uk/product/fuji-velvia-50-36-exposure-35mm-colour-reversal-film/",
        "selector": ".stock"
    },
    {
        "id": 217,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Velvia 50",
        "url": "https://analoguewonderland.co.uk/products/fuji-velvia-film-35mm-colour-iso-50",
        "selector": ".product-form__add-button"
    },
    {
        "id": 218,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Velvia 50",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-velvia-50-35mm-film-36-exposures-14-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 219,
        "website_name": "Sutck in Film (UK)",
        "film_name": "Velvia 50",
        "url": "https://stuckinfilm.co.uk/products/fujifilm-velvia-50-35mm-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 220,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Velvia 50",
        "url": "https://parallaxphotographic.coop/shop/fuji-velvia-50-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## Kodak Professional Ektachrome E100 Color Reversal Film ##########
    {
        "id": 300,
        "website_name": "Dodd Camera",
        "film_name": "Kodak E100",
        "url": "https://doddcamera.com/kodak-professional-ektachrome-e100-color-reversal-film-135-36",
        "selector": ".stock"
    },
    {
        "id": 301,
        "website_name": "Samy's Camera",
        "film_name": "Kodak E100",
        "url": "https://www.samys.com/p/Film/1884576/Ektachrome-E100-Color-Transparency-Film-35mm-Roll-Film,-36-Exposures/205598.html",
        "selector": ".availability-container"
    },
    {
        "id": 302,
        "website_name": "B&H",
        "film_name": "Kodak E100",
        "url": "https://www.bhphotovideo.com/c/product/274846-USA/Kodak_1884576_E100G_135_36_Ektachrome_Professional.html",
        "selector": "[data-selenium='stockStatus']!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    },
    {
        "id": 303,
        "website_name": "Henry's",
        "film_name": "Kodak E100",
        "url": "https://www.henrys.com/kodak-ektachrome-e100g-135-36-100iso/5637232799.p?size=35mm&style=36+Exp",
        "selector": ".ms-buybox__inventory-container"
    },
    ########## Flic Film Chrome 100 Color Reversal Film - Respooled Kodak Ektachrome 100D ##########
    {
        "id": 400,
        "website_name": "Unique Photo",
        "film_name": "Flic Film Chrome 100",
        "url": "https://www.uniquephoto.com/product/flic-film-chrome-100-35mm-36-ex",
        "selector": ".chakra-badge"
    },
    {
        "id": 401,
        "website_name": "B&C Camera",
        "film_name": "Flic Film Chrome 100",
        "url": "https://store.bandccamera.com/products/flic-film-chrome-100-35mm-roll-film-36-exposures",
        "selector": ".product-form__inventory"
    }
]


untracking_list = [
    "https://thephotocenter.com/shop/fujifilm-provia-100f-professional-135-36/5c50798b-9597-4b63-bf21-0dda2bd84a8a",
    "https://www.royalwefilmlab.com/product/-35mm-slide-film-flic-film-chrome-100-35mm-respooled-ektachrome-e100-36exp/71",
    "https://paulsphoto.com/shop/fujifilm-provia-100f-rdp-iii-120/1b90581b-09bd-4bff-a667-2c070d12a3f8"
]


film_stock_check(tracking_list)
