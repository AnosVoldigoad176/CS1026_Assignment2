"""
Author: Anh Duc Vu - Harry Vu
Description: Code check for UPC, Basic and Positional
Last modified: Oct 6, 2021
"""



import code_check as cc

bc_list = ["None"]
pc_list = ["None"]
upc_list = ["None"]
none_list = ["None"]

while True:

    num = str(input("Please enter code (digits only) (enter 0 to quit): "))

    if cc.basic_code(num) is True and int(num) != 0:
        if "None" in bc_list:
            bc_list.remove("None")
        bc_list.append(num)
        print("-- code:", num, "valid Basic code.")
    if cc.positional_code(num) is True and int(num) != 0:
        if "None" in pc_list:
            pc_list.remove("None")
        pc_list.append(num)
        print("-- code:", num, "valid Positional code.")
    if cc.UPC_code(num) is True and int(num) != 0:
        if "None" in upc_list:
            upc_list.remove("None")
        upc_list.append(num)
        print("-- code:", num, "valid UPC code.")
    if cc.basic_code(num) is False and cc.positional_code(num) is False and cc.UPC_code(num) is False:
        if "None" in none_list:
            none_list.remove("None")
        none_list.append(num)
        print("-- code:", num, "not Basic, Position or UPC code.")
    if int(num) == 0:
        print()
        print("Summary")
        print("Basic :", ", ".join(bc_list))
        print("Position :", ", ".join(pc_list))
        print("UPC :", ", ".join(upc_list))
        print("None :", ", ".join(none_list))
        exit(0)
