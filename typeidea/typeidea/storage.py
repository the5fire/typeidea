# coding:utf-8
from __future__ import unicode_literals

from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont


class MyStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        # 处理逻辑
        if 'image' in content.content_type:
            # 加水印
            image = self.watermark_with_text(content, 'the5fire.com', 'red')
            content = self.convert_image_to_file(image, name)

        return super(MyStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format='PNG')
        buffer = temp.getbuffer()
        return InMemoryUploadedFile(temp, None, name, 'image/png', buffer.nbytes, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily="/Users/the5fire/Downloads/font1060/font1060/Sofia-Regular.otf"):
        image = Image.open(file_obj).convert('RGBA')
        imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(imageWatermark)
        width, height = image.size
        margin = 10
        font = ImageFont.truetype(fontfamily, int(height / 20))
        textWidth, textHeight = draw.textsize(text, font)
        x = (width - textWidth - margin) / 2
        y = height - textHeight - margin

        draw.text((x, y), text, color, font)

        return Image.alpha_composite(image, imageWatermark)
