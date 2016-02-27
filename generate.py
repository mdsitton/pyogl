from pglgen import codegen


def main():
    apis = ['gl', 'wgl', 'glx', 'egl']
    codegen.gen_bindings(apis)

if __name__ == '__main__':
    main()
