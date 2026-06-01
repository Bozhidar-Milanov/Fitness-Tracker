from datetime import date
from tabulate import tabulate


class FitnessTracker:
    """Клас за проследяване на фитнес активности."""

    def __init__(self, potrebitel):
        self.potrebitel = potrebitel
        self.aktivnosti = []

    def dobavi_aktivnost(self, vid, minuti, kalorii):
        """Добавя нова активност с дата, вид, минути и изгорени калории."""
        aktivnost = {
            "data": str(date.today()),
            "vid": vid,
            "minuti": minuti,
            "kalorii": kalorii,
        }
        self.aktivnosti.append(aktivnost)
        print(f"[+] Добавена активност: {vid} | {minuti} мин | {kalorii} кал")

    def pokaji_vsichki(self):
        """Показва всички активности в таблица."""
        if not self.aktivnosti:
            print("[!] Няма записани активности.")
            return
        print(f"\n--- Активности на {self.potrebitel} ---")
        print(tabulate(self.aktivnosti, headers="keys", tablefmt="rounded_outline"))

    def sortiraj_po_kalorii(self, nizhodyashto=True):
        """Сортира активностите по изгорени калории (низходящо по подразбиране)."""
        sortirani = sorted(self.aktivnosti, key=lambda x: x["kalorii"], reverse=nizhodyashto)
        red = "низходящо" if nizhodyashto else "възходящо"
        print(f"\n--- Сортирани по калории ({red}) ---")
        print(tabulate(sortirani, headers="keys", tablefmt="rounded_outline"))
        return sortirani

    def filtriraj_po_vid(self, vid):
        """Филтрира активностите по вид (напр. 'Бягане')."""
        rezultat = [a for a in self.aktivnosti if a["vid"].lower() == vid.lower()]
        if not rezultat:
            print(f"[!] Няма активности от вид '{vid}'.")
        else:
            print(f"\n--- Активности от вид: {vid} ---")
            print(tabulate(rezultat, headers="keys", tablefmt="rounded_outline"))
        return rezultat

    def oboshtenie(self):
        """Показва обобщена статистика — калории, минути и препоръка."""
        if not self.aktivnosti:
            print("[!] Няма данни за обобщение.")
            return

        obshto_kalorii = sum(a["kalorii"] for a in self.aktivnosti)
        obshto_minuti = sum(a["minuti"] for a in self.aktivnosti)
        broi = len(self.aktivnosti)

        print(f"\n=== Обобщение за {self.potrebitel} ===")
        print(f"  Общо активности  : {broi}")
        print(f"  Общо минути      : {obshto_minuti} мин")
        print(f"  Общо калории     : {obshto_kalorii} кал")
        print(f"  Средно кал/сесия : {obshto_kalorii / broi:.1f} кал")

        print("\n  Препоръка:")
        if obshto_kalorii >= 2000:
            print("  >> Отлична седмица! Продължавай така!")
        elif obshto_kalorii >= 1000:
            print("  >> Добър напредък! Опитай се да добавиш още малко.")
        else:
            print("  >> Все още е малко. Постави си по-висока цел!")
