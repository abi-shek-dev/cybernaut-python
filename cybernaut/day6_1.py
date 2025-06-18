
cars = {
    "car1": {"brand": "Koenisegg", "model": "Jesko", "year": 2019},
    "car2": {"brand": "Bugatti", "model": "Chiron", "year": 2016},
    "car3": {"brand": "Pagani", "model": "Huayra BC", "year": 2011}
}

cars["car4"] = {"brand": "McLaren", "model": "P1", "year": 2013}

cars["car2"]["year"] = 2025

del cars["car1"]

print("Remaining cars:")
for car_id, car_info in cars.items():
    print(f"{car_id}: Brand: {car_info['brand']}, Model: {car_info['model']}, Year: {car_info['year']}")
