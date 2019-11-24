from src.classes import loadBenchFromFile, printBoxStatus, Box
import os

BENCH_2_0 = os.getcwd() + "/../instances/bench_2_0"


def heuristic0(listObj, wListCap):
    items = listObj.copy()
    wItems = wListCap.copy()
    wBox = []
    items.sort(key=lambda x: int(x.weight), reverse=True)
    i = 0
    while items:
        weight = 0
        for item in items:
            weight += int(item.weight)
        wItems.sort(key=lambda val: weight - int(val))
        box = Box(wItems[0], i)
        i += 1
        for item in items:
            if box.addItem(item):
                print(box)
        weight = 0
        for obj in box.listObj:
            weight += int(obj.weight)
        wItems.sort(key=lambda x: weight - int(x))
        box.cap = wItems[0]
        for obj in box.listObj:
            items.remove(obj)
        wBox.append(box)
    return wBox


if __name__ == '__main__':
    listItem, listBox = loadBenchFromFile(BENCH_2_0)
    wb = heuristic0(listItem, listBox)
    printBoxStatus(wb)
