import pytest

from ppqm import chembridge

# from context import ppqm, molecalc
#
# from molecalc.ppqm import chembridge


TEST_ERROR_SMILES = ["C[NH4+]"]


@pytest.mark.parametrize("smiles", TEST_ERROR_SMILES)
def test_capture_error(smiles):

    molobj, msg = chembridge.smiles_to_molobj(smiles, return_status=True)

    assert "ERROR" in msg
    assert molobj is None

    return
