import uuid
from django.utils.text import slugify

def generate_unique_slug(instance, field_name, base_slug=None):
    if not base_slug:
        base_slug = slugify(getattr(instance, field_name)) or "item"
    base_slug = base_slug[:45]
    unique_slug = base_slug

    ModelClass = instance.__class__
    while ModelClass.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{uuid.uuid4().hex[:4]}"

    return unique_slug
