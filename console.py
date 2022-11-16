import pdb

from models.hiker import Hiker
from models.munro import Munro
from models.region import Region
from models.bagged_munro import Bagged_munro
import repositories.hiker_repository as hiker_repository
import repositories.munro_repository as munro_repository
import repositories.region_repository as region_repository
import repositories.bagged_munro_repository as bagged_munro_repository


bagged_munro_repository.delete_all()
munro_repository.delete_all()
hiker_repository.delete_all()
region_repository.delete_all()


hiker_1 = Hiker("John", "Smith")
hiker_repository.save(hiker_1)

hiker_2 = Hiker("Anna", "Krol")
hiker_repository.save(hiker_2)

hiker_3 = Hiker("Joanna", "Dziewit")
hiker_repository.save(hiker_3)


region_1 = Region("Cairngorms")
region_repository.save(region_1)

region_2 = Region("Fort Williams")
region_repository.save(region_2)

region_3 = Region("Loch Lomond")
region_repository.save(region_3)

region_4 = Region("Perthshire")
region_repository.save(region_4)


munro_1 = Munro("Ben Nevis", region_2, 1345)
munro_repository.save(munro_1)

munro_2 = Munro("Cairn Gorm", region_1, 1245)
munro_repository.save(munro_2)

munro_3 = Munro("Ben Macdui", region_1, 1309)
munro_repository.save(munro_3)

munro_4 = Munro("Ben Vorlich", region_3, 943)
munro_repository.save(munro_4)

munro_3 = Munro("Ben Chonzie", region_4, 931)
munro_repository.save(munro_3)


bagged_munro_1 = Bagged_munro(hiker_1, munro_1, '2020-07-09')
bagged_munro_repository.save(bagged_munro_1)

bagged_munro_2 = Bagged_munro(hiker_2, munro_2, '2021-08-09')
bagged_munro_repository.save(bagged_munro_2)

bagged_munro_3 = Bagged_munro(hiker_3, munro_4, '2021-08-09')
bagged_munro_repository.save(bagged_munro_3)

print(hiker_repository.bagged_munros(67))

pdb.set_trace()