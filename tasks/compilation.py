import luigi
import os
import sys

# Import parent module
# FIXME: There must be a better way of handling this
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from jupyter_notebook import JupyterNotebookTask

notebooks_path = os.path.join('..', 'code', 'data-preprocess')
data_path = os.path.join('..', 'data', 'stack-overflow')


class FilterPosts(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'posts-filter.ipynb')
    kernel_name = 'python3'
    timeout = 60

    questions_score = luigi.Parameter(default=10)
    answers_score = luigi.Parameter(default=5)
    input_file = luigi.Parameter(default=os.path.join(data_path, 'pandas-posts-dataset.csv'))

    #def input(self):
    #    luigi.LocalTarget(os.path.join(
    #        data_path, 'pandas-posts-dataset.csv')
    #    )

    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-filteredposts-dataset.csv')
        )



class ExtractCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'codeblock-extractor.ipynb')
    kernel_name = 'python3'
    timeout = 60

    def requires(self):
        return FilterPosts()

    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-code-dataset.csv')
        )


class PreProcessCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-preprocess.ipynb')
    kernel_name = 'python3'
    timeout = 60
    
    input_col = luigi.Parameter(default='Code')
    output_col = luigi.Parameter(default='PreprocessedCode')

    def requires(self):
        return ExtractCode()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-preprocessedcode-dataset.csv')
        )

      
"""

    ---------- NORMALIZATION METHODS -----------

"""
      
      
class NormalizeCode_PandasImport(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-normalizer-pandasimport.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='PreprocessedCode')
    output_col = luigi.Parameter(default='PandasImportCode')

    def requires(self):
        return PreProcessCode()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-normalized-pandasimport-dataset.csv')
        )
        

class NormalizeCode_NumpyImport(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-normalizer-numpyimport.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='PandasImportCode')
    output_col = luigi.Parameter(default='NumpyImportCode')

    def requires(self):
        return NormalizeCode_PandasImport()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-normalized-numpyimport-dataset.csv')
        )
        
        
class NormalizeCode_Dataframe(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-normalizer-dataframe.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='NumpyImportCode')
    output_col = luigi.Parameter(default='DataframeCode')

    def requires(self):
        return NormalizeCode_NumpyImport()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-normalized-dataframe-dataset.csv')
        )
        
        
        
"""

    ---------- PARSER METHODS -----------

"""
class ParseCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-parser.ipynb')
    kernel_name = 'python3'
    timeout = 60
    
    input_col = luigi.Parameter(default='DataframeCode')
    output_col = luigi.Parameter(default='DataframeParsed')

    def requires(self):
        return NormalizeCode_Dataframe()
    
    
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-parsedcode-dataset.csv')
        ) 
        
"""

    ---------- COMPILATION METHODS -----------

"""
class CompileCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-compiler.ipynb')
    kernel_name = 'python3'
    timeout = 60
    
    input_col = luigi.Parameter(default='DataframeCode')
    output_col = luigi.Parameter(default='DataframeCompiled')

    def requires(self):
        return NormalizeCode_NumpyImport()
    
    
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-compiledcode-dataset.csv')
        )







