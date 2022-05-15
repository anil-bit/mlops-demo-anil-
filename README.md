crete env

'''bash
conda create -n wineq python=3.7 -y
'''

activate env

'''bash
conda activate wineq
'''
create req file

'''bash
touch requirements.txt
'''

install lib

'''bash
pip install -r requirements.txt
'''


git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit" 

git add . && git commit -m "update readme.md"

git remote add origin https://github.com/anil-bit/mlops-demo-anil-.git

git branch -M main

git push origin main

tox command-
'''bash
tox
'''
tox rebuild-
'''bash
tox -r
'''
pytest command
'''bash
pytest -v
'''

setup command
'''bash
pip install -e .
'''

build your own package commands-
python setup.py sdist bdist wheel

 




