
import luigi
import os
import sys

# Import parent module
# FIXME: There must be a better way of handling this
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from jupyter_notebook import JupyterNotebookTask

notebooks_path = os.path.join('..', 'data-exploration')
data_path = os.path.join('..', 'data')

class FilterPosts(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'posts-filter.ipynb')
    kernel_name = 'python3'
    timeout = 60

    questions_score = luigi.Parameter(default=10)
    answers_score = luigi.Parameter(default=5)

    def input(self):
        luigi.LocalTarget(os.path.join(
            data_path, 'pandas-posts-dataset.csv')
        )

    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-filteredposts-dataset.csv')
        )


class ExtractCode(JupyterNotebookTask):
    notebook_path = os.path.join(notebooks_path, 'posts-filter.ipynb')
    kernel_name = 'python3'
    timeout = 60

    def requires(self):
        return FilterPosts()

    def output(self):
        return luigi.LocalTarget(os.path.join(
            data_path, 'pandas-code-dataset.csv')
        )



