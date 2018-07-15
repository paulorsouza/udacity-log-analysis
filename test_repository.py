"""Repository unit tests"""


import pytest
import repository

def test_list_top_articles():
    """Should return top articles in correct order"""
    top3 = repository.list_top_articles(3)
    assert len(top3) == 3
    assert top3[0][0] == 338647
    assert top3[1][0] == 253801
    assert top3[2][0] == 170098
    assert top3[0][1] == 'candidate-is-jerk'
    assert top3[0][2] == 'Candidate is jerk, alleges rival'
    top1 = repository.list_top_articles(1)
    assert len(top1) == 1
    top9 = repository.list_top_articles(9)
    assert len(top9) == 8 # There are just 8 articles

def test_list_authors_views():
    """Should return top authors in correct order"""
    authors = repository.list_authors_views()
    assert len(authors) == 4
    assert authors[0][0] == 507594
    assert authors[1][0] == 423457
    assert authors[2][0] == 170098
    assert authors[3][0] == 84557
    assert authors[0][1] == 'Ursula La Multa'
    assert authors[1][1] == 'Rudolf von Treppenwitz'
    assert authors[2][1] == 'Anonymous Contributor'
    assert authors[3][1] == 'Markoff Chaney'

def test_list_critical_days():
    """Should return days that log more than 1% requests 404"""
    critical_days = repository.list_critical_days()
    assert len(critical_days) == 1
    assert critical_days[0][0].strftime("%Y-%m-%d") == '2016-07-17'