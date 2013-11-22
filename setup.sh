sudo python distribute_setup.py
sudo easy_install pip
sudo pip install virtualenv
virtualenv --distribute venv
source venv/bin/activate
pip install Flask gunicorn