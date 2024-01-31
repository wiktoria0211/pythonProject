from DDL import *
import folium


### SZKOLA ###
def utworz_szkole():
    nazwa = input('Nazwa: ')
    kod = input('Kod szkoły: ')
    adres = input('Adres: ')
    miasto = input('Miejscowość: ')
    add = Szkola(nazwa, miasto, kod, adres)

    session.add(add)
    session.commit()


def wyswietl_szkoly_z(miejsce):
    szk_db = session.query(Szkola).filter(Szkola.miasto == miejsce).all()

    if szk_db == []:
        print("Brak szkół w mieście")
    else:
        for id, szkola in enumerate(szk_db):
            print(f'{id + 1}. {szkola.kod} - {szkola.nazwa}')


def usun_szkole():
    kod = input('Kod usuwanej placówki: ')
    szk_db = session.query(Szkola).filter(Szkola.kod == kod).all()
    print(szk_db)
    for szkola in szk_db:
        if szkola.kod == kod:
            session.delete(szkola)

    session.commit()


def modyfikuj_szkole():
    kod = input('Kod modyfikowanej placówki: ')
    szk_db = session.query(Szkola).filter(Szkola.kod == kod).all()

    for szkola in szk_db:
        szkola.nazwa = input('Nazwa: ')
        szkola.kod = input('Kod szkoły: ')
        adres = input('Adres: ')
        szkola.adres = adres
        szkola.miasto = input('Miejscowość: ')
        coords = get_coords(adres)
        szkola.lokalizacja = f'POINT({coords[1]} {coords[0]})'

    session.commit()


### PRACOWNIK ###
def utworz_pracownika():
    imie = input('Imię: ')
    nazwisko = input('Nazwisko: ')
    etat = input('Etat: ')
    kod = input('Kod szkoły: ')
    adres = input('Adres: ')
    miasto = input('Miasto: ')
    add = Pracownik(imie, nazwisko, etat, kod, adres, miasto)

    session.add(add)
    session.commit()


def wyswietl_pracownikow():
    szk_pr = session.query(Pracownik).all()
    if szk_pr == []:
        print("Brak pracowników")
    else:
        for id, pracownik in enumerate(szk_pr):
            print(f'{id + 1}. {pracownik.imie} {pracownik.nazwisko} - {pracownik.etat} - {pracownik.kod_szkoly}')


def wyswietl_pracownikow_z_szkoły(kod):
    szk_pr = session.query(Pracownik).filter(Pracownik.kod_szkoly == kod).all()
    if szk_pr == []:
        print("Brak pracowników")
    else:
        for id, pracownik in enumerate(szk_pr):
            print(f'{id + 1}. {pracownik.imie} {pracownik.nazwisko} - {pracownik.etat} - {pracownik.kod_szkoly}')


def wyswietl_pracownikow_z_miasta(miasto):
    szk_pr = session.query(Pracownik).filter(Pracownik.miasto == miasto).all()
    if szk_pr == []:
        print("Brak pracowników")
    else:
        for id, pracownik in enumerate(szk_pr):
            print(f'{id + 1}. {pracownik.imie} {pracownik.nazwisko} - {pracownik.etat} - {pracownik.kod_szkoly}')


def usun_pracownikow():
    usun = input('Nazwisko nauczyciela do usunięcia: ')
    pr_db = session.query(Pracownik).filter(Pracownik.nazwisko == usun).all()

    u_list = []

    for pracownik in pr_db:
        u_list.append(pracownik)
    print('Znalezieni pracownikcy:')
    print('0. usuń wszystkich')

    for id, do_usuniecia in enumerate(u_list):
        print(id + 1, do_usuniecia.nazwisko)
    nr = int(input('Wybierz pracownika do usunięcia: '))

    if nr == 0:
        for pracownik in u_list:
            session.delete(pracownik)
    else:
        aa = u_list[nr - 1]
        session.delete(aa)
    session.commit()


def modyfikuj_pracownika():
    modyf = input('Nazwisko pracownika do modyfikacji: ')
    pr_db = session.query(Pracownik).filter(Pracownik.nazwisko == modyf).all()

    m_list = []

    if len(pr_db) > 1:

        for pracownik in pr_db:
            m_list.append(pracownik)
        print('Znaleziono takich pracowników:')

        for id, do_modyf in enumerate(m_list):
            print(f"{id + 1}. {do_modyf.imie} {do_modyf.nazwisko} - {do_modyf.etat}")
        number = int(input('Wybierz pracownika do usunięcia: '))

        prac = m_list[number - 1]
        prac.imie = input('Imię: ')
        prac.nazwisko = input('Nazwisko: ')
        prac.etat = input('Etat: ')
        prac.kod_szkoły = input('Kod szkoły: ')
        adres = input('Adres: ')
        pracownik.miasto = input('Miasto: ')
        prac.adres = adres
        coords = get_coords(adres)
        prac.lokalizacja = f'POINT({coords[1]} {coords[0]})'
    else:
        for pracownik in pr_db:
            pracownik.imie = input('Imię: ')
            pracownik.nazwisko = input('Nazwisko: ')
            pracownik.etat = input('Etat: ')
            pracownik.kod_szkoly = input('Kod szkoły: ')
            adres = input('Adres: ')
            pracownik.miasto = input('Miasto: ')
            pracownik.adres = adres
            coords = get_coords(adres)
            pracownik.lokalizacja = f'POINT({coords[1]} {coords[0]})'

    session.commit()


### UCZEN ###
def utworz_ucznia():
    imie = input('Imię: ')
    nazwisko = input('Nazwisko: ')
    klasa = input('Klasa: ')
    adres = input('Adres: ')
    add = Uczen(imie, nazwisko, klasa, adres)

    session.add(add)
    session.commit()


def wyswietl_uczniów():
    szk_ucz = session.query(Uczen).all()
    if szk_ucz == []:
        print("Brak uczniów")
    else:
        for id, uczen in enumerate(szk_ucz):
            print(f'{id + 1}. {uczen.imie} {uczen.nazwisko} - {uczen.klasa}')


def wyswietl_uczniów_z_klasy(klasa):
    szk_ucz = session.query(Uczen).filter(Uczen.klasa == klasa).all()
    if szk_ucz == []:
        print("Brak uczniów")
    else:
        for id, uczen in enumerate(szk_ucz):
            print(f'{id + 1}. {uczen.imie} {uczen.nazwisko} - {uczen.klasa}')


def usun_ucznia():
    usun = input('Nazwisko ucznia do usunięcia: ')
    pr_ucz = session.query(Uczen).filter(Uczen.nazwisko == usun)
    u_list = []

    for uczen in pr_ucz:
        if uczen.nazwisko == usun:
            u_list.append(uczen)
    print('Znalezieni uczniowie:')
    print('0. usuń wszystkich')

    for id, do_usuniecia in enumerate(u_list):
        print(id + 1, do_usuniecia.nazwisko)
    nr = int(input('Wybierz ucznia do usunięcia: '))

    if nr == 0:
        for uczen in u_list:
            session.delete(uczen)
    else:
        aa = u_list[nr - 1]
        session.delete(aa)

    session.commit()


def modyfikuj_ucznia():
    modyf = input('Nazwisko ucznia do modyfikacji: ')
    ucz_db = session.query(Uczen).filter(Uczen.nazwisko == modyf).all()

    m_list = []

    if len(ucz_db) > 1:

        for uczen in ucz_db:
            if uczen.nazwisko == modyf:
                m_list.append(uczen)
        print('Znaleziono takich uczniów:')

        for id, do_modyf in enumerate(m_list):
            print(f"{id + 1}. {do_modyf.imie} {do_modyf.nazwisko} - {do_modyf.klasa}")
        number = int(input('Wybierz ucznia do usunięcia: '))

        prac = m_list[number - 1]
        prac.imie = input('Imię: ')
        prac.nazwisko = input('Nazwisko: ')
        prac.klasa = input('Klasa: ')
        adres = input('Adres: ')
        prac.adres = adres
        coords = get_coords(adres)
        prac.lokalizacja = f'POINT({coords[1]} {coords[0]})'
    else:
        for uczen in ucz_db:
            uczen.imie = input('Imię: ')
            uczen.nazwisko = input('Nazwisko: ')
            uczen.klasa = input('Klasa: ')
            adres = input('Adres: ')
            uczen.adres = adres
            coords = get_coords(adres)
            uczen.lokalizacja = f'POINT({coords[1]} {coords[0]})'

    session.commit()


### MAPY ###

def mapa_szkol():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    szk_db = session.query(Szkola).all()
    for szkola in szk_db:
        coords = convert_point(szkola.lokalizacja)
        folium.Marker(location=coords, popup=f"{szkola.nazwa}").add_to(mapa)
    print('\Wydrukowano')
    mapa.save(f'mapa_szkol.html')


def mapa_pracownikow():
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    prac_db = session.query(Pracownik).all()
    for pracownik in prac_db:
        coords = convert_point(pracownik.lokalizacja)
        folium.Marker(location=coords, popup=f"{pracownik.nazwisko} - {pracownik.etat}").add_to(mapa)
    print('\Wydrukowano')
    mapa.save(f'mapa_pracownikow.html')


def mapa_pracownikow_z_szkoly(kod):
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    prac_db = session.query(Pracownik).filter(Pracownik.kod_szkoly == kod).all()
    for pracownik in prac_db:
        coords = convert_point(pracownik.lokalizacja)
        folium.Marker(location=coords, popup=f"{pracownik.nazwisko} - {pracownik.etat}").add_to(mapa)
    print('\Wydrukowano')
    mapa.save(f'mapa_pracownikow_z_{pracownik.kod_szkoly}.html')


def mapa_uczniow_z_szkoly(klasa):
    mapa = folium.Map(location=[52.3, 21.0], tiles='OpenStreetMap', zoom_start=7)

    prac_db = session.query(Uczen).filter(Uczen.klasa == klasa).all()
    for uczen in prac_db:
        coords = convert_point(uczen.lokalizacja)
        folium.Marker(location=coords, popup=f"{uczen.nazwisko} - {uczen.klasa}").add_to(mapa)
    print('\Wydrukowano')
    mapa.save(f'mapa_uczniow_klasy_{uczen.klasa}.html')


def GUI():
    while True:
        print('\n System zarządzania szkołami, pracownikami i uczniami \n\n'
              f'0: Wyjście\n'
              f'Szkoły\n'
              f'11: Lista  szkół w danym mieście\n'
              f'12: Dodaj  szkołe\n'
              f'13: Usuwanie  szkół w danym miejście\n'
              f'14. Modyfikowanie szkoły\n'
              f'Pracownicy\n'
              f'21. Lista pracowników z wybranej szkoły\n'
              f'22. Lista pracowników z wybranego miasta\n'
              f'23. Tworzenie pracownika\n'
              f'24. Usuwanie pracownika\n'
              f'25. Modyfikacja pracownika\n'
              f'Uczniowie\n'
              f'31. Lista wszystkich uczniów\n'
              f'32. Lista uczniów z klasy\n'
              f'33. Dodawanie ucznia\n'
              f'34. Usuwanie ucznia\n'
              f'35. Modyfikacja ucznia\n'
              f'Maps\n'
              f'41. Mapa wszystkich szkół\n'
              f'42. Mapa wszystkich pracowników\n'
              f'43. Mapa pracowników z wybranej szkoły\n'
              f'44. Mapa uczniów danej klasy\n')
        wybor = int(input('Wybierz funkcje: '))
        print(f'Wybrano {wybor}: \n')

        match wybor:
            case 0:
                print('Zamknij system')
                session.flush()
                engine.dispose()
                break
            case 11:
                print('Lista w szkół w danym miejście')
                miejsce = input('Miasto: ')
                wyswietl_szkoly_z(miejsce)
            case 12:
                print('Dodawanie w szkół')
                utworz_szkole()
            case 13:
                print('Usuwanie  szkół')
                usun_szkole()
            case 14:
                print("Modyfikowanie szkoły")
                modyfikuj_szkole()
            case 23:
                print('Tworzenie pracownika')
                utworz_pracownika()
            case 21:
                print('Lista pracowników z wybranej szkoły')
                kod = input("Podaj kod szkoły: ")
                wyswietl_pracownikow_z_szkoły(kod)
            case 22:
                print('Lista pracowników z wybranego miasta')
                miasto = input('Podaj miasto: ')
                wyswietl_pracownikow_z_miasta(miasto)
            case 24:
                print('Usuwanie pracownika')
                usun_pracownikow()
            case 25:
                print("Modyfikacja pracownika")
                modyfikuj_pracownika()
            case 33:
                print("Dodawanie ucznia")
                utworz_ucznia()
            case 31:
                print('Lista wszytkich uczniów')
                wyswietl_uczniów()
            case 32:
                print("Lista uczniów z klasy")
                klasa = input('Podaj klasę: ')
                wyswietl_uczniów_z_klasy(klasa)
            case 34:
                print('Usuwanie ucznia')
                usun_ucznia()
            case 35:
                print('Modyfikacja ucznia')
                modyfikuj_ucznia()
            case 41:
                print("Mapa wszystkich szkół")
                mapa_szkol()
            case 42:
                print('Mapa wszsytkich pracowników')
                mapa_pracownikow()
            case 43:
                print('Mapa pracowników z wybranej szkoły')
                kod = input('Podaj kod szkoły: ')
                mapa_pracownikow_z_szkoly(kod)
            case 44:
                print("Mapa uczniów danej klasy")
                klasa = input('Podaj klasę: ')
                mapa_uczniow_z_szkoly(klasa)
