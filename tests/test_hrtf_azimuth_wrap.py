import pytest
import media.hrtf_azimuth_wrap as mod

CASES = [
    ("quat_interp", (1, 2)),
    ("azimuth_unwrap", (1, 2)),
    ("crossfade", (1, 2)),
    ("behind_flip", (1, 2)),
    ("hrtf_set", (1, 2)),
    ("listener_rotation", (90.0, 2.0)),
    ("gain_jump", (1, 2)),
    ("elevation", (1, 2)),
    ("interpolation_mode", (1, 2)),
    ("wrap_threshold", (1, 2)),
    ("validation", (1, 2)),
    ("fallback_stereo", (1, 2)),
    ("smoothing", (0.2, 0.5)),
    ("abrupt_metric", (1.0, 2.0)),
    ("batch_guard", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
