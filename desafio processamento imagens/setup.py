from setuptools import setup, find_packages

setup(
    name='project_name',  # Nome do seu pacote
    version='0.1',  # Versão do pacote
    packages=find_packages(),  # Detecta automaticamente os pacotes
    install_requires=[],  # Adicione aqui suas dependências, caso existam
    description="Exemplo de pacote Python para testar conhecimentos.",
    author="Seu Nome",
    author_email="seuemail@example.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
