from models import FitnessTracker

tracker = FitnessTracker("Божидар Миланов")

print("     ФИТНЕС ТРЕКЕР - Демо програма")

aktivnosti_data = [
    ("Бягане",           45, 480),
    ("Колело",           60, 520),
    ("Плуване",          30, 300),
    ("Бягане",           50, 530),
    ("Йога",             40, 180),
    ("Тенис",            55, 420),
    ("Колело",           75, 650),
    ("Ходене",           90, 350),
]

print("\n[1] Добавяне на активности:")
print("-" * 40)
for vid, minuti, kalorii in aktivnosti_data:
    tracker.dobavi_aktivnost(vid, minuti, kalorii)

print("\n[2] Всички активности:")
tracker.pokaji_vsichki()

print("\n[3] Сортирани по калории (низходящо):")
tracker.sortiraj_po_kalorii(nizhodyashto=True)

print("\n[4] Сортирани по калории (възходящо):")
tracker.sortiraj_po_kalorii(nizhodyashto=False)

print("\n[5] Филтриране по вид:")
vidove_za_proverka = ["Бягане", "Колело", "Плуване", "Тенис"]
for vid in vidove_za_proverka:
    tracker.filtriraj_po_vid(vid)

print("\n[6] Активност с най-много калории:")
naj_dobra = tracker.aktivnosti[0]
for a in tracker.aktivnosti:
    if a["kalorii"] > naj_dobra["kalorii"]:
        naj_dobra = a
print(f"  >> {naj_dobra['vid']} | {naj_dobra['minuti']} мин | {naj_dobra['kalorii']} кал")

print("\n[7] Активности над 400 калории:")
nad_400 = [a for a in tracker.aktivnosti if a["kalorii"] > 400]
for a in nad_400:
    print(f"  - {a['vid']:20s} | {a['kalorii']} кал")

print("\n[8] Обобщение и статистика:")
tracker.oboshtenie()
