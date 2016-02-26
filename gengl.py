from pglgen import regparse, codegen


def main():

    api = 'gl'
    code = codegen.gen_binding(*regparse.parse_registry('gl.xml'))

    with open('./opengl/{}.py'.format(api), 'w') as glFile:
        glFile.write(code)


if __name__ == '__main__':
    main()
