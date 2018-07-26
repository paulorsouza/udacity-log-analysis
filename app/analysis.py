#!/usr/bin/env python3
from texttable import Texttable
import repository


def draw_top_articles():
    texttable = Texttable()
    texttable.add_row(['Titulo', 'Visualizações'])
    for article in repository.list_top_articles(3):
        texttable.add_row([article[2], article[0]])
    print('''||===========================================
        ====================||''')
    print('''||1. Quais são os três artigos mais populares
        de todos os tempos?||''')
    print('''||===========================================
        ====================||''')
    print(texttable.draw())


def draw_top_authors():
    texttable = Texttable()
    texttable.add_row(['Autor', 'Visualizações'])
    for author in repository.list_authors_views():
        texttable.add_row([author[1], author[0]])
    print('''||================================================
        ====================||''')
    print('''||2. Quem são os autores de artigos mais populares
        de todos os tempos?||''')
    print('''||================================================
        ====================||''')
    print(texttable.draw())


def draw_critical_days():
    texttable = Texttable()
    texttable.add_row(['Dia', '%'])
    for day in repository.list_critical_days():
        date = day[0].strftime("%Y-%m-%d")
        error = day[1]
        success = day[2]
        perc = ((error * 100) / (error + success))
        texttable.add_row([date, perc])
    print('''||=============================================
        ======================||''')
    print('''||3. Em quais dias mais de 1'%' das requisições
        resultaram em erros?*||''')
    print('''||=============================================
        ======================||''')
    print(texttable.draw())


draw_top_articles()
draw_top_authors()
draw_critical_days()
