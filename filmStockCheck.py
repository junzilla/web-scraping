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
    need_fix_count = 0

    print(f"\n=============== 开始检查 (共 {len(sites_config)} 个目标) ===============\n")

    for item in sites_config:
        id = item['id']
        url = item['url']
        site_name = item['website_name']
        film_name = item['film_name']
        selector = item['selector']

        time.sleep(random.uniform(1, 3))

        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:

                # the most significant part of this html
                soup = BeautifulSoup(response.text, 'html.parser')
                element = soup.select_one(selector)

                if element:
                    if element.name == 'input':
                        raw_text = element.get('value', '')
                    else:
                        # 如果是普通标签 (div, span, button)，文字在标签中间
                        raw_text = element.get_text()
                    
                    text = " ".join(raw_text.split()).lower()

                    # comment out this line for debugging
                    print(f"      {id} {text}")

                    bad_words = ["out of stock", "sold out", "backordered", "notify when", "unavailable", "special order", "call store", "coming back soon", "4 week", "pre-order"]
                    is_out_of_stock = any(w in text for w in bad_words)
                    if not is_out_of_stock:
                        print(f"🟢 [有货] {film_name} @ {site_name}")
                        print(f"      🔗: {url}\n")
                        in_stock_count += 1
                    else:
                        print(f"🔴 [无货] {film_name} @ {site_name}\n")
                        out_of_stock_count += 1
                else:
                    print(f"🟡  [变动] {site_name}: 找不到选择器 '{selector}'")
                    print(f"       🔗: {url}\n")
                    need_fix += 1
        except Exception as e:
            print(f"⚠️  [出错] {site_name}: {e}")
            print(f"       🔗: {url}\n")
    
    success_count = in_stock_count + out_of_stock_count + need_fix_count
    print(f"=================== {success_count}/{len(sites_config)} 检查完成 ====================")
    print(f"========== {in_stock_count} 个有货，{out_of_stock_count} 个无货，{need_fix_count} 个需要维护 ==========\n")


tracking_list = [
    ########## FUJICHROME Provia 100F ##########
    {
        "id": 100,
        "website_name": "Ace Photo",
        "film_name": "Provia 100F",
        "url": "https://acephoto.net/do-not-use/fuji-provia-100f-35mm-36-exp/",
        "selector": ".alertBox--error"
    },
    {
        "id": 101,
        "website_name": "Ace Photo",
        "film_name": "Provia 100F 5 Packs",
        "url": "https://acephoto.net/cameras/fuji-provia100-f-135-36-e-6-slide-film/",
        "selector": ".alertBox--error"
    },
    {
        "id": 102,
        "website_name": "ArtByPino",
        "film_name": "Provia 100F",
        "url": "https://artbypino.com/products/fujifilm-fujichrome-provia-rdp-iii-100f-color-e6-slide-35mm-36-exp-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 103,
        "website_name": "Austin Camera",
        "film_name": "Provia 100F",
        "url": "https://austincamera.com/products/fujifilm-fujichrome-provia-100f-professiona-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 104,
        "website_name": "B&C Camera",
        "film_name": "Provia 100F",
        "url": "https://store.bandccamera.com/products/fuji-pro-rdpiii-135-36",
        "selector": ".product-form__inventory"
    },
    {
        "id": 105,
        "website_name": "Bedford Camera & Video",
        "film_name": "Provia 100F",
        "url": "https://www.bedfords.com/4547410247626",
        "selector": "#form-action-addToCart"
    },
    {
        "id": 106,
        "website_name": "District Camera",
        "film_name": "Provia 100F",
        "url": "https://www.districtcamera.com/products/fujifilm-provia-100-36f-professional-fujichrome-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".product-form__add-button"
    },
    {
        "id": 107,
        "website_name": "Dodd Camera",
        "film_name": "Provia 100F",
        "url": "https://doddcamera.com/fuji-rdp-iii-provia-100f-135-36-single-roll",
        "selector": ".stock"
    },
    {
        "id": 108,
        "website_name": "Essential Photo Supply",
        "film_name": "Provia 100F",
        "url": "https://essentialphotosupply.com/products/fujifilm-fujichrome-provia-100f-professional-rdp-iii-color-transparency-film-35mm-roll-film-36-exposures",
        "selector": ".AddtoCart"
    },
    {
        "id": 109,
        "website_name": "Film Supply Club",
        "film_name": "Provia 100F",
        "url": "https://filmsupply.club/products/fujfilm-provia-100-35mm-color-positive-film-single-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 110,
        "website_name": "Legacy Photo Lab",
        "film_name": "Provia 100F",
        "url": "https://legacy-photolab.com/products/fuji-provia-100f-100-iso-35mm-x-36-exp",
        "selector": ".atc-button--text"
    },
    {
        "id": 111,
        "website_name": "Nelson",
        "film_name": "Provia 100F",
        "url": "https://nelsonphotoandvideo.com/products/fuji-pro-rdpiii-135-36",
        "selector": ".product-info__add-button"
    },
    {
        "id": 112,
        "website_name": "OC Camera",
        "film_name": "Provia 100F",
        "url": "https://www.occamera.com/product-p/16326028(32616).htm",
        "selector": ".StockQuantity_OutOfStock"
    },
    {
        "id": 113,
        "website_name": "Photo Warehouse",
        "film_name": "Provia 100F",
        "url": "https://www.ultrafineonline.com/fuproprrdp10.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 114,
        "website_name": "Poto Care",
        "film_name": "Provia 100F",
        "url": "https://www.fotocare.com/FUJIFILM_PROVIA_RDP_III_135_36_p/16380.htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 115,
        "website_name": "Reformed Film Lab",
        "film_name": "Provia 100F",
        "url": "https://reformedfilmlab.com/products/fuji-provia-100f-35mm-36-exposure-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 116,
        "website_name": "Retrospekt",
        "film_name": "Provia 100F",
        "url": "https://retrospekt.com/products/fujifilm-provia-100f-35mm-color-reversal-film",
        "selector": ".buy-buttons"
    },
    {
        "id": 117,
        "website_name": "Samy's Camera",
        "film_name": "Provia 100F",
        "url": "https://www.samys.com/p/Film/16326028/Fujifilm-Fujichrome-Provia-100F-Professional-RDP-III-Color-Transparency-Film-35mm-Roll-Film,-36-Exposures/207062.html",
        "selector": ".availability-container"
    },
    {
        "id": 118,
        "website_name": "Stewarts Photo",
        "film_name": "Provia 100F",
        "url": "https://www.stewartsphoto.com/fujifilm-provia-100-pro-rdpiii-135-36.html",
        "selector": ".out-of-stock"
    },
    {
        "id": 119,
        "website_name": "Tempe camera",
        "film_name": "Provia 100F",
        "url": "https://www.tempecamera.biz/Fujifilm_1759_p/1759.htm",
        "selector": "div[itemprop='offers']"
    },
    {
        "id": 120,
        "website_name": "theFINDlab",
        "film_name": "Provia 100F",
        "url": "https://thefindlab.ecwid.com/Fujichrome-Provia-100F-35mm-36-Exposures-p356363044",
        "selector": ".label__text"
    },
    {
        "id": 121,
        "website_name": "Unique Photo",
        "film_name": "Provia 100F",
        "url": "https://www.uniquephoto.com/product/fujifilmrdpiii13536provia100f14981733",
        "selector": ".chakra-heading"
    },
    {
        "id": 122,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Provia 100F",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-provia-100f-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
    {
        "id": 123,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Provia 100F",
        "url": "https://www.bristolcameras.co.uk/product/fuji-provia-100f-36-exposure-35mm-film/",
        "selector": ".stock"
    },
    {
        "id": 124,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Provia 100F",
        "url": "https://analoguewonderland.co.uk/products/fuji-provia-100f-film-35mm-colour-iso-100",
        "selector": ".product-form__add-button"
    },
    {
        "id": 125,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Provia 100F",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-provia-100f-35mm-film-36-exposures-14-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 126,
        "website_name": "Stuck in Film (UK)",
        "film_name": "Provia 100F",
        "url": "https://stuckinfilm.co.uk/products/fujifilm-provia-100f-35mm-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 127,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Provia 100F",
        "url": "https://parallaxphotographic.coop/shop/fuji-provia-100f-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## FUJICHROME Velvia 100 ##########
    {
        "id": 200,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 100",
        "url": "https://legacy-photolab.com/products/fuji-fujichrome-velvia-100-iso-35mm-x-36-exp",
        "selector": ".atc-button--text"
    },
    {
        "id": 201,
        "website_name": "Photo Warehouse",
        "film_name": "Velvia 100",
        "url": "https://www.ultrafineonline.com/fuve100rvp35.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 202,
        "website_name": "Camera House (AU)",
        "film_name": "Velvia 100",
        "url": "https://www.camerahouse.com.au/fujifilm-fujichrome-velvia-100-35mm-36-exposure-pro-colour-transparency-film-1",
        "selector": ".stock"
    },
    {
        "id": 203,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Velvia 100",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-velvia-100-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
    {
        "id": 204,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Velvia 100",
        "url": "https://www.bristolcameras.co.uk/product/fuji-velvia-100-36-exposure-35mm-film/",
        "selector": ".stock"
    },
    {
        "id": 205,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Velvia 100",
        "url": "https://analoguewonderland.co.uk/products/fuji-velvia-film-35mm-colour-iso-100",
        "selector": ".product-form__add-button"
    },
    {
        "id": 206,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Velvia 100",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-velvia-50-35mm-film-36-exposures-15-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 207,
        "website_name": "Stuck in Film (UK)",
        "film_name": "Velvia 100",
        "url": "https://stuckinfilm.co.uk/products/copy-of-fujifilm-velvia-100-120-film-5-pack",
        "selector": ".product-form__submit"
    },
    {
        "id": 208,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Velvia 100",
        "url": "https://parallaxphotographic.coop/shop/fuji-velvia-100-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## FUJICHROME Velvia 50 ##########
    {
        "id": 300,
        "website_name": "Ace Photo",
        "film_name": "Velvia 50",
        "url": "https://acephoto.net/cameras/fujichrome-velvia-50-135-36-slide-film/",
        "selector": ".alertBox--error"
    },
    {
        "id": 301,
        "website_name": "ArtByPino",
        "film_name": "Velvia 50",
        "url": "https://artbypino.com/products/fujifilm-fujichrome-professional-velvia-50-35mm-color-reversal-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 302,
        "website_name": "Austin Camera",
        "film_name": "Velvia 50",
        "url": "https://austincamera.com/products/fujifilm-fujichrome-velvia-rvp-50-color-slide-film-35mm-roll-film-36-exposures",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 303,
        "website_name": "B&C Camera",
        "film_name": "Velvia 50",
        "url": "https://store.bandccamera.com/products/fujifilm-fujichrome-velvia-rvp-50-color-film-35mm-roll-36-exp",
        "selector": ".product-form__inventory"
    },
    {
        "id": 304,
        "website_name": "Coastal Film Lab",
        "film_name": "Velvia 50",
        "url": "https://www.coastalfilmlab.com/products/fujifilm-velvia-50-36exp-35mm-color-positive-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 305,
        "website_name": "Essential Photo Supply",
        "film_name": "Velvia 50",
        "url": "https://essentialphotosupply.com/products/velvia_50_135-36",
        "selector": ".AddtoCart"
    },
    {
        "id": 306,
        "website_name": "Film Supply Club",
        "film_name": "Velvia 50",
        "url": "https://filmsupply.club/products/fujfilm-velvia-50-35mm-color-positive-film-single-roll-purchase",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 307,
        "website_name": "Legacy Photo Lab",
        "film_name": "Velvia 50",
        "url": "https://legacy-photolab.com/products/fujichrome-velvia-50-35mm-color-positive-film",
        "selector": ".atc-button--text"
    },
    {
        "id": 308,
        "website_name": "Nelson",
        "film_name": "Velvia 50",
        "url": "https://nelsonphotoandvideo.com/products/fujifilm-fujichrome-velvia-rvp-50-color-film-35mm-roll-36-exp",
        "selector": ".product-info__add-button"
    },
    {
        "id": 309,
        "website_name": "OC Camera",
        "film_name": "Velvia 50",
        "url": "https://www.occamera.com/product-p/16329161(122).htm",
        "selector": ".StockQuantity_OutOfStock"
    },
    {
        "id": 310,
        "website_name": "Photo Warehouse",
        "film_name": "Velvia 50",
        "url": "https://www.ultrafineonline.com/fufuprove50r.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 311,
        "website_name": "Reformed Film Lab",
        "film_name": "Velvia 50",
        "url": "https://reformedfilmlab.com/products/fujifilm-velvia-50-35mm-36-exposure-roll",
        "selector": "[data-add-to-cart-text]"
    },
    {
        "id": 312,
        "website_name": "Retrospekt",
        "film_name": "Velvia 50",
        "url": "https://retrospekt.com/products/fujifilm-velvia-50-35mm-black-and-white-film",
        "selector": ".buy-buttons"
    },
    {
        "id": 313,
        "website_name": "Samy's Camera",
        "film_name": "Velvia 50",
        "url": "https://www.samys.com/p/Film/16329161/Fujifilm-RVP-Fujichrome-Velvia-50-135-36-Professional-Color-Slide-Transparency-Film-ISO-50---Single-Roll/14510.html",
        "selector": ".availability-container"
    },
    {
        "id": 314,
        "website_name": "Stewarts Photo",
        "film_name": "Velvia 50",
        "url": "https://www.stewartsphoto.com/fujifilm-pro-rvp-50-135-36-velvia.html",
        "selector": ".out-of-stock"
    },
    {
        "id": 315,
        "website_name": "Unique Photo",
        "film_name": "Velvia 50",
        "url": "https://www.uniquephoto.com/product/fujifilmrvp1353650asa15942265",
        "selector": ".chakra-heading"
    },
    {
        "id": 316,
        "website_name": "Camera House (AU)",
        "film_name": "Velvia 50",
        "url": "https://www.camerahouse.com.au/fujifilm-fujichrome-velvia-50-135-36",
        "selector": ".stock"
    },
    {
        "id": 317,
        "website_name": "Decisive Moment (AU)",
        "film_name": "Velvia 50",
        "url": "https://www.decisivemoment.com.au/product-page/fujifilm-velvia-50-35mm-film",
        "selector": "[data-hook='BackInStockButton.Root']"
    },
    {
        "id": 318,
        "website_name": "Analogue Wonderland (UK)",
        "film_name": "Velvia 50",
        "url": "https://analoguewonderland.co.uk/products/fuji-velvia-film-35mm-colour-iso-50",
        "selector": ".product-form__add-button"
    },
    {
        "id": 319,
        "website_name": "Bristol Cameras (UK)",
        "film_name": "Velvia 50",
        "url": "https://www.bristolcameras.co.uk/product/fuji-velvia-50-36-exposure-35mm-colour-reversal-film/",
        "selector": ".stock"
    },
    {
        "id": 320,
        "website_name": "The Photographers' Gallery (UK)",
        "film_name": "Velvia 50",
        "url": "https://bookshop.thephotographersgallery.org.uk/products/fujifilm-velvia-50-35mm-film-36-exposures-14-99-incl-vat",
        "selector": ".product-form__submit"
    },
    {
        "id": 321,
        "website_name": "Stuck in Film (UK)",
        "film_name": "Velvia 50",
        "url": "https://stuckinfilm.co.uk/products/fujifilm-velvia-50-35mm-film",
        "selector": ".product-form__submit"
    },
    {
        "id": 322,
        "website_name": "Parallax Photographic Coop (UK)",
        "film_name": "Velvia 50",
        "url": "https://parallaxphotographic.coop/shop/fuji-velvia-50-35mm-film-36-exposures/",
        "selector": ".stock"
    },
    ########## Others  ##########
    {
        "id": 400,
        "website_name": "Photo Warehouse",
        "film_name": "Provia 400 RHP",
        "url": "https://www.ultrafineonline.com/furxppr4035x.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 401,
        "website_name": "Photo Warehouse",
        "film_name": "Velvia 100F RVP",
        "url": "https://www.ultrafineonline.com/furvp13fuve1.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 402,
        "website_name": "Photo Warehouse",
        "film_name": "Velvia 100 RVP",
        "url": "https://www.ultrafineonline.com/fufuprove10r.html",
        "selector": ".add-to-cart h2"
    },
    {
        "id": 403,
        "website_name": "Photo Warehouse",
        "film_name": "Provia 100F 5 Packs",
        "url": "https://www.ultrafineonline.com/fupr10rd35x3.html",
        "selector": ".add-to-cart h2"
    }
]


film_stock_check(tracking_list)
