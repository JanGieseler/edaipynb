# notebook specific functions

from IPython.display import display_html, Javascript
# from IPython import display

import json
import os.path
import re
import ipykernel
import requests
import time
from pathlib import Path

from requests.compat import urljoin

try:  # Python 3 (see Edit2 below for why this may not work in Python 2)
    from notebook.notebookapp import list_running_servers
except ImportError:  # Python 2
    import warnings
    from IPython.utils.shimmodule import ShimWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ShimWarning)
        from IPython.html.notebookapp import list_running_servers


def get_notebook_name():
    """
    Return the full path of the jupyter notebook.
    """
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    for ss in servers:
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                relative_path = nn['notebook']['path']
                return os.path.join(ss['notebook_dir'], relative_path)


def save_notebook():
    return display(Javascript("IPython.notebook.save_notebook()"),
                   include=['application/javascript'])

def output_HTML(read_file, output_file):
    from nbconvert import HTMLExporter
    import codecs
    import nbformat
    exporter = HTMLExporter()
    # read_file is '.ipynb', output_file is '.html'
    output_notebook = nbformat.read(read_file, as_version=4)
    output, resources = exporter.from_notebook_node(output_notebook)
    codecs.open(output_file, 'w', encoding='utf-8').write(output)


def save_notebook_as_html(target_folder=None):
    """


    :param target_folder: Path object that defines the target folder for the .html file if none same folder as .ipynb
    :return:
    """

    save_notebook()
    time.sleep(3)  # wait a little to make sure file is saved
    current_file = get_notebook_name()
    if target_folder is None:
        output_file = current_file.replace('.ipynb', '.html')
    else:
        output_file = target_folder/Path(current_file).name.replace('.ipynb', '.html')

    output_HTML(current_file, output_file)
    print(str(output_file) + ' saved')

def restart_kernel() :
    display_html("<script>Jupyter.notebook.kernel.restart()</script>",raw=True)








def save_fig(fig, filename, **kwargs):
    """
    wrapper for save fig, that checks and creates the required folder

    """

    folder_path = filename.parent

    paths = []
    while not folder_path.exists():
        paths.append(folder_path)
        folder_path = folder_path.parent
    for path in paths[::-1]:
        print('make directory:', path)
        path.mkdir()

    fig.savefig(filename, **kwargs)
