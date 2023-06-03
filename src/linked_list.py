from typing import Optional, List, Union


class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node: Optional['Node'] = None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return 'None'

        ll_string = ''
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def to_list(self) -> List[dict]:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        node: Optional[Node] = self.head
        data_list: List[dict] = []
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, id: Union[int, str]) -> Optional[dict]:
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению."""
        node: Optional[Node] = self.head
        while node:
            try:
                if 'id' in node.data and node.data['id'] == id:
                    return node.data
            except TypeError:
                print("Ошибка: данные не являются словарем или в словаре отсутствует ключ 'id'")
            node = node.next_node
        return None
