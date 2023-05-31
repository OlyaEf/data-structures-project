from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next_node: Optional['Node'] = None) -> None:
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self) -> None:
        self.top = None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: ({self.top.data if self.top else None})"

    def is_empty(self):
        """
        Проверяет, пуст ли стек.

        Returns:
            bool: True, если стек пуст; False, если стек не пуст.
        """
        return self.top is None

    def push(self, data: Any) -> None:
        """
        Добавляет элемент в стек.

        Args:
            data (Any): Элемент, который нужно добавить в стек.
        """
        new_node = Node(data, self.top)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> Any:
        """
        Удаляет и возвращает верхний элемент стека.

        Returns:
            Optional[Any]: Значение верхнего элемента стека или None, если стек пуст.
        """
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self) -> Optional[Any]:
        """
        Возвращает значение верхнего элемента стека без его удаления.

        Returns:
            Optional[Any]: Значение верхнего элемента стека или None, если стек пуст.
        """
        if self.is_empty():
            return None
        return self.top.data


