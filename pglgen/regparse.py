from collections import OrderedDict
import os

from pglgen import xmlparse as xml


class Command(xml.BaseParser):
    '''Parse xml registry command tags'''

    def init_data(self, apiFile):

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
            self.rtnType.extend(data)
        elif 'command/param/name' in tagPath:
            self.params.append([data[0].strip(), ' '.join(self.protoParam).strip()])
            self.protoParam = []
        elif 'command/param' in tagPath:
            self.protoParam.extend(data)


class Commands(xml.BaseParser):
    '''Integrate changes from the indivdual Command parsers.'''

    def init_data(self, apiFile):

        self.commands = []

        self.register_parser('registry/commands/command', Command)

    def integrate(self):
        for cmd in self.commands:
            attr = {
                'parms': cmd.params,
                'return': ' '.join(cmd.rtnType).strip(),
            }
            self.root.commands[cmd.name] = attr


class Feature(xml.BaseParser):

    def init_data(self, apiFile):

        self.name = None
        self.api = None
        self.version = None

        self.default = OrderedDict()
        self.profile_setup(self.default)

        self.profiles = OrderedDict()

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
                    self.profiles[profile] = {}
                    self.profile_setup(self.profiles[profile])

                self.profiles[profile][featureStatus][tag].append(attrs['name'])
            else:
                # skip opengl 1.0 enums in opengl 1.1
                if (hasattr(self.root, 'gl1Enums') and tag == 'enum' and
                        self.version == '1.1' and attrs['name'] in self.root.gl1Enums):
                    return
                self.default[featureStatus][tag].append(attrs['name'])

    def integrate(self):

        info = {
            'api': self.api,
            'version': self.version,
            'name': self.name
        }
        # Add in the enums for opengl 1.0
        if hasattr(self.root, 'gl1Enums') and self.api == "gl" and self.version == '1.0':
            self.default['require']['enum'].extend(self.root.gl1Enums)

        features = OrderedDict([
            ('info', info),
            ('default', self.default)
        ])

        # merge any profiles into parent master
        features.update(self.profiles)

        try:
            self.parent.features[self.api]
        except:
            od = OrderedDict()
            od[self.name] = features
            self.parent.features[self.api] = od
        else:
            self.parent.features[self.api][self.name] = features


class Extensions(xml.BaseParser):

    def init_data(self, apiFile):

        self.name = None
        self.supported = None
        self.version = None

        self.extensions = OrderedDict()

        self.requireBlockAPI = None
        self.requireBlockProfile = 'default'

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()

        #if 'registry/extensions/extension/require/enum'
        if ('extension/require/enum' in tagPath or
            'extension/require/command' in tagPath):

            #if self.name is None or self.supported is None:
            ptag, pattrs, pdata = self.stack.peek(posRel=2)
            self.name = pattrs['name']
            self.supported = pattrs['supported'].split('|')

            # quick hack until we can properly handle core vs compatibility profile.
            if 'glcore' in self.supported:
                if 'gl' not in self.supported:
                    self.supported = ['gl']
                else:
                    self.supported.remove('glcore')


            ptag, pattrs, pdata = self.stack.peek(posRel=1)
            if 'profile' in pattrs:
                self.requireBlockProfile = pattrs['profile']
            else:
                self.requireBlockProfile = 'default'

            # This is to restrict a subset of a extension to a specific api.
            if 'api' in pattrs:
                self.requireBlockAPI = pattrs['api']
            else:
                self.requireBlockAPI = None

            prof = self.requireBlockProfile

            for api in self.supported:
                if self.requireBlockAPI is None or self.requireBlockAPI == api:

                    # this is to detect if the dict structure is setup
                    # if not we create it.
                    try:
                        self.extensions[api]
                    except KeyError:
                        self.extensions[api] = OrderedDict()

                    try:
                        self.extensions[api][self.name]
                    except KeyError:
                        self.extensions[api][self.name] = {}

                    try:
                        self.extensions[api][self.name][prof]
                    except KeyError:
                        self.extensions[api][self.name][prof] = {'enum': [], 'command': []}

                    self.extensions[api][self.name][prof][tag].append(attrs['name'])

    def integrate(self):
        self.parent.extensions.update(self.extensions)


class Registry(xml.BaseParser):

    def init_data(self, apiFile):

        self.enums = OrderedDict()
        self.commands = OrderedDict()

        # The dictionary structure for defining features and extensions
        # One difference between features and extensions is that afik there
        # is not any instances of an extension removing features.
        # gl.xml is also the only file that uses profiles, so everything should
        # be found in default for those.
        # features = {
        #     gl: {                        # api
        #         GL_VERSION_1_0: {        # name
        #             'info': { # info only for opengl features not ext.
        #                 'api': gl,
        #                 'version': 1.0,
        #                 'name': GL_VERSION_1_0,
        #             },
                      # Within profiles extensions dont have remove or require.
        #             'default': {  # Items in default are port of all profiles
        #                 'require': {
        #                     'enum': [],
        #                     'command': [],
        #                 },
        #                 'remove': {
        #                     'enum': [],
        #                     'command': [],
        #                 }
        #             }, # profiles will be after default (core / compatability)
        #         }
        #     }
        # }
        self.features = OrderedDict()
        if apiFile == "gl":
            with open("gl1enums.txt") as f:
                self.gl1Enums = f.read().split()

        self.extensions = OrderedDict()

        self.tag = 'registry'

        self.register_parser('registry/commands', Commands)
        self.register_parser('registry/feature', Feature)
        self.register_parser('registry/extensions', Extensions)

    def parse(self):

        tagPath = self.stack.path()
        tag, attrs, data = self.stack.peek()

        # No need for a full class to parse enums
        if 'registry/enums/enum' in tagPath:
            self.enums[attrs['name']] = attrs['value']


def parse_registry(xmlFile):
    apiName = xmlFile.rsplit(".")[0]
    reg = xml.parse_xml(Registry, xmlFile, apiName)
    return (reg.enums, reg.commands, reg.features, reg.extensions)


#  Higher level Tree-like View of parser classes.
#
#     - Registry
#       - Commands
#         - Command
#       - Feature
