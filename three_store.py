from typing import List, Dict


class TreeStore:

    def __init__(self, items: List[Dict]):
        _items = {}  # Для прямого доступа по айди
        _nodes = {}  # Для хранения дочерних элементов узла

        # Создание корневого узла
        root_item = items[0]
        _nodes[root_item['id']] = []
        _items[root_item['id']] = root_item

        for item in items[1:]:
            _nodes[item['id']] = []
            _nodes[item['parent']].append(item)
            _items[item['id']] = item

        self._nodes = _nodes
        self._items = _items

    def getAll(self) -> List[Dict]:
        # Перебирается только список элементов, сложность O(n), можно было просто сохранить исходный список, но наверное это не подразумевалось
        return list(self._items.values())

    def getItem(self, item_id) -> Dict:
        # Обращение напрямую, сложность O(1)
        return self._items[item_id]

    def getChildren(self, item_id: int) -> List:
        # обращение к элементу напрямую, сложность O(1)
        return self._nodes[item_id]

    def getAllParents(self, item_id: int) -> List:
        # Сложность O(n + 1), где n - кол-во родительских узлов
        item = self._items[item_id]
        if item['parent'] == 'root':
            return []
        parent_id = item['parent']
        return [self._items[parent_id]] + self.getAllParents(parent_id)


example_items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]
ts = TreeStore(example_items)

# Примеры использования:
print(ts.getAll() == example_items)

print(ts.getItem(7) == {"id": 7, "parent": 4, "type": None})
#
print(ts.getChildren(4) == [{"id": 7, "parent": 4, "type": None},
                            {"id": 8, "parent": 4, "type": None}])
print(ts.getChildren(5) == [])
#
print(ts.getAllParents(7) == [{"id": 4, "parent": 2, "type": "test"},
                              {"id": 2, "parent": 1, "type": "test"},
                              {"id": 1, "parent": "root"}])
