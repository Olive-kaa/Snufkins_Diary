import pdb

from models.hiker import Hiker
from models.munro import Munro
from models.region import Region
import repositories.hiker_repository as hiker_repository
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository

print("Deleting all...")
hiker_repository.delete_all()
munro_repository.delete_all()
region_repository.delete_all()

print("Hikers...")
hiker_1 = Hiker("John", "Smith")
hiker_repository.save(hiker_1)

hiker_2 = Hiker("Anna", "Krol")
hiker_repository.save(hiker_2)

hiker_3 = Hiker("Joanna", "Dziewit")
hiker_repository.save(hiker_3)

print("regions....")
region_1 = Region("Cairngorms")
region_repository.save(region_1)

region_2 = Region("Fort Williams")
region_repository.save(region_2)

print("Munros")
munro_1 = Munro("Ben Nevis", region_2, 1345)
munro_repository.save(munro_1)

munro_2 = Munro("Cairn Gorm", region_1, 1245)
munro_repository.save(munro_2)

munro_3 = Munro("Ben Macdui", region_1, 1309)
munro_repository.save(munro_3)



pdb.set_trace()