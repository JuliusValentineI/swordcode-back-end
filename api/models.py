from django.db import models

def get_post_type():
    return {
        "javascript": "Javascript Vanila", 
        "typescript": "Typescript Vanila",
        "python": "Python Vanila",
        "next_js": "Next Js",
        "react": "React",
        "react_movile": "React Mobile",
        "django": "Django",
        "flask": "Flask",
        "ninja": "Ninja",
        None: None,
        "test": "Pruebas de testeo"
    }


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default="")
    post_type = models.CharField(max_length=50, choices=get_post_type(), default=None)
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class File(models.Model):
    filename = models.CharField(max_length=255)
    filetype = models.CharField(max_length=255, default='text/markdown')
    content = models.TextField()
    
    upload_to = 'api/files'

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='files',
        default=""
    )    
    
