from roboticstoolbox import DiffSteer


class DiffSteer2(DiffSteer):
    def init(self, x0=None, control=None, animate=True):
        super(DiffSteer, self).init(x0, control, animate)
        self._v_prev_L = [0]
        self._v_prev_R = [0]