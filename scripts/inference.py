"""Portable inference entry point for the repository-root project layout."""
from pathlib import Path
import sys

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from tamweel.inference import predict as _predict


def predict(frame, artifact_dir=None):
    """Return application IDs and model probabilities using the packaged final model."""
    return _predict(frame, artifact_dir)
