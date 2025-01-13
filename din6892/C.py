"""Überschlägige Dimensionierung von Passfederverbindungen"""

from typing import Literal, Optional
from . import B
import din6885



def p_zul(R_emin : float):
    """Glg. 33"""
    return 0.9 * R_emin

def phi(i : int):
    """Traganteil, Abschnitt 7.3b"""
    if i == 1:
        return 1.
    elif i == 2:
        return 0.75
    else:
        raise ValueError("i must be 1 or 2")

def M_teq(K_A : float, M_tnenn : float):
    """Glg. 34"""
    return K_A * M_tnenn

def M_tzul(p_zul : float, h : float, t_1 : float, l_tr : float, d : float, i : int, phi):
    """Glg. 35"""

    return p_zul * (h - t_1) * l_tr * d / 2 * i * phi / 1000

class Calculator:
    def __init__(self,
                 passfeder : din6885.Passfeder,
                 K_A : float,
                 M_tnenn : float,
                 R_emin : float,

                 i : Optional[int] = None,

                 _print = print,
                 _assert = False):
        
        self.passfeder = passfeder
        self.K_A = K_A
        self.M_tnenn = M_tnenn
        self.R_emin = R_emin

        if hasattr(passfeder, "i"):
            assert i is None
            assert isinstance(self.passfeder.i, int)
            self.i = self.passfeder.i
        else:
            assert i is not None, "Passfederanzahl i must be specified"
            self.i = i

        [_print(key, "=", value) for key, value in vars(self).items()]

        self.M_teq = M_teq(self.K_A, self.M_tnenn)
        _print("M_teq =", self.M_teq)

        self.p_zul = p_zul(self.R_emin)
        _print("p_zul =", self.p_zul)

        self.l_tr = B.l_tr(self.passfeder.l, self.passfeder.b, self.passfeder.form)
        _print("l_tr =", self.l_tr)

        self.phi = phi(self.i)
        _print("phi =", self.phi)

        self.M_tzul = M_tzul(self.p_zul, self.passfeder.h, self.passfeder.t_1, self.l_tr, self.passfeder.d_1, self.i, self.phi)
        res = self.M_tzul >= self.M_teq

        if res:
            _print("\033[32mM_tzul =", self.M_tzul, ">=", self.M_teq, "\033[0m")
        else:
            _print("\033[31mM_tzul =", self.M_tzul, "<", self.M_teq, "\033[0m")

        if _assert:
            assert res