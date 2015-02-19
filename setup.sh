python virtualenv.py helloflask

helloflask/bin/pip install -r requirements.txt

cp ./rest-server-v2.py  ./helloflask/rest-server-v2.py

cd helloflask
source bin/activate

python rest-server-v2.py