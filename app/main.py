from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner,  movie):
    customer_objects = []

    for data in customers:
        customer_obj = Customer(name=data["name"], food=data["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=data["food"], customer=customer_obj)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
