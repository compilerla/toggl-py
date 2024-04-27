from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("toggl-py")
except PackageNotFoundError:
    # package is not installed
    __version__ = "1.0.0"
