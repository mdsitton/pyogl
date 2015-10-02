from pglgen import regparse, codegen


def main():

    enums, commands = regparse.parse_registry('gl.xml')

    code = codegen.gen_binding(enums, commands)

    with open('./opengl/gl.py', 'w') as glFile:
        glFile.write(code)


if __name__ == '__main__':
    main()
