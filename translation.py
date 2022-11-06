dict_en_to_pl_days = {
    "Mo": "Pon",
    "Mon": "Pon",
    "Tu": "Wt",
    "Tue": "Wt",
    "Tues": "Wt",
    "We": "Śr",
    "Wed": "Śr",
    "Th": "Czw",
    "Thu": "Czw",
    "Thur": "Czw",
    "Thurs": "Czw",
    "Fr": "Pt",
    "Fri": "Pt",
    "Sa": "Sob",
    "Sat": "Sob",
    "Su": "Niedz",
    "Sun": "Niedz",
}

dict_en_to_pl_months = {
    "Jan": "st",
    "Feb": "lut",
    "Mar": "mrz",
    "Apr": "kw",
    "May": "maj",
    "Jun": "cz",
    "Jul": "lip",
    "Aug": "sier",
    "Sep": "wrz",
    "Oct": "paź",
    "Nov": "li",
    "Dec": "gr",
}

def is_trans_to_pl():
    flag = str(input('Polskie nazwy dni/miesięcy wpisz 1, angielski nazwy dni miesięcy wpisz 2'))
    return flag


def translation_pl():
    pass
print(dict[1].values)