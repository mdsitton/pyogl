from setuptools import Command, setup

class Generate(Command):
    description = 'Generate opengl binding'
    user_options = []

    def run(self):
        import generate
        generate.main()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(name='pyOGL',
      version='0.1',
      description='Python OpenGL ctypes binding.',
      author='Matthew Sitton',
      author_email='matthewsitton@gmail.com',
      url='https://github.com/mdsitton/pyogl',
      packages=['opengl'],
      cmdclass={'generate': Generate},
     )
