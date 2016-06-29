import building as b
import encoder as e


house = b.House(rooms=[
    b.Kitchen(furniture=[
        b.Refrigerator(type='cool',
                       max_temp=5,
                       min_temp=-5,
                       capacity=100,
                       material='metal',
                       coordinate={'top_left': (0, 0),
                                   'bottom_right': (100, 80)},
                       category='Kitchen',
                       provider='Beko',
                       weight=10,
                       power=250,
                       mean_time=5,)
        ],
        windows=[
            b.Windows(type='window',
                      material='glass',
                      coordinate={'top_left': (0, 0),
                                  'bottom_right': (100, 80)},
                      weight=10,),
        ],
        height=300,
        material='brick',
        coordinate={'top_left': (0, 0),
                    'bottom_right': (600, 600)},
    ),
],)

print('Volume of house:', house.total_volume)
print('Weight of house:', house.total_weight)
print('Energy of house (month):', house.total_energy)

# pe = e.PickleEncoder()
# pe.dump(house)
# house2 = pe.load('house.pickle')

"""
je = e.JSONEncoder()
je.dump(house)
house2 = je.load('house.txt')

print('Volume of house:', house2.total_volume)
print('Weight of house:', house2.total_weight)
print('Energy of house (month):', house2.total_energy)
"""
