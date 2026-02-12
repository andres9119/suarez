from django import template
from django.conf import settings
import os
from urllib.parse import unquote

register = template.Library()

@register.simple_tag
def webp_url(image_url):
    """
    Returns the URL for the WebP version of an image if it exists on disk.
    Otherwise returns the original URL.
    Usage: {% webp_url object.image.url %}
    """
    if not image_url:
        return ''
    
    # Check if it's already webp
    if image_url.lower().endswith('.webp'):
        return image_url
        
    # Unquote URL to handle special characters like 'ñ' for disk check
    unquoted_url = unquote(image_url)
    
    # Construct the absolute path on disk to check for existence
    if unquoted_url.startswith(settings.MEDIA_URL):
        relative_path = unquoted_url[len(settings.MEDIA_URL):]
        disk_path = os.path.join(settings.MEDIA_ROOT, relative_path)
    elif unquoted_url.startswith(settings.STATIC_URL):
        relative_path = unquoted_url[len(settings.STATIC_URL):]
        disk_path = os.path.join(settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else settings.STATIC_ROOT, relative_path)
    else:
        return image_url

    base_path, ext = os.path.splitext(disk_path)
    webp_disk_path = base_path + ".webp"

    if os.path.exists(webp_disk_path):
        base_url, ext = os.path.splitext(image_url)
        return f"{base_url}.webp"
    
    return image_url

@register.simple_tag
def version_url(image_url, size=None):
    """
    Returns the URL for a specific sized version of an image.
    Usage: {% version_url image_url 800 %}
    """
    if not image_url:
        return ''
    
    # Ensure we use webp variant
    base_url, ext = os.path.splitext(image_url)
    if not base_url.lower().endswith('.webp'):
        webp_variant = f"{base_url}.webp"
    else:
        webp_variant = image_url
        base_url = os.path.splitext(image_url)[0]

    if size:
        return f"{base_url}_{size}.webp"
    return webp_variant

@register.simple_tag
def get_srcset(image_url):
    """
    Generates a srcset string for the provided image URL.
    """
    if not image_url:
        return ''
    
    base_url, _ = os.path.splitext(image_url)
    # Remove .webp if it was already there for the base name
    if base_url.lower().endswith('.webp'):
        base_name = base_url[:-5]
    else:
        base_name = base_url

    return f"{base_name}_400.webp 400w, {base_name}_800.webp 800w, {base_name}_1200.webp 1200w"
