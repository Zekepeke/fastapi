# fastapi
```bash
# from server directory
python3.11 -m venv facial-project
# macOS/Linux
source facial-project/bin/activate
# Windows (PowerShell)
# facial-project\Scripts\Activate.ps1

python -m pip install --upgrade pip

# App dependencies
pip install -r requirements.txt

# run (pick one)
export FLASK_APP=app.py FLASK_ENV=development && flask run --port 8000
# or
python app.py
```
