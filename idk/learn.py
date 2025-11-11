import time

while True:
    for i in range(5):
        print("\nLearning")
        for y in range(3):
            time.sleep(0.4)
            print(".")
        time.sleep(1)
                    
    var = input("\nIf you wanna stop learning type y: ")

    if var == "y":
        print("Learning stopped")
        break
    else:
        continue