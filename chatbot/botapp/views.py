
import hashlib

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import ImageRecord


def chatbot_page(request):
    return render(request, "chatbot.html")


@csrf_exempt  # Local demo only
@require_POST
def search_images(request):
    uploaded_image = request.FILES.get("image")

    if not uploaded_image:
        return JsonResponse(
            {"error": "Please upload an image."},
            status=400,
        )

    # Calculate the uploaded file's hash.
    uploaded_hash = hashlib.sha256(uploaded_image.read()).hexdigest()

    matching_images = []

    # Compare it with every image stored in the database.
    for item in ImageRecord.objects.all():
        try:
            item.image.open("rb")
            stored_hash = hashlib.sha256(item.image.read()).hexdigest()
            item.image.close()

            if uploaded_hash == stored_hash:
                matching_images.append({
                    "title": item.title,
                    "category": item.category,
                    "image_url": request.build_absolute_uri(
                        item.image.url
                    ),
                })
        except (OSError, ValueError):
            continue

    return JsonResponse({
        "images": matching_images,
        "message": (
            "Exact image match found."
            if matching_images
            else "No exact image match found in the database."
        ),
    })
