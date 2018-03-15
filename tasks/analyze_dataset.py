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

analyze_notebooks_path = os.path.join(module_path, 'code', 'analysis')

input_path = os.path.join(module_path, 'data', 'stack-overflow')
output_path = os.path.join(module_path, 'data', 'dataset')


class AnalyzeDataset(JupyterNotebookTask):
    notebook_path = os.path.join(analyze_notebooks_path, 'dataset-analysis.ipynb')
    kernel_name = 'python3'
    timeout = 60

    dataset = luigi.Parameter(default=os.path.join(input_path, 'Dataset - Pandas.csv'))

    histogram = luigi.Parameter(default=os.path.join(output_path, 'histogram.pdf'))    
    dist = luigi.Parameter(default=os.path.join(output_path, 'distribution.pdf'))    
    summary = luigi.Parameter(default=os.path.join(output_path, 'summary.csv'))
    violin = luigi.Parameter(default=os.path.join(output_path, 'violin.pdf'))
    
    def requires(self):
        return PreProcessParseableCode()

    def output(self):
        return luigi.LocalTarget(os.path.join(output_path, 'finished-token.txt'))

	