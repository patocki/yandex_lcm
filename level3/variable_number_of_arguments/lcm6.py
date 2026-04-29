def key_and_lock(key: int, *locks):
    true_locks = []
    key_str = str(key)
    for lock in locks:
        lock_temp = str(lock)
        key = str(key)
        key_dgt = 0
        for i in range(len(lock_temp)):
            if lock_temp[i] == key[key_dgt]:
                key_dgt += 1
            if key_dgt == len(key):
                true_locks.append(lock)
                break
    return true_locks


# print(key_and_lock(12345, *(2100231400566, 1203056, 331203045)))
