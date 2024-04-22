list = [2, 3, 4, 1]
target = 9

def run():
    hashmap = {}
    for i, e in enumerate(list):
        diff = target - e
        if diff in hashmap:
            return (hashmap[diff], i)
        hashmap[e] = i
        print(hashmap)
        
run()
