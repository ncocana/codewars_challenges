# import another directory's module
from src.n_smallest_elements_in_original_order import first_n_smallest
import pytest


@pytest.mark.first_n_smallest
def test_first_n_smallest():
    assert first_n_smallest([1,2,3,4,5],3) == [1,2,3]
    assert first_n_smallest([5,4,3,2,1],3) == [3,2,1]
    assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
    assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
    assert first_n_smallest([1,2,3,4,5],0) == []
    assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
    assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
    assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
    assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
    assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]