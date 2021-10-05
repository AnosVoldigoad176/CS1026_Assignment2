import code_check as cc

bc_list = ["None"]
pc_list = ["None"]
upc_list = ["None"]
none_list = ["None"]

while True:
    num = int(input("Please enter code (digits only) (enter 0 to quit): "))

    if cc.basic_code(num) is True and num != 0:
        bc_list.remove("None")
        bc_list.append(num)
        print("-- code:", str(num), "valid Basic code.")
    if cc.positional_code(num) is True and num != 0:
        pc_list.remove("None")
        pc_list.append(num)
        print("-- code:", str(num), "valid Positional code.")
    if cc.UPC_code(num) is True and num != 0:
        upc_list.remove("None")
        upc_list.append(num)
        print("-- code:", str(num), "valid UPC code.")
    if cc.basic_code(num) is False and cc.positional_code(num) is False and cc.UPC_code(num) is False:
        none_list.remove("None")
        none_list.append(num)
        print("-- code:", str(num), "not Basic, Position or UPC code.")
    if num == 0:
        print("Summary")
        print("Basic :", str(bc_list)[1:-1])
        print("Position :", str(pc_list)[1:-1])
        print("UPC :", str(upc_list)[1:-1])
        print("None :", str(none_list)[1:-1])
        exit(0)
