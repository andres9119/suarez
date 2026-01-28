import re
from django import template

register = template.Library()

@register.filter(name='youtube_embed')
def youtube_embed(url):
    """
    Converts any YouTube URL to a high-compatibility embed URL.
    - Handles watch?v=, youtu.be/, shorts/, live/
    - Cleans up extra parameters
    - Returns standard youtube.com/embed/ for maximum browser support
    """
    if not url:
        return ""
    
    # Extract ID
    video_id = None
    
    # Pattern 1: youtu.be/ID
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0].split("&")[0]
    
    # Pattern 2: watch?v=ID
    elif "v=" in url:
        # Get the 'v' parameter specifically
        parts = url.split("?")
        if len(parts) > 1:
            params = parts[1].split("&")
            for p in params:
                if p.startswith("v="):
                    video_id = p.split("=")[1]
                    break
        # Fallback split if complex
        if not video_id:
            video_id = url.split("v=")[1].split("&")[0]
        
    # Pattern 3: shorts/, live/, embed/, v/
    else:
        for tag in ["/shorts/", "/live/", "/embed/", "/v/"]:
            if tag in url:
                video_id = url.split(tag)[1].split("?")[0].split("&")[0]
                break

    if video_id:
        # Standardize ID (YouTube IDs are 11 chars)
        video_id = video_id.strip()[:11]
        # Using the standard domain as some browsers are stricter with nocookie origins
        return f"https://www.youtube.com/embed/{video_id}?autoplay=0&rel=0&showinfo=0&modestbranding=1"
    
    return url
