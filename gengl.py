from pglgen import regparse, codegen


def main():

    apis = ['gl', 'wgl', 'glx', 'egl']
    for api in apis:
        code = codegen.gen_binding(*regparse.parse_registry('{0}.xml'.format(api)))

        with open('./opengl/{}.py'.format(api), 'w') as glFile:
            glFile.write(code)


if __name__ == '__main__':
    main()
