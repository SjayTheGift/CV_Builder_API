from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save

User = get_user_model()


# def create_resume(sender, instance, created, **kwargs):
#     if created:
#        Resume.objects.create(user=instance)

# post_save.connect(create_resume, sender=User)


class Experience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE, related_name='experiences')
    # order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return f"{self.position} - Work Experience"

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


def check_date(sender, instance, *args, **kwargs):
    if instance.start_date > instance.end_date:
        raise ValueError('Start date must be less than end date')

pre_save.connect(check_date, sender=Experience)


class Education(models.Model):
    course = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE, related_name='educations')
    # order = models.IntegerField(blank=False, default=100_000)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - Education"

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Skill(models.Model):
    title = models.CharField(max_length=38)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE, related_name='skills')
    # order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return f"{self.title} - Skill"

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')
    # image = models.ImageField(upload_to='cv_images', null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, verbose_name='Name')
    last_name = models.CharField(max_length=255, blank=True, verbose_name='Surname')
    title = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    career_summary = models.TextField(blank=True, verbose_name='Career Summary')
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    # education = models.ManyToManyField(Education, related_name='educations')
    # experience = models.ManyToManyField(Experience, related_name='experiences')
    # skill = models.ManyToManyField(Skill, related_name='skill')

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


def create_resume(sender, instance, created, **kwargs):
    if created:
       Resume.objects.create(user=instance)

post_save.connect(create_resume, sender=User)