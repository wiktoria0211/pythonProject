from sqlalchemy import create_engine, Sequence, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from geoalchemy2 import Geometry
from UTILITY import *

#POŁĄCZENIE Z BAZĄ#
db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='Kochamkamila1.',
    host='localhost',
    database='postgres',
    port=5432
)
engine = create_engine(db_params)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


#TABELE#
class Szkola(Base):
    __tablename__ = 'Szkoly'
    id = Column(Integer(), Sequence("id_seq"), primary_key=True)
    nazwa = Column(String(100), nullable=True)
    kod = Column(String(100), nullable=True)
    adres = Column(String(100), nullable=True)
    miasto = Column(String(100), nullable=True)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    def __init__(self, nazwa, miasto, kod, adres):
        self.nazwa = nazwa
        self.kod = kod
        self.adres = adres
        self.miasto = miasto
        coords = get_coords(adres)
        self.lokalizacja = f'POINT({coords[1]} {coords[0]})'


class Pracownik(Base):
    __tablename__ = 'Pracownicy'
    id = Column(Integer(), Sequence("id_seq"), primary_key=True)
    imie = Column(String(100), nullable=True)
    nazwisko = Column(String(100), nullable=True)
    etat = Column(String(100), nullable=True)
    kod_szkoly = Column(String(100), nullable=True)
    miasto = Column(String(100), nullable=True)
    adres = Column(String(100), nullable=True)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    def __init__(self, imie, nazwisko, etat, kod, adres, miasto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.kod_szkoly = kod
        self.adres = adres
        self.miasto = miasto
        coords = get_coords(adres)
        self.lokalizacja = f'POINT({coords[1]} {coords[0]})'


class Uczen(Base):
    __tablename__ = 'Uczniowie'
    id = Column(Integer(), Sequence("id_seq"), primary_key=True)
    imie = Column(String(100), nullable=True)
    nazwisko = Column(String(100), nullable=True)
    klasa = Column(String(100), nullable=True)
    adres = Column(String(100), nullable=True)
    lokalizacja = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    def __init__(self, imie, nazwisko, klasa, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.adres = adres
        coords = get_coords(adres)
        self.lokalizacja = f'POINT({coords[1]} {coords[0]})'


Base.metadata.create_all(engine)