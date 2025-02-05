import json
from django.core.management.base import BaseCommand
from app.models import Location


class Command(BaseCommand):
    help = 'Imports JSON data into the Location model'

    def handle(self, *args, **kwargs):
        json_data = '''
        {
            "AEAJM": {"name": "Ajman", "city": "Ajman", "country": "United Arab Emirates", "alias": [], "regions": [], "coordinates": [55.5136433, 25.4052165], "province": "Ajman", "timezone": "Asia/Dubai", "unlocs": ["AEAJM"], "code": "52000"},
            "AEAUH": {"name": "Abu Dhabi", "coordinates": [54.37, 24.47], "city": "Abu Dhabi", "province": "Abu Z¸aby [Abu Dhabi]", "country": "United Arab Emirates", "alias": [], "regions": [], "timezone": "Asia/Dubai", "unlocs": ["AEAUH"], "code": "52001"},
            "AEDXB": {"name": "Dubai", "coordinates": [55.27, 25.25], "city": "Dubai", "province": "Dubayy [Dubai]", "country": "United Arab Emirates", "alias": [], "regions": [], "timezone": "Asia/Dubai", "unlocs": ["AEDXB"], "code": "52005"},
            "AEFJR": {"name": "Al Fujayrah", "coordinates": [56.33, 25.12], "city": "Al Fujayrah", "province": "Al Fujayrah", "country": "United Arab Emirates", "alias": [], "regions": [], "timezone": "Asia/Dubai", "unlocs": ["AEFJR"]}
        }
        '''

        data = json.loads(json_data)
        for key, value in data.items():
            Location.objects.update_or_create(
                location_code=key,
                defaults={
                    'name': value['name'],
                    'city': value['city'],
                    'province': value['province'],
                    'country': value['country'],
                    'coordinates': value['coordinates'],
                    'timezone': value['timezone'],
                    'unlocs': value['unlocs'],
                    'alias': value.get('alias', []),
                    'regions': value.get('regions', [])
                }
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))