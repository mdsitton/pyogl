from pglgen import xml

class Command(xml.BaseParser):

    def __init__(self, xmlParser, tag, parent, root):
        super(Command, self).__init__(xmlParser, tag, parent, root)

        self.name = None
        self.rtnType = []
        self.params = []

        self.protoParam = []

        self.parent.commands.append(self)

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()
        if 'command/proto/name' in tagPath:
            self.name = data[0]
        elif 'command/proto' in tagPath:
            for i in data:
                if i not in self.rtnType and i is not '':
                    if '*' in i and len(i) > 1: # split pointer from type
                        info = i.split(' ')
                        self.rtnType.extend(info)
                    else:
                        self.rtnType.append(i)
        elif 'command/param/name' in tagPath:
            self.params.append([data[0].strip(), self.protoParam])
            self.protoParam = []
        elif 'command/param' in tagPath:
            for i in data:
                if i not in self.protoParam and i is not '':
                    if '*' in i and len(i) > 1: # split pointer from type
                        info = i.split(' ')
                        self.protoParam.extend(info)
                    else:
                        self.protoParam.append(i)


class Commands(xml.BaseParser):

    def __init__(self, xmlParser, tag, parent, root):
        super(Commands, self).__init__(xmlParser, tag, parent, root)
        self.commands = []

        self.register_parser('registry/commands/command', Command)

    def parse(self):
        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()

    def integrate(self):
        for cmd in self.commands:
            attr = {
                'parms': cmd.params,
                'return': cmd.rtnType,
            }
            self.root.commands[cmd.name] = attr


class Registry(xml.BaseParser):

    def __init__(self, xmlParser, tag, parent, root):
        super(Registry, self).__init__(xmlParser, tag, parent, root)

        self.enums = {}
        self.commands = {}

        self.tag = 'registry'

        self.register_parser('registry/commands', Commands)

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()


        if 'registry/enums/enum' in tagPath:
            self.enums[attrs['name']] = attrs['value']

def parse_registry(xmlFile):
    reg = xml.parse_xml(Registry, xmlFile)
    return (reg.enums, reg.commands)


#  Higher level Tree-like View of parser classes.
#
#     - Registry
#       - Commands
#         - Command