import din6892
import din6885


def test_lamellen():
    assert abs(din6892.C.Calculator(din6885.PassfederHoheForm(30, 43, din6885.Passfeder.Form.A), 1.75, 535.93, 500, 2).S - 1.1335435597932566) < 0.00001

def test_ritzel():
    assert abs(din6892.C.Calculator(din6885.PassfederHoheForm(50, 54, din6885.Passfeder.Form.A), 1.75, 535.93, 500, 1).S - 1.6793237922863062) < 0.00001

def test_rad():
    assert abs(din6892.C.Calculator(din6885.PassfederHoheForm(70, 48.3, din6885.Passfeder.Form.B), 1.75, 2933.511, 500, 2).S - 1.000243394348956) < 0.00001

def test_drehstarr():
    assert abs(din6892.C.Calculator(din6885.PassfederHoheForm(55, 86, din6885.Passfeder.Form.A), 1.75, 2933.511, 500, 2).S - 1.012438678430045) < 0.00001