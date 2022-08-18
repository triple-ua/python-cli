from unicodedata import category
from urllib import response


class Methods:

    @classmethod
    def h(self, program, args):
        print("\nValid syntax for method call is:")
        print("method_name param1:value1 param2:value2")
        
        print("\nParameters in square brackets are optional")

        print("\nMethod: \t\tArguments:\n")
        print("die \t\t\t-")
        print("h \t\t\t-")
        print("whoami \t\t\t-")
        print("get_spends \t\t[category] or [year [, month [, day]]]")
        print("add_spend \t\tcategory, spend, date (in format YYYY-MM-DD)")

        if(program.user.status == "admin"):
            print("")
            print("add_user \t\tlogin, password, status")
            print("clear_spends_table \t-")
            print("delete_user \t\tid")
            print("get_users \t\t-")

    @classmethod
    def whoami(self, program, args):
        print(program.user)

    @classmethod
    def get_users(self, program, args):
        if(program.user.status != "admin"):
            print("Error: you have no permissions to call this method")
            return

        users = program.database.select_all_from("users")
        
        for i, user in enumerate(users):
            print(f"\nUser #{i}:")
            print(f"\tID: {user[0]}")
            print(f"\tLogin: {user[1]}")
            print(f"\tPassword: {user[2]}")
            print(f"\tStatus: {user[3]}")

    @classmethod
    def delete_user(self, program, args):
        if(program.user.status != "admin"):
            print("Error: you have no permissions to call this method")
            return

        try:
            program.database.delete_user(args["id"])
        except:
            print("Error: bad syntax in method's arguments")
            return

        print(f"User with ID = {args['id']} successfully deleted")

    @classmethod
    def add_user(self, program, args):
        if(program.user.status != "admin"):
            print("Error: you have no permissions to call this method")
            return

        columns = []
        values = []

        for key, value in args.items():
            columns.append(f"`{key}`")
            values.append(f"'{value}'")

        columns = ', '.join(columns)
        values = ', '.join(values)

        try:
            program.database.add_user(columns, values)
        except:
            print("Error: bad syntax in method's arguments")
            return

        print(f"New user successfully added")

    @classmethod
    def clear_spends_table(self, program, args):
        if(program.user.status != "admin"):
            print("Error: you have no permissions to call this method")
            return

        print("You're trying to clear table 'spends'")
        confirmation = input("Type 'yes' to continue: ")

        if(confirmation.lower().strip() != "yes"):
            print("Action terminated")
        else:
            program.database.clear_table("spends")
            print("Table 'spends' successfully cleared")

    @classmethod
    def get_spends(self, program, args):
        user_id = program.user.id
        category = ""
        date = ""

        # block below figures out which form
        # of method user requests:
        # 1. get_spends without any parameters
        # 2. get_spends with 'category' parameter
        # 3. get_spends with date parameters
        if('category' in args.keys()):
            # case when user requesting for spends of specific category
            category = f"`category` = '{args['category']}'"
        
        elif('year' in args.keys()):
            # case when user requesting for spends of specific year
            year = args['year']
            month = ""
            day = ""

            if('month' in args.keys()):
                #... specific year AND month
                month = "-" + args['month']

                if('day' in args.keys()):
                    #... specific year AND month AND day
                    day = "-" + args['day']

            date = f"`date` REGEXP '^{year}{month}{day}'"

        try:
            response = program.database.get_spends(user_id, category, date)
        except:
            print("Error: bad syntax in method's arguments")
            return

        spends = {}

        # gathering all categories and spends in groups
        for row in response:
            if(row[1] not in spends.keys()):
                spends[row[1]] = 0

            spends[row[1]] += row[3]

        if(len(spends) == 0):
            print("No spends with specified parameters")
            return
        
        print("\nCategory: \tMoney spend:")

        for category, money_spend in spends.items():
            print(f"{category} \t\t{money_spend}")

    @classmethod
    def add_spend(self, program, args):
        columns = []
        values = []

        columns.append("`user_id`")
        values.append(f"{program.user.id}")

        for key, value in args.items():
            columns.append(f"`{key}`")
            values.append(f"'{value}'")

        columns = ', '.join(columns)
        values = ', '.join(values)

        try:
            program.database.add_spend(columns, values)
        except:
            print("Error: bad syntax in method's arguments")
            return

        print(f"New spend successfully added")