# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tealabs使用手册'
copyright = '@2022-2023, zhangeamon'
author = 'zhangeamon'

# The full version, including alpha/beta/rc tags

release = '0.0.1'

# -- General configuration ---------------------------------------------------


# Add any Sphinx extension module names here, as strings. They can be

# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom

# ones.

extensions = ['recommonmark',

  'sphinx_markdown_tables',

]

# Add any paths that contain templates here, relative to this directory.

templates_path = ['_templates']


html_logo = './_static/logo.jpg'

# The language for content autogenerated by Sphinx. Refer to documentation

# for a list of supported languages.

#

# This is also used if you do content translation via gettext catalogs.

# Usually you set "language" from the command line for these cases.

language = 'zh_CN'


# List of patterns, relative to source directory, that match files and

# directories to ignore when looking for source files.

# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = []


#supported markdown

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']


master_doc = 'index'


# -- Options for HTML output -------------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for

# a list of builtin themes.

#

#html_theme = 'alabaster'

import recommonmark

from recommonmark.transform import AutoStructify

def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)


import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

