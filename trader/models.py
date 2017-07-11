from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Team(models.Model):
    def __str__(self):
        return self.abbv

    location = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    abbv = models.CharField(max_length=3)
    logo = models.ImageField(upload_to="logos/%Y/")
    conference = models.CharField(max_length=4,choices=(('East','East'),('West','West')))

@python_2_unicode_compatible
class Player(models.Model):
    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()

    POSITION_CHOICE = (
        ('C', 'C'),
        ('PF', 'PF'),
        ('SF', 'SF'),
        ('SG', 'SG'),
        ('PG', 'PG'),
    )
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICE,
    )

    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    wingspan = models.PositiveSmallIntegerField()
    handwidth = models.PositiveSmallIntegerField()

class Contract(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
    )
    
    effective_date = models.DateField()
    contract_year = models.PositiveSmallIntegerField()
    base_compensation = models.PositiveIntegerField()
    guarantee_percentage = models.PositiveSmallIntegerField()

    OPTION_CHOICE = (
        ('N', '-'),
        ('T', 'Team'),
        ('P', 'Player'),
    )
    option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICE,
    )

    CONTRACT_TYPE_CHOICE = (
        ('RS', 'Rookie Scale'),
        ('RSE','Rookie Scale Extension'),
        ('VET','Veteran'),
        ('VE', 'Veteran Extension'),
    )
    contract_type = models.CharField(
        max_length=3,
        choices=CONTRACT_TYPE_CHOICE,
    )

class ContractHistory(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    effective_date = models.DateField()
