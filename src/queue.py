from typing import Any, Optional


class Node:
    """Класс для узла очереди"""

    def __init__(self, data: Any, next_node: Optional['Node'] = None) -> None:
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

    def is_empty(self) -> bool:
        """
        Проверяет, пустая ли очередь.
        :return:
            Bool: True, если очередь пустая; False, если очередь не пустая.
        """
        return self.head is None

    def enqueue(self, data: Any) -> None:
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self) -> Any:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return value
