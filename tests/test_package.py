import importlib


def test_package_and_starter_areas_are_importable():
    package = importlib.import_module("data_science_lib")

    assert package.__version__ == "0.1.0"
    for area in ("datasets", "preprocessing", "statistics", "visualization"):
        importlib.import_module(f"data_science_lib.{area}")
