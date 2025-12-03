class WeaponFactory:
    def __init__(self, start_id):
        self.current_id = int(start_id, 16)

    def __iter__(self):
        return self

    def __next__(self):
        hex_id = hex(self.current_id)[2:]
        self.current_id += 1
        return hex_id


if __name__ == "__main__":
    wf = WeaponFactory("1000face")
    print("------test1-------")
    print(next(wf))
    print(next(wf))
    print(next(wf))

    count = 0
    max_count = 10
    print("------test2-------")
    for id in WeaponFactory("1000f000"):
        print(id)
        count += 1
        if count > max_count:
            break
