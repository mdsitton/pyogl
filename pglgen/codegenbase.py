
from pglgen import regparse

class BaseApiGen(object):
    def __init__(self, apiName):

        self.code = {}
        self.initNames = {}

        self.apiMajorName = apiName

        info = regparse.parse_registry('{0}.xml'.format(self.apiMajorName))
        self.enums, self.commands, self.features, self.extensions = info

        self.apis = list(set(self.features.keys())|set(self.extensions.keys()))

    def gen_code(self):
        for api in self.apis:
            self.initNames[api] = []
            self.gen_header(api)
            self.gen_features(api, 'versions')
            self.gen_features(api, 'extensions')
            self.gen_init(api)
            self.write(api)

    def write(self, api):
        outputCode = self.code[api]
        with open(self.apiPath.format(api), 'w') as glFile:
            glFile.write(outputCode)

    def gen_header(self, api):
        pass

    def gen_features(self, api, genType):
        pass

    def gen_init(self, api):
        pass