from django.db import models

# Create your models here.


class Slider(models.Model):
    image = models.ImageField()
    

class Typing_on_slider(models.Model):
    first_typing = models.TextField()
    second_typing = models.TextField()

    def __str__(self):
        return str(self.id) + " " + "Slide"  

class Idare_heyeti(models.Model):
    photo = models.ImageField(upload_to = 'media')
    name = models.TextField()
    vezifesi = models.TextField()



    def __str__(self):
        return self.name +" --- " + self.vezifesi

class Legend_president(models.Model):
    photo = models.ImageField()
    name = models.TextField()

    def __str__(self):
        return self.name

class About_u(models.Model):
    photo = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.text[:100] + " ......"

class Media_links(models.Model):

    facebook = models.TextField()
    instagram = models.TextField()
    email = models.TextField()

class TeamPointTable(models.Model):
    name = models.TextField()
    points = models.IntegerField()
    def __str__(self):
        return self.name + "---" + str(self.points)

class legend_teams(models.Model):
    image = models.ImageField()
    team_name = models.TextField()
    player_names = models.TextField()

    def __str__(self):
        return self.team_name

class Quiz(models.Model):
    question = models.TextField()
    A = models.TextField()
    B = models.TextField()
    C = models.TextField()
    D = models.TextField()

    answer = models.TextField()

    def __str__(self):
        return "Question " + str((self.id)) + "-------" + self.question