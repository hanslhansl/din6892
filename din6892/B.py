"""Vereinfachte Berechnung von Passfederverbindungen"""

from typing import Literal, Optional
import din6885

def l_tr(l : float, b : float, form : din6885.Passfeder.Form):
    """Glg. 6-8"""
    match form:
        # rundstirnig
        case din6885.Passfeder.Form.A | din6885.Passfeder.Form.C | din6885.Passfeder.Form.E1 | din6885.Passfeder.Form.E2:
            return l - b
        # geradstirnig
        case din6885.Passfeder.Form.B | din6885.Passfeder.Form.D | din6885.Passfeder.Form.F1 | din6885.Passfeder.Form.F2 | din6885.Passfeder.Form.G | din6885.Passfeder.Form.H | din6885.Passfeder.Form.J:
            return l
        # rund-geradstirnig
        case din6885.Passfeder.Form.AB:
            return l - b / 2