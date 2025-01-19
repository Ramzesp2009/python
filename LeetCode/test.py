
cats = [False]*100
for cat in cats:
    if cat == False:
        for i in cats[1:]:
            cat[cat] = True
print(cats)
# print(cats)


