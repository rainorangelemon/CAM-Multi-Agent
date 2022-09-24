version_name = 'v62'
OBSTACLE_DENSITY = 1.0
LR = 3e-4
PATIENCE = 2
DECAY_EXPLORE_RATE = 0.97
DECAY_NOMINAL_RATE = 0.
MIN_EXPLORE_EPS = 0.
MAX_EXPLORE_EPS = 0.1
POTENTIAL_OBS = False
TRAIN_ON_HARD = False
VARIABLE_AGENT = False
CBUF_BEFORE_RELABEL = True
REFINE_EPS = 1.0
RELABEL_ONLY_AGENT = False
ALL_LIE = False


N_TRAJ = N_EPOCH = 1000000
N_CBUF = 0

NUM_AGENTS = 8
MAP_SIZE = 4

n_candidates = 2000
BATCH = 1024
N_ITER = 100
N_TRAJ_PER_EPOCH = 10
N_BUFFER = 20
N_EVALUATE = 100
N_VALID = 100
N_WARMUP = 100
N_DATASET = 10
N_VALID_DATASET = 20
THRESHOLD = 1e-2
HIDDEN_SIZE = 128
RELABEL = True
CYCLIC = True
DECAY_RELABEL = False
USE_SCHEDULER = True
OPTIMIZER = 'Adam'
SAVE_GIF = False