from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from datetime import datetime

DOCUMENT_TYPE = (
    ('Паспорт', 'Паспорт'),
    ('Аттестат', 'Аттестат'),
    ('СНИЛС', 'СНИЛС'),
    ('Фотография 3x4', 'Фотография 3x4'),
    ('Медицинская справка', 'Медицинская справка'),
    ('Другое', 'Другое')
)

LEVEL_OF_EDUCATION = (
    ('СПО', 'СПО'),
    ('Бакалавриат', 'Бакалавриат'),
    ('Магистратура', 'Магистратура'),
    ('Специалитет', 'Специалитет'),
)

APPLICATION_STATUS = (
    ('Принят', 'Принят'),
    ('Обрабатывается', 'Обрабатывается'),
    ('Отказ', 'Отказ')
)


SPECIALIST_POSITION = (
    ('Глава приема', 'Глава приема'),
    ('Член приемной комиссии', 'Член приемной комиссии')
)


class Educational_Institution(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Образовательное учреждение'
        verbose_name_plural = 'Образовательные учреждения'

    def __str__(self):
        return f'{self.name}  {self.address}'


class User(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name='Отчество',  blank=True, null=True)
    slug = AutoSlugField(populate_from='username', unique=True, verbose_name='URL', )
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес', null=True)
    user_photo = models.ImageField(upload_to='user_photo/%Y/%m/%d/', verbose_name='Аватарка', blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(verbose_name='Год выпуска',
                                                     default=int(datetime.now().strftime("%Y")))
    educational_institution = models.ForeignKey('Educational_Institution', on_delete=models.PROTECT,
                                                verbose_name='Образовательное учреждение', blank=True,  null=True)
    level_of_education = models.CharField(max_length=30, verbose_name='Уровень образования', choices=LEVEL_OF_EDUCATION,default='Бакалавриат')
    use_result = models.PositiveIntegerField(verbose_name='Баллы ЕГЭ', default=0)
    gpa = models.DecimalField(verbose_name='Средний балл', max_digits=3, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.username = self.email
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Document(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='Название')
    document_type = models.CharField(max_length=70, verbose_name='Тип документа', choices=DOCUMENT_TYPE)
    document = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Документ')
    date_add = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.user}-{self.name}'


class Profession(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    period_of_study = models.CharField(max_length=100, verbose_name='Период обучения')
    price = models.PositiveIntegerField(verbose_name='Цена')
    year = models.PositiveIntegerField(verbose_name='Год', default=int(datetime.now().strftime("%Y")))
    study_plan = models.FileField(upload_to='study_plan/%Y/', verbose_name='Учебный план')
    level_of_education = models.CharField(max_length=30, verbose_name='Уровень образования', choices=LEVEL_OF_EDUCATION, default='Бакалавриат')
    slug = AutoSlugField(populate_from='get_url', unique=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return f'{self.name}-{self.year}'

    def get_url(self):
        return f'{self.name}-{self.year}'


class List_Questions(models.Model):
    text = models.TextField(verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Список вопросов'

    def __str__(self):
        return f'{self.text[:30]}...'


class Question(models.Model):
    question = models.ForeignKey('List_Questions', on_delete=models.SET_NULL, verbose_name='Вопрос', null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Вопрос поступающего'
        verbose_name_plural = 'Вопросы поступающих'

    def __str__(self):
        return f'{self.user}-{self.question}'


class Specialist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    position = models.CharField(max_length=100, verbose_name='Должность', choices=SPECIALIST_POSITION)
    text = models.TextField(verbose_name='Речь', blank=True, null=True)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return f'{self.user}'


class Application(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    date_of_appointment = models.DateTimeField(verbose_name='Дата приема', blank=True, null=True)
    profession = models.ForeignKey('Profession', on_delete=models.CASCADE, verbose_name='Специальность')
    specialist = models.ForeignKey('Specialist', on_delete=models.SET_NULL, verbose_name='Специалист', null=True)
    status = models.CharField(max_length=40, verbose_name='Статус', choices=APPLICATION_STATUS, default='Обрабатывается')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.user}  {self.profession}'
