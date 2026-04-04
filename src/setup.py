from setuptools import setup
import setup_translate

pkg = 'Extensions.EPGBackup'
setup(name='enigma2-plugin-extensions-epgbackup',
       version='3.0',
       description='Plugin to backup and restore EPG Data, including integration of EPGRefresh-plugin',
       package_dir={pkg: 'EPGBackup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'mphelp.xml', 'LICENSE', 'EPGBackup.sh', 'localehelp/mphelp.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
