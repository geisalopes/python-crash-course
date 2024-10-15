def build_car(manufacturer, model, **car_info):
    """Build a dictionary that contain information about a car"""
    car_info["manufactorer_name"] = manufacturer
    car_info["model_type"] = model
    return car_info


car_profile = build_car("fiat", "500", color="teal", tow_package=True)
print(car_profile)
car_profile = build_car("opel", "opala", year="1986", color="red", headlights="pop up")
print(car_profile)
