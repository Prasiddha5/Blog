from django.db import models
class Blog(models.Model):

    CATEGORY_CHOICES = [
        ("technology", "Technology"),
        ("health", "Health"),
        ("finance", "Finance"),
        ("sports", "Sports"),
        ("education", "Education"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="technology"
    )

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when updated

    def __str__(self):
        return self.title