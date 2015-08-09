CMS
***

Django application for a simple CMS site.  For documentation, see
https://www.pkimber.net/open/app-cms.html

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-cms
  source venv-cms/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  ./init_dev.sh

Release
=======

https://www.pkimber.net/open/
