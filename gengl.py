from pglgen import regparse, codegen


def main():

    api = 'gl'
    apis = codegen.gen_binding(*regparse.parse_registry('gl.xml'))

    code = apis[api]

    with open('./opengl/{}.py'.format(api), 'w') as glFile:
        glFile.write(code)


if __name__ == '__main__':
    main()
