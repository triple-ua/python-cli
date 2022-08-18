from models.methods import Methods

class Command:
    def __init__(self, request, program):
        self.program = program
        self.command, self.args = self.__parse_request(request)

    def execute(self):
        if(not hasattr(Methods, self.command)):
            print(f"Error: method '{self.command}' is not existing")
            print("Type 'h' to see help list")
            return

        # a command below seeks for a spicified
        # method 'self.command' in class 'Methods'
        function = getattr(Methods, self.command)

        function(self.program, self.args)

    def __parse_request(self, request):
        parts = request.split()
        
        command = parts[0]
        args = {}

        for arg in parts[1:]:
            try:
                # there's a convention that right syntax for arguments is
                # arg_name1:arg_value1 arg_name2:arg_value2
                # so this part is responsive for creating a dictionary
                # of arguments in key => value
                pair = arg.split(":")
                key = pair[0]
                value = pair[1]

                # argument value can't be null or empty
                if(value == '' or value == None):
                    raise Exception
            except:
                print("Error: bad syntax in method's arguments")
                return '', ''

            args.update({key: value})

        return command, args