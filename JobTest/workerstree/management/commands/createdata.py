from io import StringIO
from django_seed import Seed
from django.core.management.base import BaseCommand
from workerstree.models import *
import random


class Command(BaseCommand):
    def __init__(self, stdout: StringIO | None = ..., stderr: StringIO | None = ..., no_color: bool = ..., force_color: bool = ...) -> None:
        super().__init__()
        self.seeder = Seed.seeder()
        self.fullname = ['Галина Петрівна Кульшенко', 'Ксенія Володимирівна Гура', 'Яков Андрійович Леонов', 'Сергій Леонідович Богза', 
                         'Віктор Анатолійович Перець', 'Яна Олександрівна Барліт', 'Андрій Андрійович Реготун', 'Степан Владиславович Куцьо',
                         'Іван Кирилович Ганущак', 'Олександра Іванівна Старова']
        self.position = {'Директор': ['director', 5], 
                        'Заступник директора': ['zamdirect', 100],
                        'Головний інженер': ['maining', 1000],
                        'Старший майстер': ['seniormaist', 5000],
                        'Майстер': ['master', 12000],
                        'Інженер': ['ingenire', 15000],
                        'Гірничий': ['mainer', 25000]
                        }

    def handle(self, *args, **kwargs):
        for key, value in self.position.items():
            self.seeder.add_entity(Position, 1, {
                'name': key,
                'slug': value[0]    
            })
            self.seeder.execute()
        
        position = {
            Director : [1, 'Директор'],
            HeadAssistant : [100, 'Заступник директора', 1],
            MainIngenire: [1000, 'Головний інженер', 100],
            SeniorMaster: [7000, 'Старший майстер', 1000],
            Master: [13000, 'Майстер', 7000],
            Ingenire: [20000, 'Інженер',13000],
            Miner: [30000, 'Гірничий', 20000]
        }
        count = 1
        for key, value in position.items():
            self.seeder.add_entity(key, value[0], {
                'fullName': lambda x: random.choice(self.fullname),
                'position': value[1],
                'email': lambda x: self.seeder.faker.email(),
                
            })
            self.seeder.execute()
            if key == Director:
                continue
            for scor in range(1,value[0]):
                posit = key.objects.get(pk=scor)
                posit.boss_id=random.randint(1, value[2])
                posit.pos_n_id=count
                posit.save()
            count+=1
       
       
           
            
         
       
           

        

