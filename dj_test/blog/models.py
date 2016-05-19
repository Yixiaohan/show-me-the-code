from django.db import models
# Create your models here.


class Author(models.Model):
    MALE = 1
    FEMALE = 0
    SEX_CHOICE = ((MALE, u'male'), (FEMALE, u'female'))

    author = models.CharField('author name', null=False, max_length=30, blank=False, unique=True,)
    sex = models.IntegerField('sex', choices=SEX_CHOICE, help_text="sex")
    age = models.IntegerField('age', null=True, default=0, help_text="age")
    status = models.BooleanField('status', default=True, help_text='user status')

    def __unicode__(self):
        return self.author

    # class Meta:
    #     abstract = True

    def user_data(self):
        return {
            'user_name': self.user_name,
            'sex': self.sex,
            'age': self.age,
        }


class Article(models.Model):
    title = models.CharField('title', null=False, blank=False, max_length=50, help_text='article title')
    # author = models.ForeignKey(Author, default=1)
    # author = models.CharField(max_length=255, null=True)
    content = models.TextField('content', null=False, blank=False, help_text='content')
    create_at = models.DateTimeField('create time', auto_now_add=True, null=False)
    update_at = models.DateTimeField('update time', auto_now=True)
    tags = models.CharField('tags', null=True, max_length=30, help_text='tags')

    def __unicode__(self):
        return self.title

    def data(self):
        return {
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'tags': self.tags,
        }