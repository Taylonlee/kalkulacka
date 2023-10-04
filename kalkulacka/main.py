from kalkulačka import Kalkulacka

try:
    pokracovat = "ano"
    while pokracovat == "ano":
        kalkulacka = Kalkulacka()
        kalkulacka.main()
        print(kalkulacka.scitani())
        print(kalkulacka.odecitani())
        print(kalkulacka.nasobeni())
        print(kalkulacka.deleni())
        while True:
            pokracovat = input("\nPřeješ si zadat jiný příklad? (ano/ne): ")
            if pokracovat in ["ano", "ne"]:
                break
            else:
                print("Zadej buď ANO nebo NE.")
    print("Děkuji za využití Kalkulačky! Přeji hezký den! :-)")
except KeyboardInterrupt:
    print("Ooops, chybička se vloudila! :-(")