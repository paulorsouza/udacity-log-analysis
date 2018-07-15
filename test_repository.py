"""Repository unit tests"""


import pytest
import repository

def test_list_top_articles():
    """Should return top articles in correct order"""
    top3 = repository.get_top_articles(3)
    assert len(top3) == 3
    assert top3[0][0] == 338647 
    assert top3[1][0] == 253801 
    assert top3[2][0] == 170098
    assert top3[0][1] == 'candidate-is-jerk'
    assert top3[0][2] == 'Candidate is jerk, alleges rival'
    top1 = repository.get_top_articles(1)
    assert len(top1) == 1
    top9 = repository.get_top_articles(9)
    assert len(top9) == 8 # There are just 8 articles
    