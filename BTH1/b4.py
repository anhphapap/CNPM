import json


def read_data():
    with open("./data/data.json") as file:
        employees = json.load(file)
    return employees


def show_list(employees = []):
    for k in employees:
        print(f"Ma nhan vien: {k['ma_nv']}\nTen nhan vien: {k['ten_nv']}")


def find_empl(name):
    print("===KQ tim kiem===")
    for e in employees:
        if name in e['ten_nv']:
            print(f"Ma nhan vien: {e['ma_nv']}\nTen nhan vien: {e['ten_nv']}")


def remove_empl(id):
    print("===KQ xoa===")
    for k in employees:
        if k['ma_nv'] == id:
            employees.remove(k)
    with open("./data/data.json","w") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)
    show_list(employees)


def add_empl(id, name):
    print("===KQ them===")
    employees.append({'ma_nv': id, 'ten_nv': name})
    with open("./data/data.json","w") as file:
        json.dump(employees, file, ensure_ascii=False, indent=4)
    show_list(employees)


employees = read_data()
show_list(employees)
# find_empl("C")
# remove_empl(1)
add_empl(1,"Tran Van A")
