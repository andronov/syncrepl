#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 et
#
# Syncrepl Client documentation build configuration file, created by
# sphinx-quickstart on Thu May 25 21:02:02 2017.

# Refer to the AUTHORS file for copyright statements.
#
# This file contains only factual information.
# Therefore, this file is likely not copyrightable.
# As such, this file is in the public domain.
# For locations where public domain does not exist, this file is licensed
# under the Creative Commons CC0 Public Domain Dedication.

#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Syncrepl Client'
copyright = 'the entities listed in the AUTHORS source file.  Licensed (code and documentation) as per the LICENSE source file'
author = 'A. Karl Kornel'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.75'
# The full version, including alpha/beta/rc tags.
release = '0.75'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Set the default domain to "py" (Python), which is the default, but
# let's make that clear!
default_domain = 'py'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SyncreplClientdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SyncreplClient.tex', 'Syncrepl Client Documentation',
     'A. Karl Kornel', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'syncreplclient', 'Syncrepl Client Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SyncreplClient', 'Syncrepl Client Documentation',
     author, 'SyncreplClient', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for viewcode -------------------------------------------------

# Enable viewcode
viewcode_import = True

# -- Options for Intersphinx ----------------------------------------------

# Configure mappings to pull from Python 3.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'ldap': ('https://www.python-ldap.org/doc/html', None),
    'ldap.ldapobject': ('https://www.python-ldap.org/doc/html', None),
    'ldapurl': ('https://www.python-ldap.org/doc/html', None),
}

# -- Options for autodoc --------------------------------------------------

autodoc_default_flags = [ 'members' ]
autoclass_content = 'class'
autodoc_member_order = 'bysource'

# We can't use Mock and MagicMock (as per Read the Docs' FAQ) because that 
# generates hideous metaclass exceptions when the metaclass-ldaen code is 
# imported.

# The code below seems to work, by generating empty classes, which at least 
# allow things to load.  This only works because importing these modules does 
# not actually cause any code to execute.

# NOTE that we can't use autodoc_mock_imports, because it can mess with the
# display of base classes (when the 'show-inheritance' flag is set).

class FakeObject(object):
    pass

class FakeSimpleLDAPObject(object):
    class SimpleLDAPObject(object):
        pass

class FakeSyncreplConsumer(object):
    class SyncreplConsumer(object):
        pass

MOCKS = {
    'ldap': FakeObject(),
    'ldap.ldapobject': FakeSimpleLDAPObject(),
    'ldap.syncrepl': FakeSyncreplConsumer(),
    'ldapurl': FakeObject()
}
sys.modules.update((mod_name, mod_val) for mod_name, mod_val in MOCKS.items())
