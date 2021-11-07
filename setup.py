from setuptools import setup
import mp_docu

setup(
    name='mp_docu',
    version=mp_docu.__version__,
    description='Moon Package for Document(conversion, translation, publishing, ...)',
    url='https://github.com/hopelife/mp_docu',
    author='Moon Jung Sam',
    author_email='monblue@snu.ac.kr',
    license='MIT',
    packages=['mp_docu'],
    # entry_points={'console_scripts': ['mp_docu = mp_docu.__main__:main']},
    keywords='scraper',
    # python_requires='>=3.8',  # Python 3.8.6-32 bit
    # install_requires=[ # 패키지 사용을 위해 필요한 추가 설치 패키지
    #     'selenium',
    # ],
    # zip_safe=False
)
