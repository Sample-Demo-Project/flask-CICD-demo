from flask import Flask, render_template_string
from utils.greeting import Greeting

app = Flask(__name__)

TEMPLATE = """<!doctype html>
<html lang="en">
  <meta charset="utf-8">
  <title>CI/CD Demo</title>
  <body style="font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; padding: 2rem;">
    <h1>{{ message }}</h1>
    <p>Deployed by GitHub Actions → GitHub Pages.</p>
  </body>
</html>"""

@app.route("/")
def index():
    g = Greeting()
    # 你只要改 Greeting.say 的回傳，就會反映到最終頁面
    message = g.say("CI/CD")
    return render_template_string(TEMPLATE, message=message)

if __name__ == "__main__":
    app.run(debug=True)
