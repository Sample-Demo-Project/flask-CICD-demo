import os
from app import app

def build():
    with app.test_client() as c:
        resp = c.get("/")
        html = resp.data.decode("utf-8")

    os.makedirs("docs", exist_ok=True)
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    # SPA/深連結回退（安全可選）
    with open("docs/404.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    build()