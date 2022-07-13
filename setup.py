from pathlib import Path

from setuptools import (find_packages,
                        setup)

import {{project}}

project_base_url = 'https://github.com/{{github_login}}/{{project}}/'


def read_file(path_string: str) -> str:
    return Path(path_string).read_text(encoding='utf-8')


setup(name={{project}}.__name__,
      packages=find_packages(exclude=('tests', 'tests.*')),
      version={{project}}.__version__,
      description={{project}}.__doc__,
      long_description=read_file('README.md'),
      long_description_content_type='text/markdown',
      author='{{full_name}}',
      author_email='{{email}}',
      classifiers=[
          '{{trove_license_classifier}}',
{% for minor in range(min_version_of['python'].split(".")[1]|int, (max_version_of['python'].split(".")[1])|int + 1) %}
          'Programming Language :: Python :: 3.{{minor}}',
{% endfor %}
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      license='{{spdx_license_name}}',
      url=project_base_url,
      download_url=project_base_url + 'archive/master.zip',
      python_requires='>={{min_version_of['python']}}',
      install_requires=read_file('requirements.txt'))
