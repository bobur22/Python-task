from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, help_text=_("Title of the category."))
    description = models.TextField(null=True, blank=True, help_text=_("Description of the category."))
    category_id = models.ManyToManyField('self', related_name='category_id', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Shop(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, help_text=_("Title of the shop."))
    description = models.TextField(null=True, blank=True, help_text=_("Description of the shop."))
    image_url = models.ImageField(upload_to="shop/", null=True, blank=True, help_text=_("Image of the shop."))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def img_preview(self):
        print(mark_safe(f'<img src = "{self.image_url.url}" width = "300"/>'), "salom")
        return mark_safe(f'<img src = "{self.image_url.url}" width = "300"/>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

class Images(models.Model):
    image = models.ImageField(upload_to="products/", null=True, blank=True, help_text=_("Image of the product."),
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

class Product(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, help_text=_("Title of the product."))
    description = models.TextField(null=True, blank=True, help_text=_("Description of the product."))
    amount = models.PositiveIntegerField(null=True, blank=True, help_text=_("The amount of the product."))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text=_("The price of the product."))
    image = models.ManyToManyField(Images, related_name='product_image')
    active = models.BooleanField(default=True, help_text=_("Activate the product."))

    category_id = models.ManyToManyField(Category, related_name="products")
    shop_id = models.ForeignKey(Shop, related_name="shop", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.first().image.url}" width = "300"/>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
