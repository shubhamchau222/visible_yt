echo   [$(date)]: "Installation initiating"
conda create --prefix ./env python=3.8 -y
source activate ./env
echo   [$(date)]: "Requirements installing"
pip install -r requirements_dev.txt --user