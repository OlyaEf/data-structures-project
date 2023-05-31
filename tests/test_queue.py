"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import pytest

from src.queue import Queue


def test_str_method_empty_queue():
    # Создаем пустую очередь
    queue = Queue()

    # Проверяем, что строковое представление пустой очереди верное
    assert str(queue) == ""


def test_str_method_non_empty_queue():
    # Создаем очередь и добавляем элементы
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    # Проверяем, что строковое представление очереди содержит верные данные
    assert str(queue) == "data1\ndata2\ndata3"


def test_enqueue_and_dequeue():
    # Создаем очередь
    queue = Queue()

    # Добавляем элементы в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')

    # Проверяем, что извлечение элементов происходит в правильном порядке
    assert queue.dequeue() == 'data1'
    assert queue.dequeue() == 'data2'

    # Проверяем, что очередь становится пустой после извлечения всех элементов
    assert queue.is_empty()


def test_dequeue_empty_queue():
    # Создаем пустую очередь
    queue = Queue()

    # Пытаемся извлечь элемент из пустой очереди и проверяем, что получаем исключение IndexError
    with pytest.raises(IndexError):
        queue.dequeue()
