# 14:00:01
# 14:00:02
# 14:00:03

for h in range(14, 16):
    m = 0
    s = 0
    if h != 15:
        for m in range(60):
            for s in range(60):
                print(f"{h}:{m}:{s}")
else:
    print(f"{h}:{m}:{s}")
