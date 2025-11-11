def nejsi():
    print("Nejsi stary mladenec")

if input("Jsi muz? [ano], [ne]: ") == "ano":
    if input("Byl jsi nekdy zenaty? [ano], [ne]: ") == "ne":
        if input("Povazujes se za stareho? [ano], [ne]: ") == "ano":
            print("Jsi stary mladenec")
        else:
            nejsi()
    else:
        nejsi()
else:
    nejsi()