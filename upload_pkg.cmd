@ECHO OFF
IF NOT EXIST .pypirc (
    ECHO .pypirc is missing
    GOTO End
)
python setup.py register -r pypi
python setup.py sdist upload -r pypi

:END