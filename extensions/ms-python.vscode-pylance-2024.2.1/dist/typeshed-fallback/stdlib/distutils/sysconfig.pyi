import sys
from collections.abc import Mapping
from distutils.ccompiler import CCompiler

PREFIX: str
EXEC_PREFIX: str
BASE_PREFIX: str
BASE_EXEC_PREFIX: str
project_base: str
python_build: bool

def expand_makefile_vars(s: str, vars: Mapping[str, str]) -> str: ...
def get_config_var(name: str) -> int | str | None: ...
def get_config_vars(*args: str) -> Mapping[str, int | str]: ...
def get_config_h_filename() -> str: ...
def get_makefile_filename() -> str: ...
def get_python_inc(plat_specific: bool = ..., prefix: str | None = None) -> str: ...
def get_python_lib(plat_specific: bool = ..., standard_lib: bool = ..., prefix: str | None = None) -> str: ...
def customize_compiler(compiler: CCompiler) -> None: ...

if sys.version_info < (3, 10):
    def get_python_version() -> str: ...
