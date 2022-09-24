version_name = 'v85'

ENV_CONFIG = {
    'num_agents': 3,
    'SIZE': (4,4),
    'agent_top_k': 2,
    'obstacle_top_k': 1,
    'PROB': (0.,0.1),
    'simple': True,
}

LR = 1e-2
PATIENCE = 2
DECAY_EXPLORE_RATE = 0.9
DECAY_NOMINAL_RATE = 0.
MIN_EXPLORE_EPS = 0.
MAX_EXPLORE_EPS = 0.5
POTENTIAL_OBS = False
TRAIN_ON_HARD = False
VARIABLE_AGENT = False
CBUF_BEFORE_RELABEL = True
REFINE_EPS = 1.0
RELABEL_ONLY_AGENT = False
ALL_LIE = False
ONLY_BOUNDARY = True


N_TRAJ = N_EPOCH = 4000
N_CBUF = 1000

SPATIAL_PROP = True
n_candidates = 2000
BATCH = 256
N_ITER = 100
N_TRAJ_PER_EPOCH = 10
N_BUFFER = 20
N_EVALUATE = 100
N_VALID = 100
N_WARMUP = 10
N_DATASET = 10
N_VALID_DATASET = 50
THRESHOLD = 1e-2
HIDDEN_SIZE = 128
RELABEL = True
EXPLORE_WAY = 'linear'
DECAY_RELABEL = False
USE_SCHEDULER = True
OPTIMIZER = 'SGD'
SAVE_GIF = False