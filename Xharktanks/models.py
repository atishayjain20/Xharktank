from django.db import models

# Create your models here.

# Investors will make an counter offer to the pitch by providing these inputs
# Unique Id of the Pitch made by the entrepreneur
# Name of the investor making a counter offer
# Amount ready to invest in the idea
# Ask Percentage of Equity for a company

class Investors(models.Model):
    id=models.AutoField(primary_key=True)
    investor=models.CharField(max_length=20)
    amount=models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    equity=models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    comment=models.TextField()


    def __str__(self):
        return str(self.id)

# Entrepreneurs will post Pitch by providing these inputs
# Name of the entrepreneur posting the pitch
# Title of the pitch
# Business Idea for the Product they wish to develop
# Ask Expected Amount for investment
# Percentage of Equity to be diluted

class Entre(models.Model):
    id=models.AutoField(primary_key=True)
    offers=models.ManyToManyField(Investors,blank=True)
    entrepreneur=models.CharField(max_length=20)
    pitchTitle=models.TextField()
    pitchIdea=models.TextField()
    askAmount=models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    equity=models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    class Meta:
        ordering=['-id']
    def __str__(self):
        return str(self.id)




    # timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    # entrid=models.IntegerField(default=NULL)