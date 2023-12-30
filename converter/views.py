from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
from django.core.files.base import ContentFile
import io


def jpeg_to_png(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        img = Image.open(image)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        content = ContentFile(buffer.getvalue())
        response = HttpResponse(content, content_type="image/png")
        response["Content-Disposition"] = 'attachment; filename="converted_image.png"'

        return response

        return HttpResponse(content, content_type="image/png")

    return render(request, "converter/jpeg_to_png.html")


def png_to_jpeg(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        img = Image.open(image)

        # Convert RGBA to RGB before saving as JPEG
        if img.mode == "RGBA":
            img = img.convert("RGB")

        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        content = ContentFile(buffer.getvalue())
        return HttpResponse(content, content_type="image/jpeg")

    return render(request, "converter/png_to_jpeg.html")


def main(request):
    return render(request, "main.html")
