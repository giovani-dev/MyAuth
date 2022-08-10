import os
import setuptools


app_enviroment = os.getenv('APP_ENVIROMENT')
requirements = [
    'fastapi[all]',
    'uvicorn[standard]',
    'peewee==3.15.1',
    'PyMySQL==1.0.2',
    'passlib==1.7.4'
]

if app_enviroment != 'dev' or \
    app_enviroment != 'homolog' or \
        app_enviroment == 'stage':
        requirements.append('pytest==7.1.2')


setuptools.setup(
    name='MyAuth-API',
    version='0.0.1',
    author='Giovani Liskoski Zanini',
    author_email='giovanilzanini@hotmail.com',
    description='Gerenciar a autenticação dos usuarios de sua plataforma.',
    packages=setuptools.find_packages(),
    python_requires=">=3.10.*",
    install_requires=requirements
)
