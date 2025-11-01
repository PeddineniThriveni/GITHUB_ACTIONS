from SRC.math_operations import add,sub

def test_add():
   assert add(3,5)==8
   assert add(1,2)==3

def test_sub():
    assert sub(5,6)==-1
    assert sub(9-8)==1