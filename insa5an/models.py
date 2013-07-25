from django.db import models


# Create your models here.
class Etudiant(models.Model):

    def upload(self, input_filename, output_filename):
        ext = filename.split('.')[-1]
        return 'photos/'+self.email.split('@')[0]+'/'+output_filename+'.'+ext

    def upload_portrait(self, filename):
        return upload(filename, 'portrait')

    def upload_group1(self, filename):
        return upload(filename, 'group1')

    def upload_group2(self, filename):
        return upload(filename, 'group2')

    def upload_group3(self, filename):
        return upload(filename, 'group3')

    DEPARTEMENT_CHOICES = (
        ('INFO', 'INFO'),
        ('SRC', 'SRC'),
        ('EII', 'EII'),
        ('GMA', 'GMA'),
        ('GCU', 'GCU'),
        ('SGM', 'SGM'),
    )

    email = models.EmailField(unique=True)
    departement = models.CharField(blank=True, max_length=4, choices=DEPARTEMENT_CHOICES)
    annee_etranger = models.IntegerField(blank=True, null=True)
    associatif = models.TextField(blank=True, max_length=300)
    commentaire = models.TextField(blank=True, max_length=300)
    portrait = models.ImageField(blank=True, null=True, upload_to=upload_portrait, max_length=350)
    photo_group1 = models.ImageField(blank=True, null=True, upload_to=upload_group1, max_length=350)
    photo_group2 = models.ImageField(blank=True, null=True, upload_to=upload_group2, max_length=350)
    photo_group3 = models.ImageField(blank=True, null=True, upload_to=upload_group3, max_length=350)
    has_info = models.BooleanField(default=False)
    has_portrait = models.BooleanField(default=False)
    nb_photo_group = models.IntegerField(default=0)
    is_valid = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.email,)
