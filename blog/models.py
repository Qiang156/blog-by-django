from django.db import models
from django.db.models.base import Model

STATUS_CHOICE = (
    (0, 'draft'),
    (1, 'published'),
    (2, 'deleted'),
)

GENDER_CHOICE = (
    (0, 'None'),
    (1, 'Male'),
    (2, 'Female'),
)


# ----------------------------------------------------
class User(models.Model):
    """
    User
    """
    name = models.CharField(verbose_name="User Name",
                            unique=True,
                            max_length=30,
                            null=False,
                            blank=False)

    password = models.CharField(verbose_name='Password',
                                max_length=32,
                                null=False,
                                blank=False)

    real_name = models.CharField(verbose_name="Real Name",
                                 unique=True,
                                 max_length=30,
                                 null=False,
                                 blank=False)

    gender = models.SmallIntegerField(verbose_name="Gender",
                                      choices=GENDER_CHOICE)

    email = models.EmailField(verbose_name="Email",
                              unique=True,
                              max_length=100,
                              null=False,
                              blank=False)

    def __str__(self) -> str:
        return self.name

    def getGender(self):
        return GENDER_CHOICE[self.gender][1]

    class Meta:
        db_table = "blog_users"


# ----------------------------------------------------
class Category(models.Model):
    """
    Cateogry for Post
    """
    name = models.CharField(verbose_name="Name",
                            unique=True,
                            max_length=50,
                            blank=False,
                            null=False)
    sort = models.IntegerField(verbose_name="sort", default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "blog_categories"


# ----------------------------------------------------
class Post(models.Model):
    """
    POST
    """
    title = models.CharField(verbose_name="Title",
                             max_length=100,
                             blank=False,
                             null=False)

    body = models.TextField(verbose_name="Content")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.SmallIntegerField(verbose_name="Status",
                                      choices=STATUS_CHOICE)

    created_at = models.DateTimeField(verbose_name="Created Time",
                                      auto_now_add=True,
                                      editable=False)
                                      
    updated_at = models.DateTimeField(verbose_name="Updated Time",
                                      auto_now=True,
                                      editable=False)

    def __str__(self) -> str:
        return self.title

    def getStatus(self):
        return STATUS_CHOICE[self.status][1]

    class Meta:
        db_table = "blog_posts"
