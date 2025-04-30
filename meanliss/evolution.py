import numba as nb
import numpy as np

@nb.njit
def evolve(state: np.ndarray):
    next_state = np.zeros_like(state)
    
    filter_rows, filter_cols = 3, 3

    for i in range(state.shape[0] - filter_rows + 1):
        for j in range(state.shape[1] - filter_cols + 1):
            filter_view = state[i: i + filter_rows, j: j + filter_cols]

            curr_cell = filter_view[1, 1]

            live_cells = filter_view.sum() - curr_cell

            if curr_cell == 1:
                if live_cells < 2:
                    next_state[i + 1, j + 1] = 0

                elif live_cells == 2 or live_cells == 3:
                    next_state[i + 1, j + 1] = 1

                elif 3 < live_cells:
                    next_state[i + 1, j + 1] = 0

            else:
                if live_cells == 3:
                    next_state[i + 1, j + 1] = 1

    return next_state