# cosomis-benin

Run the App
`cd cosomis-benin/cosomis`

## Setup

Activate Python environment (use python 3)
`python3 -m venv venv`

Activate Python Environment
`source venv/bin/activate`

Install application

- `pip install -r requirements.txt`
- `pip install -r requirements.dev.txt`

Start Application

- Create a local environment file (customize according to your needs) from the provided template: `cp cosomis/example.env cosomis/.env`. For example fill database credentials
- Do the same for `local_settings.py`: `cp cosomis/local_settings_template.py cosomis/local_settings.py`
- `python3 manage.py migrate`
- `python3 manage.py runserver`

## Manually loading .emv file

```bash
export $(cat .env | xargs)
```
