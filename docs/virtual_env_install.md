## Installation in a virtual environment Installation on Linux. 


```bash
git clone https://github.com/VulturARG/gila_software_challenge.git
cd gila_software_challenge
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python3 main.py
```

## Automatic tests 
### Run test
```bash
python3 -m unittest
```

### Run coverage
```bash
coverage run -m unittest
```

### Generate coverage HTML report 
```bash
coverage html
```