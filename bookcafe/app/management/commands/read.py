import json
from django.core.management.base import BaseCommand, CommandParser
from ...models import Book

class Command(BaseCommand):
    help='load json data from a file into the database'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_file', type=str,help='path to the json file')
    def handle(self, *args, **options):
        json_file_path=options['json_file']
        try:
            with open(json_file_path,'r') as file:
                data_list=json.load(file)
            for item in data_list:
                # 모델에 맞게 데이터를 저장
                Book.objects.create(
                    title=item['name'],
                    price=item['price'],
                    cover_image_url=item['image']
                )
            self.stdout.write(self.style.SUCCESS('Success'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('file not found'))
                              