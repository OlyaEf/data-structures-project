import pytest

from src.linked_list import LinkedList


def test_linked_list():
    # Создаем пустой односвязный список
    ll = LinkedList()

    # Проверяем пустой список
    assert str(ll) == "None"

    # Добавляем данные в начало списка
    ll.insert_beginning({'id': 1})
    assert str(ll).strip() == "{'id': 1} -> None"

    # Добавляем данные в конец списка
    ll.insert_at_end({'id': 2})
    assert str(ll).strip() == "{'id': 1} -> {'id': 2} -> None"

    # Добавляем еще данные в конец списка
    ll.insert_at_end({'id': 3})
    assert str(ll).strip() == "{'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    # Добавляем данные в начало списка
    ll.insert_beginning({'id': 0})
    assert str(ll).strip() == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_insert_beginning():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'name': 'Alice'})
    assert str(ll) == "{'id': 1, 'name': 'Alice'} -> None"


def test_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end({'id': 1, 'name': 'Alice'})
    assert str(ll) == "{'id': 1, 'name': 'Alice'} -> None"


def test_to_list():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'name': 'Alice'})
    ll.insert_at_end({'id': 2, 'name': 'Bob'})
    ll.insert_at_end({'id': 3, 'name': 'Charlie'})
    lst = ll.to_list()
    assert lst == [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]


def test_get_data_by_id():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'name': 'Alice'})
    ll.insert_at_end({'id': 2, 'name': 'Bob'})
    ll.insert_at_end({'id': 3, 'name': 'Charlie'})
    user_data = ll.get_data_by_id(2)
    assert user_data == {'id': 2, 'name': 'Bob'}


def test_get_data_by_id_not_found():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'name': 'Alice'})
    ll.insert_at_end({'id': 2, 'name': 'Bob'})
    ll.insert_at_end({'id': 3, 'name': 'Charlie'})
    user_data = ll.get_data_by_id(4)
    assert user_data is None


def test_get_data_by_id_non_dict_data():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'name': 'Alice'})
    ll.insert_at_end('Invalid Data')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'name': 'Bob'})
    user_data = ll.get_data_by_id(2)
    assert user_data == {'id': 2, 'name': 'Bob'}


if __name__ == '__main__':
    pytest.main()