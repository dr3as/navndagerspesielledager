#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import calendar
from dateutil import easter
import json


def easter_sunday(year: int):
    """Returnerer dato for første påskedag."""
    return easter.easter(year)


def nth_weekday(year: int, month: int, weekday: int, n: int):
    """Returner f.eks. 2. søndag i februar, siste torsdag i september.
    weekday: 0=mandag ... 6=søndag
    n: 1=første, 2=andre, -1=siste"""
    c = calendar.Calendar()
    days = [
        d for d in c.itermonthdates(year, month)
        if d.month == month and d.weekday() == weekday
    ]
    return days[n - 1] if n > 0 else days[n]


def generate_special_days(year: int):
    """Returnerer dict med {dato: [liste over merkedager]} for gitt år."""
    days = {}
    easter_day = easter_sunday(year)

    def add(date_obj, *names):
        """Legg til merkedager."""
        if not date_obj:
            return
        key = date_obj.strftime("%Y-%m-%d")
        if key not in days:
            days[key] = []
        for name in names:
            if name not in days[key]:
                days[key].append(name)

    # ======== Faste datoer ========
    add(datetime.date(year, 1, 1), "Første nyttårsdag")
    add(datetime.date(year, 1, 4), "Verdens blindeskriftdag")
    add(datetime.date(year, 1, 21), "HKH Prinsesse Ingrid Alexandras fødselsdag")
    add(datetime.date(year, 1, 24), "🍕 Internasjonal pizzadag")
    add(datetime.date(year, 1, 27), "🎂 Sjokoladekakedagen")
    add(datetime.date(year, 2, 5), "🍫 Nutella-dagen")
    add(datetime.date(year, 2, 6), "Den samiske nasjonaldagen")
    add(datetime.date(year, 2, 14), "💘 Valentinsdagen")
    add(datetime.date(year, 2, 21), "Internasjonal morsmålsdag")
    add(datetime.date(year, 2, 21), "HM Haralds Vs fødselsdag")
    add(datetime.date(year, 3, 1), "Internasjonal dag mot all diskriminering")
    add(datetime.date(year, 3, 8), "Kvinnedagen")
    add(datetime.date(year, 3, 14), "🥧 Pi-dagen (3.14)")
    add(datetime.date(year, 3, 17), "St. Patricks Day")
    add(datetime.date(year, 3, 20), "🌍 Internasjonal lykkedag")
    add(datetime.date(year, 3, 21), "🎵 Verdens poesidag")
    add(datetime.date(year, 3, 25), "🧇 Vaffeldagen")
    add(datetime.date(year, 4, 7), "🏃 Verdens helsedag")
    add(datetime.date(year, 4, 14), "🍖 Biff- og bj-dagen")
    add(datetime.date(year, 4, 22), "🌱 Jordens dag")
    add(datetime.date(year, 4, 23), "Verdens Bokdag")
    add(datetime.date(year, 4, 29), "Dansens dag")
    add(datetime.date(year, 5, 1), "⚒️ Arbeidernes dag")
    add(datetime.date(year, 5, 3), "Internasjonal dag for pressefrihet")
    add(datetime.date(year, 5, 4), "🌌 Star Wars-dagen")
    add(datetime.date(year, 5, 8), "Frigjøringsdagen 1945")
    add(datetime.date(year, 5, 9), "🍦 Europeisk iskremdag")
    add(datetime.date(year, 5, 17), "Grunnlovsdagen (Nasjonaldag)")
    add(datetime.date(year, 6, 1), "🐶 Internasjonal hundedag")
    add(datetime.date(year, 6, 5), "Danmarks nasjonaldag")
    add(datetime.date(year, 6, 6), "Sverige nasjonaldag")
    add(datetime.date(year, 6, 7), "Unionsoppløsningen 1905")
    add(datetime.date(year, 6, 14), "Verdens blodgiverdag")
    add(datetime.date(year, 6, 18), "😎 Internasjonal picknickdag")
    add(datetime.date(year, 6, 23), "🔥 Sankthansaften")
    add(datetime.date(year, 6, 24), "☀️ Sankthansdagen")
    add(datetime.date(year, 6, 29), "Persok")
    add(datetime.date(year, 7, 4), "HM Dronning Sonjas fødselsdag")
    add(datetime.date(year, 7, 6), "🍫 Verdens sjokoladedag")
    add(datetime.date(year, 7, 20), "HKH Kronprins Haakon Magnus’ fødselsdag")
    add(datetime.date(year, 7, 29), "Olsok")
    add(datetime.date(year, 7, 30), "Den internasjonale vennskapsdagen")
    add(datetime.date(year, 8, 3), "Vesle Olsok")
    add(datetime.date(year, 8, 8), "🐱 Verdens kattedag")
    add(datetime.date(year, 8, 10), "Larsok")
    add(datetime.date(year, 8, 16), "Rugsok")
    add(datetime.date(year, 8, 24), "Barsok")
    add(datetime.date(year, 9, 5), "🧀 Internasjonal ostedag")
    add(datetime.date(year, 9, 10), "Verdensdagen for selvmordsforebygging")
    add(datetime.date(year, 9, 13), "🎮 Internasjonal gamerdag")
    add(datetime.date(year, 9, 21), "🍂 Høstjevndøgn (ca. 21.–23. september)")
    add(datetime.date(year, 9, 21), "Internasjonal fredsdag")
    add(datetime.date(year, 9, 29), "☕ Internasjonal kaffedag")
    add(datetime.date(year, 10, 1), "💞 Puppedagen (brystkreftbevissthet)")
    add(datetime.date(year, 10, 1), "Internasjonal musikkdag")
    add(datetime.date(year, 10, 4), "🌮 Tacoens dag")
    add(datetime.date(year, 10, 10), "Verdensdagen for psykisk helse")
    add(datetime.date(year, 10, 11), "Den internasjonelle jentedagen")
    add(datetime.date(year, 10, 14), "Den internasjonelle eggdagen")
    add(datetime.date(year, 10, 16), "🍞 Verdens matdag")
    add(datetime.date(year, 10, 17), "Epledagen")
    add(datetime.date(year, 10, 24), "FN-dagen")
    add(datetime.date(year, 10, 31), "🎃 Halloween")
    add(datetime.date(year, 11, 11), "💘 Singlesday")
    add(datetime.date(year, 11, 20), "FNs internasjonale barnedag")
    add(datetime.date(year, 11, 21), "Verdens fjernsynsdag")
    add(datetime.date(year, 11, 13), "😄 Verdens snillhetsdag")
    add(datetime.date(year, 12, 10), "🌍 Menneskerettighetsdagen")
    add(datetime.date(year, 12, 13), "Luciadagen")
    add(datetime.date(year, 12, 21), "❄️ Vintersolverv (ca. 21.–22. desember)")
    add(datetime.date(year, 12, 23), "Lille Julaften")
    add(datetime.date(year, 12, 24), "Julaften")
    add(datetime.date(year, 12, 25), "Første Juledag")
    add(datetime.date(year, 12, 26), "Andre Juledag")
    add(datetime.date(year, 12, 31), "Nyttårsaften")

    # ======== Bevegelige merkedager ========
    add(nth_weekday(year, 2, 6, 2), "💐 Morsdag")  # andre søndag i februar
    add(nth_weekday(year, 11, 6, 2), "👨‍🍼 Farsdag")  # andre søndag i november
    add(easter_day - datetime.timedelta(weeks=7), "🎭 Fastelavn")
    add(easter_day - datetime.timedelta(weeks=7) + datetime.timedelta(days=2), "🥞 Feittirsdag")
    add(easter_day - datetime.timedelta(weeks=7) + datetime.timedelta(days=3), "🙏 Askeonsdag")
    add(easter_day - datetime.timedelta(days=7), "🌿 Palmesøndag")
    add(easter_day - datetime.timedelta(days=3), "🍞 Skjærtorsdag")
    add(easter_day - datetime.timedelta(days=2), "✝️ Langfredag")
    add(easter_day - datetime.timedelta(days=1), "🐣 Påskeaften")
    add(easter_day, "🐰 Første påskedag")
    add(easter_day + datetime.timedelta(days=1), "🐥 Andre påskedag")
    add(easter_day + datetime.timedelta(days=39), "☁️ Kristi Himmelfartsdag")
    add(easter_day + datetime.timedelta(days=49), "🔥 Første pinsedag")
    add(easter_day + datetime.timedelta(days=50), "🔥 Andre pinsedag")

    # ======== Sesong og tid ========
    add(nth_weekday(year, 3, 6, -1), "⏰ Overgang til sommertid (still klokken frem)")
    add(nth_weekday(year, 10, 6, -1), "🕰️ Overgang til vintertid (still klokken tilbake)")

    # ======== Andre bevegelige merkedager ========
    add(nth_weekday(year, 5, 6, 1), "😂 Verdens latterdag")
    add(nth_weekday(year, 9, 3, -1), "🥘 Fårikålens dag")
    add(nth_weekday(year, 10, 4, 2), "🥚 Den internasjonelle eggdagen")
    add(nth_weekday(year, 11, 6, 1), "🕯️ Allehelgensdag")
    add(nth_weekday(year, 11, 3, 4), "🦃 Thanksgiving (USA)")
    thanksgiving = nth_weekday(year, 11, 3, 4)
    add(thanksgiving + datetime.timedelta(days=1), "🛍️ Black Friday")
    add(nth_weekday(year, 6, 5, 2), "🇬🇧 Storbritannias nasjonaldag (2. lørdag i juni)")

    # ======== (FJERNET) Offisielle norske helligdager fra holidays ========
    # Ikke brukt lenger – du har lagt dem inn manuelt.

    return days


def generate_for_years(start: int, end: int):
    """Returnerer alle merkedager mellom to år som ett dict, sortert etter dato."""
    all_days = {}
    for y in range(start, end + 1):
        all_days.update(generate_special_days(y))
    # sorter kronologisk
    return dict(sorted(all_days.items(), key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m-%d")))


def get_special_days_for_date(date_obj: datetime.date):
    """Returnerer liste over merkedager for gitt dato."""
    all_days = generate_for_years(date_obj.year, date_obj.year)
    return all_days.get(date_obj.strftime("%Y-%m-%d"), [])


def get_next_special_day(date_obj: datetime.date):
    """Returnerer (dato, liste) for neste dag med merkedag."""
    specials = generate_for_years(date_obj.year, date_obj.year + 1)
    upcoming = sorted(datetime.date.fromisoformat(k) for k in specials.keys())
    for d in upcoming:
        if d > date_obj:
            return d, specials[d.strftime("%Y-%m-%d")]
    return None, []


if __name__ == "__main__":
    OUTFILE = "spesielledager.json"
    data = generate_for_years(2025, 2027)  # 2025–2027 inkl.
    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Skrev {len(data)} dager til {OUTFILE}")

    # Eksempel på test i terminal
    today = datetime.date.today()
    next_day, desc = get_next_special_day(today)
    print(f"I dag ({today}) er det:", get_special_days_for_date(today))
    print(f"Neste merkedag er {next_day}: {desc}")
