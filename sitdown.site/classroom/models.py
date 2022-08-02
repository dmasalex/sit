from django.db import models
from django.shortcuts import reverse
from pytils import translit



def slugify(s, date_of_birth):
    new_slug = translit.slugify(s)
    return new_slug + "-" + date_of_birth


class Classroom(models.Model):
    """Номер класса"""

    name = models.CharField('Класс', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    comment = models.TextField('Заметка', blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Classroom, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('classroom_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['name']


class Gender(models.Model):
    """Пол"""

    name = models.CharField('Пол', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('gender', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'
        ordering = ['name']


class Requirement(models.Model):
    """Ограничения"""

    name = models.CharField('Ограничение', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    comment = models.TextField('Заметка', blank=True)

    def get_absolute_url(self):
        return reverse('requirement_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Requirement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ограничение'
        verbose_name_plural = 'Ограничения'
        ordering = ['name']


class Schoolboy(models.Model):
    """Ученик"""

    name = models.CharField('Фамилия Имя', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    phone = models.CharField('Номер телефона', blank=True, max_length=11)
    date_of_birth = models.DateField('Дата рождения')
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/')
    comment = models.TextField('Заметка', blank=True)
    classroom = models.ForeignKey(Classroom, related_name='schoolboy', on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, related_name='schoolboy', on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, related_name='schoolboy', on_delete=models.CASCADE)
    energy = models.BooleanField('Активный', default=False)
    height = models.CharField('Рост, см.', max_length=3, blank=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_update = models.DateTimeField('Дата редактирования', auto_now=True)

    def get_absolute_url(self):
        return reverse('schoolboy_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('schoolboy_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('schoolboy_delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, str(self.date_of_birth))
        super(Schoolboy, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['name']


class Location(models.Model):
    """Рассадка школьников"""

    position = models.CharField('Рассадка', max_length=255)
    save_bd = models.BooleanField('Сохранение в БД', default=False)
    classroom = models.ForeignKey(Classroom, related_name='location', on_delete=models.CASCADE)
    create_data = models.DateTimeField('Дата начала рассадки', auto_now_add=True)
    end_data = models.DateField('Дата окончания рассадки', blank=True, null=True)

    def __str__(self):
        return f'{self.classroom}'

    class Meta:
        verbose_name = 'Рассадка'
        verbose_name_plural = 'Рассадки'
        ordering = ['position']


class Teacher(models.Model):
    """Учитель"""
    name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255, default="Классный руководитель")
    slug = models.SlugField(max_length=255, unique=True)
    classroom = models.ForeignKey(Classroom, related_name='teacher', on_delete=models.CASCADE)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/')
    comment = models.TextField('Заметка', blank=True)

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['name']
