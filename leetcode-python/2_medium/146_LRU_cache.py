######### LeetCode Problem N°146 - LRU Cache (Medium) ################
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#   - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#   - int get(int key) Return the value of the key if the key exists, otherwise return -1.
#   - void put(int key, int value) Update the value of the key if the key exists. 
#     Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
#     from this operation, evict the least recently used key.
#   - The functions get and put must each run in O(1) average time complexity.
#
# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
# Constraints:
#   - 1 <= capacity <= 3000
#   - 0 <= key <= 10**4
#   - 0 <= value <= 10**5
#   - At most 2 * 10**5 calls will be made to get and put.
#
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        
    def get(self, key: int) -> int:
        '''Consume una Key de la Cache. IMPORTANTE: Space O(1)'''
        # Tras consumir un elemento, debo moverlo al final de la cola
        value = self.keys.pop(key, -1)
        if value != -1:
            self.keys[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        '''Crea (o actualiza) una Key en la Cache. IMPORTANTE: Space O(1)'''
        # Sea una Key nueva o una actualización, debo mandarlo al final de la cola 
        # por eso, primero hago 'pop' y no 'get'
        if self.keys.pop(key, -1) == -1 and len(self.keys) == self.capacity:
            # key nueva y capacidad actual maxima, elimino key mas antigua
            self.keys.pop(next(iter(self.keys)))        
        self.keys[key] = value 

    def __repr__(self):
        return f'LRUCache(capacity={self.capacity}, keys={self.keys})'

# Pruebas
test1={
    'method': ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], 
    'arg': [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    'out_exp': [None,None,None,1,None,-1,None,-1,3,4]
}
test1={
    'method': ["LRUCache","get","put","get","put","put","get","get"], 
    'arg': [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]],
    'out_exp': [None,-1,None,-1,None,None,2,6], 
}


tests = [test1]
for test in tests:
    out = []
    for method, arg, out_exp in zip(test['method'], test['arg'], test['out_exp']):
        if method == 'LRUCache':
            capacity = arg[0]
            obj = LRUCache(capacity)            
            out.append(obj)
        elif method == 'put':
            key, value= arg[0], arg[1]
            res = obj.put(key, value)
            out.append(res)
        elif method == 'get':
            key = arg[0]
            res = obj.get(key)
            out.append(res)
        print(obj)
    print('Resultado esperado:', test['out_exp'])
    print('Resultado:', out)

