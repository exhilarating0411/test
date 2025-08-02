from http.server import BaseHTTPRequestHandler
from PIL import Image, ImageDraw
import io

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 生成图片
        img = Image.new('RGB', (200, 100), color = 'red')
        d = ImageDraw.Draw(img)
        d.text((10,10), "Hello from Python!", fill=(255,255,0))

        # 2. 将图片保存到内存中
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_bytes = buffer.getvalue()

        # 3. 发送HTTP响应
        self.send_response(200)
        self.send_header('Content-type', 'image/png') # 告诉浏览器这是一个PNG图片
        self.end_headers()
        self.wfile.write(img_bytes)
        return