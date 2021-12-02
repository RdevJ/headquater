find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

pytest $1