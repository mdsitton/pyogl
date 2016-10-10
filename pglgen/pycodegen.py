from collections import OrderedDict

from opengl import gltypes

from pglgen import regparse

codeHeader = '''\'\'\'
OpenGL binding For python
WARNING - This is generated code, do not modify directly.
\'\'\'
import ctypes as ct

from opengl.bindutils import gl_func
from opengl import gltypes as t

def set_func(name, returnType, paramTypes):
    \'\'\'gl_func wrapper that inserts function in globals.\'\'\'
    globals()[name] = gl_func(name, returnType, paramTypes)

def set_enum(name, value):
    globals()[name] = value

noParms = ()
'''

enum = '    set_enum("{0}", {1})\n'

funcTemplate = '''
def {0}():
{1}
'''
initTemplate = '''
def init():
{0}
'''

func = '    set_func(\'{0}\', {1}, ({2}))\n'
commentedFunc = '    # set_func(\'{0}\', {1}, ({2}))\n'

pointer = 'ct.POINTER({0})'


# Get list of supported types automatically
supportedTypes = [item for item in dir(gltypes) if item[0] != '_' and item != 'ct']

typeMap = {
    'int': 'INT',
    'char': 'CHAR',
    'float': 'FLOAT',
    'unsigned int': 'UINT',
    'unsigned long': 'ULONG'
}

def generate_type_str(typeData):

    baseTypeStr = None

    typeStr = ''

    for typeItem in typeData:
        dataType = typeItem['type']
        isConst = typeItem['const']

        if dataType == 'pointer':
            typeStr = pointer.format(typeStr)

        else:

            try:
                baseTypeStr = typeMap[dataType]
            except KeyError:
                baseTypeStr = dataType

            typeStr = 't.'+baseTypeStr

    return typeStr, baseTypeStr


def gen_func_code(enums, commands):
    functionCode = []
    nonCommented = False

    for name, typeInfo in commands.items():
        rtnType = typeInfo['return']
        params = typeInfo['parms']

        commentFunction = False

        rtnStr, baseRtnType = generate_type_str(rtnType)

        # Mark the function  to be commented out out if we do
        # not currently support any of the datatypes needed
        if baseRtnType not in supportedTypes:
            commentFunction = True

        # generate param list string
        parmItems = []
        for parName, parType in params:
            parStr, baseType = generate_type_str(parType)

            # Mark the function to be commented out out if we do
            # not currently support any of the datatypes needed
            if baseType not in supportedTypes:
                commentFunction = True

            parmItems.append(parStr)

        # Add a comma to the end of a single argument because tuples..
        if len(parmItems) == 1:
            parmStr = '{0},'.format(parmItems[0])
        else:
            parmStr = ', '.join(parmItems)

        # Comment out function if marked.
        if commentFunction:
            funcCode = commentedFunc.format(name, rtnStr, parmStr)
        else:
            nonCommented = True
            funcCode = func.format(name, rtnStr, parmStr)

        functionCode.append(funcCode)

    for name, value in enums.items():
        if '(' in value or ')' in value:
            functionCode.append('# {0}'.format(enum.format(name, value)))
        else:
            nonCommented = True
            functionCode.append(enum.format(name, value))

    if not nonCommented:
        functionCode.append('    pass')

    return ''.join(functionCode)

#def gen_feature_function()

def gen_bindings(apis):
    for api in apis:
        apiClass = ApiGen(api)
        apiClass.gen_code()

class ApiGen(object):
    def __init__(self, apiName):

        self.code = {}
        self.initNames = {}

        self.apiMajorName = apiName

        info = regparse.parse_registry('{0}.xml'.format(self.apiMajorName))
        self.enums, self.commands, self.features, self.extensions = info

        self.apis = list(set(self.features.keys())|set(self.extensions.keys()))

    def gen_code(self):
        for api in self.apis:
            self.code[api] = codeHeader
            self.initNames[api] = []
            self.gen_features(api, 'versions')
            self.gen_features(api, 'extensions')
            self.gen_init(api)
            self.write(api)

    def write(self, api):
        outputCode = self.code[api]
        with open('./opengl/{}.py'.format(api), 'w') as glFile:
            glFile.write(outputCode)

    def gen_features(self, api, genType):
        '''Generate code for opengl feature levels'''

        initNames = []
        code = []
        try:
            if genType == 'versions':
                apiNames = self.features[api]
            elif genType == 'extensions':
                apiNames = self.extensions[api]
        except KeyError:
            # this api doesnt contain any features
            return

        for name, features in apiNames.items():

            if genType == 'versions':
                version = features['info']['version']
                funComment = '\n#### {} VERSION {} ####'.format(api.upper(), version)
            elif genType == 'extensions':
                funComment = '\n#### {} ####'.format(name.upper())

            code.append(funComment)

            featureCmds = OrderedDict()
            featureEnums = OrderedDict()

            for profname, featureData in features.items():
                if profname == 'info':
                    continue

                if genType == 'versions':
                    featureData = featureData['require']
                elif genType == 'extensions':
                    featureData = featureData

                for c in featureData['command']:
                    featureCmds[c] = self.commands[c]
                for e in featureData['enum']:
                    featureEnums[e] = self.enums[e]
            initName = 'init_' + name.lower()
            initNames.append(initName)

            funcCode = gen_func_code(featureEnums, featureCmds)

            code.append(funcTemplate.format(initName, funcCode))

        self.initNames[api].extend(initNames)
        self.code[api] += ''.join(code)

    def gen_init(self, api):
        '''Generate code for opengl extensions'''
        initCode = []

        for initName in self.initNames[api]:
            initCode.append('    {}()\n'.format(initName))

        self.code[api] += initTemplate.format(''.join(initCode))
