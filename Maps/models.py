from django.db import models
import csv



class Tractor(models.Model):
    number = models.CharField(max_length=250)


class Coord(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE)


class Route(models.Model):
    startX = models.FloatField()
    startY = models.FloatField()
    endX = models.FloatField()
    endY = models.FloatField()


class parking(models.Model):
    number = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()


    path = r'C:\Data\Hack\PolyHx\Snowi\Maps\parking.csv'
    file_reader = csv.reader(open(path, 'rt'), delimiter=',')
    for row in file_reader:
        print
        row, ", "

    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = Teacher.objects.get_or_create(
    #             first_name=row[0],
    #             last_name=row[1],
    #             middle_name=row[2],
    #         )

