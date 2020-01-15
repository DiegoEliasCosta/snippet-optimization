import luigi
import os
import sys

from preprocess_code import PreProcessTitleTextRake

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
        return PreProcessTitleTextRake()

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
        return PreProcessTitleTextRake()

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
        return PreProcessTitleTextRake()

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
        return PreProcessTitleTextRake()

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
#  					M1TFIDF
# ------------------------------------------------
class RunM1TFIDF(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1TFIDF-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1tfidf'))


class EvaluateM1TFIDF(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1TFIDF()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1tfidf'))


class EvaluateM1TFIDF_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1TFIDF()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1tfidf-line'))


# ------------------------------------------------
#  					M1TFIDFH2
# ------------------------------------------------
class RunM1TFIDFH2(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1TFIDFH2-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1tfidfh2'))


class EvaluateM1TFIDFH2(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1TFIDFH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1tfidfh2'))


class EvaluateM1TFIDFH2_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1TFIDFH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1tfidfh2-line'))


# ------------------------------------------------
#  					M1Doc2VecTitle
# ------------------------------------------------
class RunM1Doc2VecTitle(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1D2VTitle-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1-d2vtitle'))


class EvaluateM1Doc2VecTitle(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1Doc2VecTitle()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitle'))


class EvaluateM1Doc2VecTitle_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1Doc2VecTitle()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitle-line'))


# ------------------------------------------------
#  					M1Doc2VecTitleH2
# ------------------------------------------------
class RunM1Doc2VecTitleH2(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1D2VTitleH2-Question_Text_Doc2Vec_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1-d2vtitleh2'))


class EvaluateM1Doc2VecTitleH2(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1Doc2VecTitleH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitleh2'))


class EvaluateM1Doc2VecTitleH2_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1Doc2VecTitleH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitleh2-line'))


# ------------------------------------------------
#  					M1Doc2VecTitleBody
# ------------------------------------------------
class RunM1Doc2VecTitleBody(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1D2VTitleBody-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1-d2vtitlebody'))


class EvaluateM1Doc2VecTitleBody(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1Doc2VecTitleBody()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitlebody'))


class EvaluateM1Doc2VecTitleBody_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1Doc2VecTitleBody()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitlebody-line'))


# ------------------------------------------------
#  					M1Doc2VecTitleBodyH2
# ------------------------------------------------
class RunM1Doc2VecTitleBodyH2(JupyterNotebookTask):
    notebook_path = os.path.join(method_notebook_path, 'm1', 'M1D2VTitleBodyH2-Question_Text_Api_Desc.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))

    code_snippet_col = luigi.Parameter(default='PreprocessedCode3')
    id_col = luigi.Parameter(default='Id')     
    api_doc_file = luigi.Parameter(default=api_doc_file)   
    cosine_sim_th = luigi.Parameter(default=0.0)
     
    def requires(self):
        return PreProcessTitleTextRake()

    def output(self):
        return luigi.LocalTarget(os.path.join(data_path, 'pandas-solutioncode-m1-d2vtitlebodyh2'))


class EvaluateM1Doc2VecTitleH2(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)

    def requires(self):
        return RunM1Doc2VecTitleBodyH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitlebodyh2'))


class EvaluateM1Doc2VecTitleH2_Line(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebook_path, 'evaluate-line-granularity.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(data_path, 'Dataset - Pandas.csv'))
    debug = luigi.Parameter(default=DEBUG)


    def requires(self):
        return RunM1Doc2VecTitleBodyH2()

    def output(self):
        return luigi.LocalTarget(os.path.join(results_path, 'results-m1-d2vtitlebodyh2-line'))
