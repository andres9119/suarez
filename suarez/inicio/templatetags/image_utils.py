from django import template
import os

register = template.Library()

@register.simple_tag
def webp_url(image_url):
    """
    Returns the URL for the WebP version of an image if it exists.
    Usage: {% webp_url object.image.url %}
    """
    if not image_url:
        return ''
    
    # Check if it's already webp
    if image_url.lower().endswith('.webp'):
        return image_url
        
    base, ext = os.path.splitext(image_url)
    return f"{base}.webp"
