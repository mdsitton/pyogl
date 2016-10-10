from pglgen import pycodegen

# This is somewhat of a hack
# It injects a variable into the builtins so that its simple
# to check for code genetation in the types system.
try:
    import __builtin__ as builtins
except ImportError:
    import builtins
builtins.genGL = True

def main():
    apis = ['gl', 'wgl', 'glx', 'egl']

    for api in apis:
        apiClass = pycodegen.PyApiGen(api)
        apiClass.gen_code()

if __name__ == '__main__':
    main()
