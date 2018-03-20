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
analysis_path = os.path.join(module_path, 'data', 'analysis')

api_doc_file = os.path.join(module_path, 'code', 'data-import', 'build_api_doc_base', 'api_doc.csv') 

DEBUG = 1

# ------------------------------------------------
#  						BASELINE  
# ------------------------------------------------

class RunBaseline(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'baseline', 'baseline.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='PreprocessedCode3')    
    
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-baseline'))

		
		
class EvaluateBaseline(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunBaseline()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-baseline'))
		

class EvaluateBaseline_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunBaseline()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-baseline-line'))

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
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH1()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1'))
        
        
        
class EvaluateH1_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH1()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1-line'))
		
		
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
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h2'))
		
        
class EvaluateH2_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h2-line'))
		
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
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH1H2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1h2'))
        
        
        
class EvaluateH1H2_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunH1H2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-h1h2-line'))


# ------------------------------------------------
#  					M1
# ------------------------------------------------
class RunM1(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.1)
     
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1'))

		
        
        
		
class EvaluateM1(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1'))

        
        
class EvaluateM1_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-line'))