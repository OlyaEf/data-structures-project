"""Здесь надо написать тесты с использованием unittest для модуля stack."""

from src.stack import Stack


def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() is True
    assert stack.pop() is None
    assert stack.peek() is None


def test_str_method():
    stack = Stack()

    # Проверяем, что при создании стека строковое представление пустое
    assert str(stack) == "Stack: (None)"

    # Добавляем элементы в стек
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    # Проверяем, что строковое представление содержит верное количество элементов
    assert str(stack) == "Stack: (data3)"

    # Удаляем верхний элемент стека
    stack.pop()

    # Проверяем, что строковое представление обновилось после удаления элемента
    assert str(stack) == "Stack: (data2)"

    # Удаляем оставшиеся элементы
    stack.pop()
    stack.pop()

    # Проверяем, что после удаления всех элементов стека строковое представление пустое
    assert str(stack) == "Stack: (None)"


def test_stack_operations():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.is_empty() is False
    assert stack.peek() == 3

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

    assert stack.is_empty() is True


def test_peek_does_not_remove_element():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.peek() == 2
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_push_pop_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_push_peek_pop_combination():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.peek() == 2
    assert stack.pop() == 2

    stack.push(3)

    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.pop() is None