from abc import ABC, abstractmethod
from enum import Enum
import datetime

class Bookingstatus(Enum):

    COMPLETED , REQUESTED , CANCELLED , PENDING ,CHECKED_IN , ABANDONED = 1,2,3,4,5,6


class Seattype(Enum):

    REGULAR , PREMIUM , ACCESIBLE , EMERGENCYEXIT, SHIPPED , OTHER = 1,2,3,4,5,6 


class Accountstatus(Enum):

    ACTIVE , BLOCKED , BANNED , COMPROMISED , ARCHIEVE , UNKNOWN = 1,2,3,4,5,6

class Paymentstatus(Enum):

    COMPLETED , CANCELLED , DECLINED , REFUNDED, UNPAID , PENDING , ABANDONED, SETTLING, FILLED = 1,2,3,4,5,6,7,8,9


class Adress():

    def __init__(self,city,street,state,country,zipcode):

        self.city = city
        self.street = street 
        self.state = state
        self.country = country
        self.zipcode = zipcode

class Account():

    def __init__(self,id,password,status = Accountstatus.ACTIVE):

        self.id = id
        self.password = password
        self.status = status

    def changepassword(self):
        None

class person(ABC):

    def __init__(self,name,phone,email,adress,account):

        self.name = name
        self.email = email
        self.phone = phone
        self.address = adress
        self.account = account

class Customer(person):

    def make_booking(self,booking):
        None

    def get_booking(self,booking):
        None
    



class Admin(person):

    def add_shows(self,show):
        None

    def add_movies(self,movie):
        None
    
    def block_user(self,user):
        None

class Frontdesk(person):

    def create_booking(self,booking):
        None
class guest:

    def register_account(self):
        None

class Show:

    def __init__(self,start_time,end_time,id,movie,played_at):

        self.start_time = start_time
        self.end_time = end_time
        self.id = id
        self.movie = movie
        self.played_at =  played_at
        self.created_on = datetime.date.today()

class Movie:

    def __init__(self,title,language,genre,duration_in_mins,releasedate,country,added_by):

        self.language = language
        self.genre = genre
        self.duration_in_mins = duration_in_mins
        self.releasedate = releasedate
        self.country = country
        self.added_by = added_by
        self.shows = []
        
    def get_shows(self):
            None

class Booking:

    def __init__(self,booking_num,show,payment,num_f_seats,status,show_seats):

        self.booking_num = booking_num
        self.created_on = datetime.date.today()
        self.num_f_seats = num_f_seats
        self.show = show
        self.payment = payment
        self.status = status
        self.show_seats = show_seats

    def cancelbooking(self):
        None
    
    def assign_seats(self,seat):
        None
    def make_payment(self,payment):
        None
         







class Showseats(Cinemaseat):

    def __init__(self,seat_id,price,is_reserved):

        self.id = seat_id
        self.reserved = is_reserved
        self.price = price



class Payment:

    def __init__(self,id,transaction,amount,status):

        self.created_on = datetime.date.today()
        self.amount = amount
        self.transaction = transaction
        self.status = status


class City:

    def __init__(self,name,state,zipcode):

        self.name = name 
        self.state = state
        self.zipcode = zipcode

class Cinemas:

    def __init__(self,name,cinema_halls,halls,location):

        self.name = name
        self.cinema_halls = cinema_halls
        self.halls = halls
        self.location = location

class Cinemahalls:

    def __init__(self,name,seats,total_seats,shows):

        self.name = name
        self.seats = seats
        self.total_seats = total_seats
        self.shows = shows


class Search(ABC):

    def search_by_title(self,title):
        None
    def search_by_language(self,language):
        None
    def search_by_genre(self,genre):
        None
    def search_by_city(self,city):
        None
    def search_by_release_date(self,release_date):
        None

class Catalog(Search):

    def __init__(self):
        self.titles = {}
        self.languages = {} 
        self.genres = {} 
        self.city_names = {}
        self.release_dates = {}

    def search_by_title(self,title):
        return self.titles.get(title)
    def search_by_language(self,language):
        return self.languages.get(language)
    '''
    .
    .
    .
    '''
    def search_by_release_date(self,release_date):
        return self.release_dates.get(release_date)





