import luigi
import os
import sys

# Import parent module
# FIXME: There must be a better way of handling this
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from jupyter_notebook import JupyterNotebookTask

notebooks_path = os.path.join(module_path, 'code', 'data-preprocess')
data_path = os.path.join(module_path, 'data', 'stack-overflow')


class FilterPosts(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'posts-filter.ipynb')
    kernel_name = 'python3'
    timeout = 60

    questions_score = luigi.Parameter(default=0)
    answers_score = luigi.Parameter(default=0)
    input_file = luigi.Parameter(default=os.path.join(data_path, 'pandas-posts-dataset.csv'))

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

		
class FormatCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-formatter.ipynb')
    kernel_name = 'python3'
    timeout = 60

    input_col = luigi.Parameter(default='Code')
    output_col = luigi.Parameter(default='Code')
	
    def requires(self):
        return ExtractCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-formattedcode-dataset.csv')
        )
		

class PreProcessSpecialCharsCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-preprocess-specialchars.ipynb')
    kernel_name = 'python3'
    timeout = 120
    
    input_col = luigi.Parameter(default='Code')
    output_col = luigi.Parameter(default='PreprocessedCode')

    def requires(self):
        return FormatCode()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-preprocessedcode-dataset-part1.csv')
        )
		

class PreProcessTerminalLikeCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-preprocess-terminalcode.ipynb')
    kernel_name = 'python3'
    timeout = 120
    
    input_col = luigi.Parameter(default='PreprocessedCode')
    output_col = luigi.Parameter(default='PreprocessedCode2')

    def requires(self):
        return PreProcessSpecialCharsCode()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-preprocessedcode-dataset-part2.csv')
        )
		
		
class PreProcessParseableCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'code-preprocess-parseableiteractive.ipynb')
    kernel_name = 'python3'
    timeout = 120
    
    input_col = luigi.Parameter(default='PreprocessedCode2')
    output_col = luigi.Parameter(default='PreprocessedCode3')

    def requires(self):
        return PreProcessTerminalLikeCode()
        
    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-preprocessedcode-dataset-part3.csv')
        )
		