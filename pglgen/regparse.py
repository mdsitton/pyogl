from collections import OrderedDict

from pglgen import xml

class Command(xml.BaseParser):
    '''Parse xml registry command tags'''

    def init_data(self):

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
    '''Integrate changes from the indivdual Command parsers.'''

    def init_data(self):

        self.commands = []

        self.register_parser('registry/commands/command', Command)

    def integrate(self):
        for cmd in self.commands:
            attr = {
                'parms': cmd.params,
                'return': cmd.rtnType,
            }
            self.root.commands[cmd.name] = attr


class Feature(xml.BaseParser):

    def init_data(self):

        self.name = None
        self.api = None
        self.version = None

        self.default = OrderedDict()
        self.profile_setup(self.default)

        self.profiles = {}

        #self.parent.features.append(self)

    @staticmethod
    def profile_setup(profileDict):
        profileDict.update({
            'require': {
                'enum': [],
                'command': [],
            },
            'remove': {
                'enum': [],
                'command': [],
            }
        })

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()

        if ('feature/require/enum' in tagPath or
            'feature/require/command' in tagPath or
            'feature/remove/enum' in tagPath or
            'feature/remove/command' in tagPath):

            # The xml parser calls the parser when the full tag data is read.
            # So in order to get certain information before that happens a stack
            # traversal is needed. This is to set various information from the
            # feature tag that is needed in various tags contained within the tag.
            if self.name is None or self.version is None or self.api is None:
                ptag, pattrs, pdata = self.stack.peek(posRel=2)
                self.name = pattrs['name']
                self.version = pattrs['number']
                self.api = pattrs['api']

            featureStatus, pattrs, pdata = self.stack.peek(posRel=1)
            if 'profile' in pattrs.keys():
                profile = pattrs['profile']
                if profile not in self.profiles.keys():
                    self.profiles[profile] = OrderedDict()
                    self.profile_setup(self.profiles[profile])

                self.profiles[profile][featureStatus][tag].append(attrs['name'])
            else:
                self.default[featureStatus][tag].append(attrs['name'])

    def integrate(self):

        info = {
            'api': self.api,
            'version': self.version,
            'name': self.name
        }

        features = {
            'info': info,
            'default': self.default,
        }

        # merge any profiles into parent master
        features.update(self.profiles)

        try:
            self.parent.features[self.api]
        except:
            od = OrderedDict()
            od[self.name] =  features
            self.parent.features[self.api] = od
        else:
            self.parent.features[self.api][self.name] = features


class Registry(xml.BaseParser):

    def init_data(self):

        self.enums = OrderedDict()
        self.commands = OrderedDict()
        self.features = OrderedDict()

        self.tag = 'registry'

        self.register_parser('registry/commands', Commands)
        self.register_parser('registry/feature', Feature)

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()

        # No need for a full class to parse enums
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
#       - Feature
