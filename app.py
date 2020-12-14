from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://opgg-com-image.akamaized.net/attach/images/20200325054401.1038024.gif",
        "https://img2.quasarzone.co.kr/web/editor/1912/1912obj___873000268.gif",
        "http://4.bp.blogspot.com/-GuzHHRgw6wg/UgvrdcfsfEI/AAAAAAAAACw/YBbtXcZe4c8/s320/cat+banging.gif",
	"http://kids.dongascience.com/upload/posting/2020/08/75ccac6cabeba28942e9b7eeef67106c.gif",
	"http://kids.dongascience.com/upload/posting/2020/08/20a96892c54e5d7f956a50a78d3e634d.gif",
	"http://kids.dongascience.com/upload/posting/2020/08/26c9ff6cee4f797bc170271df98c9810.gif",
	"http://kids.dongascience.com/upload/posting/2020/08/e19e355fb16792d329bb8ab7b9f33723.gif",
	"https://upload2.inven.co.kr/upload/2018/05/26/bbs/i14701944056.gif",
	"https://upload2.inven.co.kr/upload/2018/05/26/bbs/i14771846318.gif"
        ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
