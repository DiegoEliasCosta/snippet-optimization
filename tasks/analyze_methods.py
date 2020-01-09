import luigi
import os
import sys

from evaluate import *

# Import parent module
# FIXME: There must be a better way of handling this
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from jupyter_notebook import JupyterNotebookTask

method_notebook_path = os.path.join(module_path, 'code', 'method')
analyze_notebook_path = os.path.join(module_path, 'code', 'analysis')

data_path = os.path.join(module_path, 'data', 'stack-overflow')
results_path = os.path.join(module_path, 'data', 'results')
analysis_path = os.path.join(module_path, 'data', 'analysis')

api_doc_file = os.path.join(module_path, 'code', 'data-import', 'build_api_doc_base', 'api_doc.csv') 

# ------------------------------------------------
#					EVALUATE ALL
# ------------------------------------------------
class AnalyzeAllBlock(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'analyze-all.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    
    def requires(self):
        return { 
            'baseline': EvaluateBaseline(),
            'h1': EvaluateH1(),
            'h2': EvaluateH2(),
            'h1h2': EvaluateH1H2(),
            'm1': EvaluateM1(),
            'm1Doc2Vec': EvaluateM1Doc2Vec()
            }
        

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'all-methods-block'))

        

class AnalyzeAllLine(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'analyze-all.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    
    def requires(self):
        return { 
            'baseline': EvaluateBaseline_Line(),
            'h1': EvaluateH1_Line(),
            'h2': EvaluateH2_Line(),
            'h1h2': EvaluateH1H2_Line(),
            'm1': EvaluateM1_Line(),
            'm1Doc2Vec': EvaluateM1Doc2Vec_Line()
            }
        

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'all-methods-line'))


