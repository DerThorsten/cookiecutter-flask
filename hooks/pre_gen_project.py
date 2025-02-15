import logging
import re
import sys

# Provide ability to import from the `hooks` directory
sys.path.append("..")

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def check_python_version():
    python_major_version = sys.version_info[0]
    python_minor_version = sys.version_info[1]
    # Must remain compatible with Python 2 to provide useful error message.
    warning = (
        "\nWARNING: You are running cookiecutter using "
        "Python {}.{}, but a version >= Python 3.6+ is required.\n"
        "Either install a more recent version of Python, or use the Docker instructions.\n"
    ).format(python_major_version, python_minor_version)
    if (python_major_version == 2) or (
        python_major_version == 3 and python_minor_version < 6
    ):
        LOGGER.warning(warning)
        sys.exit(1)


def validate_python_module_name():
    module_name = "{{ cookiecutter.app_name }}"
    if not re.match(MODULE_REGEX, module_name):
        log_module_name_warning(module_name, LOGGER)
        sys.exit(1)


if __name__ == "__main__":
    check_python_version()

    # Import after validating Python version to prevent confusing SyntaxError
    # for users with incompatible Python versions.
    from hooks.utils import log_module_name_warning

    validate_python_module_name()
