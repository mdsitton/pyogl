from pglgen import codegen

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
    codegen.gen_bindings(apis)

if __name__ == '__main__':
    main()
