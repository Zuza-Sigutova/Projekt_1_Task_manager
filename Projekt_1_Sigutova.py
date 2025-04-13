ukoly = [ ]

def pridat_ukol():
    while True:
      nazev_ukol=input("\nZadejte název úkolu: ").strip()    
      ukol_popis=input("Zadejte popis úkolu: ").strip()
    
      if nazev_ukol and ukol_popis:
        novy_ukol = { 'nazev_ukol': nazev_ukol, 'ukol_popis': ukol_popis}

        ukoly.append(novy_ukol)
        print(f"Ukol '{nazev_ukol}' byl přidán.")
        break
      else:
        print("\nPole název a popis nesmí být prázdné, zadejte prosím znovu.")

def zobrazit_ukoly():
   print("\nSeznam úkolů:")
   for i, ukol in enumerate(ukoly, start = 1 ):
      print(f"{i}.{ ukol ['nazev_ukol']} - {ukol['ukol_popis']}")


def odstranit_ukol():
   zobrazit_ukoly()
   try:
      cislo = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))
      if 1 <= cislo <= len(ukoly):
         odstranene = ukoly.pop(cislo-1)
         print(f"Úkol' {odstranene['nazev_ukol']}' byl odstraněn.")
      else:
        print("Zadaný úkol neexistuje.")
   except ValueError:
         print("Zadejte platné číslo.") 
    

def hlavni_menu():
    """Tato funkce zobrazí Hlavní menu."""
    while True:
       print("\nSprávce úkolů - Hlavní menu")
       print("1. Přidat nový úkol \n2. Zobrazit všechny úkoly \n3. Odstranit úkol \n4. Konec programu")
       ukol_moznost=input("Vyberte možnost (1-4): ")
       if ukol_moznost == "1":
          pridat_ukol()
       elif ukol_moznost == "2":
          zobrazit_ukoly() 
       elif ukol_moznost == "3":
          odstranit_ukol()    
       elif ukol_moznost == "4":
          print("\nKonec programu.")
          break
       else:
        print("\nZadaná neplatná volba. Zadejte prosím znovu.")  

hlavni_menu()
   