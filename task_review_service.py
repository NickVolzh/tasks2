# Пример кода 1. Файл test_add_house

#Асбстрактный сервис по созданию сущности дома и квартир в нем (для ТСЖ)
 
from model.new_house import New_house
from model.rooms import Rooms
import time
 
 
def test_add_house(app):
        app.new_house.fill_info(New_house(district="Железнодорожный", street="Тестовая", house_number="1",
                                          postal_index="630132", tech_status="90",
                                          maintenance_date="01.01.1992", build_date="01.01.1991",
                                          surrounding_area="500", roof_area="250", attic_area="250",
                                          cellar_area="250", stairs_area="300"))
 
        time.sleep(3)
 
        app.rooms.fill_flats(Rooms(entrance="1", room_number="1", floor_number="1",
                                   total_area="45", living_area="28"))
  
 
# Пример кода 2. Файл edit_house

from model.new_house import New_house
 
 
def test_modify_house(app):
    app.new_house.modify_first_house(New_house(district="Ленинский", street="ТестоваяИзмененная", house_number="2",
                                      postal_index="630054", tech_status="95", surrounding_area="600",
                                       roof_area="350", attic_area="350", cellar_area="350", stairs_area="200"))
