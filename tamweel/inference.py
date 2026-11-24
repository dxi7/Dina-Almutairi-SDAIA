from importlib import import_module
from pathlib import Path
import sys


_PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _script_directory():
    candidates = (
        _PROJECT_ROOT / "scripts",
        _PROJECT_ROOT / "submission" / "project_bundle" / "scripts",
    )
    for directory in candidates:
        if (directory / "day5_final.py").is_file():
            location = str(directory)
            if location not in sys.path:
                sys.path.insert(0, location)
            return directory
    raise FileNotFoundError("The project scripts directory containing day5_final.py was not found.")


def _default_artifact_directory():
    candidates = (
        _PROJECT_ROOT / "artifacts" / "final_model",
        _PROJECT_ROOT / "submission" / "project_bundle" / "artifacts" / "final_model",
    )
    for directory in candidates:
        if (directory / "model.json").is_file() and (directory / "model_manifest.json").is_file():
            return directory
    raise FileNotFoundError("The final model artifacts were not found.")


def predict(frame, artifact_dir=None):
    _script_directory()
    predict_final = import_module("day5_final").predict_final
    model_directory = Path(artifact_dir) if artifact_dir is not None else _default_artifact_directory()
    return predict_final(frame, model_directory)
