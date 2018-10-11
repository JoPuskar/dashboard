import sys
import argparse
import datetime

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

import pandas as pd

from visualizations.models import District, STFCLocations


class Command(BaseCommand):
    help = 'load stfc data from stfc csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)   

        df = pd.read_csv(sys.argv[3]).fillna(value=0)
        total = df['STFC Name'].count()
        for row in range(0, total):

            pnt = Point(df['Latitude'][row], df['Longitude'][row])
            stfc, created = STFCLocations.objects.get_or_create(
                    district_name=df['District'][row],
                    name=df['STFC Name'][row],
                    type=df['Type'][row],
                    address=df['Address'][row],
                    contact_number=df['Contact Number'][row],
                    contact_person=df['Contact Person'][row],                    
                    latlong = pnt,                                      
                )
            if created:
                self.stdout.write('Sucessfully loaded %s' % stfc)