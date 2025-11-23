import requests

def get_live_json(uid):
    url = f'https://live.douyin.com/webcast/room/web/enter/?aid=6383&web_rid={uid}'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Referer": f"https://live.douyin.com/{uid}",
        "Origin": "https://live.douyin.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive"
    }

    # 使用 Session 保持会话，处理 cookies 和重定向
    session = requests.Session()
    try:
        resp = session.get(url, headers=headers, allow_redirects=True, timeout=10)
        print("📄 Content-Type:", resp.headers.get("Content-Type"))
        print("🔗 最终 URL:", resp.url)
        print("🔍 内容预览:\n", resp.text[:500])

        # 强制判断是否是 JSON
        if 'application/json' in resp.headers.get("Content-Type", ""):
            data = resp.json()
            print("✅ 成功获取 JSON：")
            print(data)
        else:
            print("⚠️ 响应不是 JSON 格式，可能被重定向或拦截")

    except Exception as e:
        print("❌ 请求或解析失败:", e)

# 示例调用
get_live_json(675748629342)
