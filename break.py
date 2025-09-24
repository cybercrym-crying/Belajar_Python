# break akan membuat loop berhenti pada posisi nya sehingga code setelahnya akan di lewati juga
i = 0
while True:
    if i == 3:
        print("stop")
        break
    print(i)
    i += 1
