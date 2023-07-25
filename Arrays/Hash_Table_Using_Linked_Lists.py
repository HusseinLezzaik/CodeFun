# **Worst Case = Collision of Values:** Assume hash functions optimized and constant-time operations are guranteed


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        key_hash = self._hash(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._hash(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._hash(key)

        if self.table[key_hash] is None:
            return False

        for i in range (0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True

        return False

# Let's test our hash table
HT = HashTable(4)
HT.insert("a", "1")
HT.insert("b", "2")
HT.insert("c", "3")
print(HT.get("a"))  # prints: 1
print(HT.get("b"))  # prints: 2
HT.delete("b")
print(HT.get("b"))  # prints: None
