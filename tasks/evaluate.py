import luigi
import os
import sys

from preprocess_code import PreProcessParseableCode

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

api_doc_file = os.path.join(module_path, 'data-import', 'build_api_doc_base', 'api_doc.csv') 


# ------------------------------------------------
#  						H1  
# ------------------------------------------------

class RunH1(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'h1', 'H1-method_name_matching.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-h1'))

		
		
class EvaluateH1(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))


    def requires(self):
        return RunH1()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1'))
		
		
# ------------------------------------------------
#  						 H2
# ------------------------------------------------
		
class RunH2(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'h2', 'H2-Non_Contructors.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-h2'))

		
		
class EvaluateH2(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))


    def requires(self):
        return RunH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h2'))
		
		
# ------------------------------------------------
#  					H1 and H2
# ------------------------------------------------
class RunH1H2(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'h2', 'H1H2-Non_Contructors.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-h1h2'))

		
		
class EvaluateH1H2(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))


    def requires(self):
        return RunH1H2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1h2'))