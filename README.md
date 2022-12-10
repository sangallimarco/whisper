pip install -r requirements.txt
brew install ffmpeg


# VENV
python3 -m pip install --user virtualenv   
python3 -m venv env
source env/bin/activate 

pip3 freeze > requirements.txt
