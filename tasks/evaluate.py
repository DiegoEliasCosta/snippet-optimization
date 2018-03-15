import luigi
import os
import sys
from preprocess-code import PreProcessParseableCode

# Import parent module
# FIXME: There must be a better way of handling this
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from jupyter_notebook import JupyterNotebookTask

notebooks_path = os.path.join(module_path, 'code', 'data-preprocess')
data_path = os.path.join(module_path, 'data', 'stack-overflow')
