import pprint

MOUNTAIN_CAR_CONFIG = "mountain_car"
CUP_CATCH_CONFIG = "cup_catch"
HALF_CHEETAH_RUN_CONFIG = "half_cheetah_run"
HALF_CHEETAH_FLIP_CONFIG = "half_cheetah_flip"
REACHER_CONFIG = "reacher"
ANT_MAZE = "ant_maze"
DEBUG_CONFIG = "debug"
CARTPOLE_CONFIG = "cartpole"
PENDULUM_CONFIG = "pendulum"
BARL_REACHER_CONFIG = "barl_reacher"
BETA_TRACKING_CONFIG = "beta_tracking"
BETA_ROTATION_CONFIG = "beta_rotation"
ANT_MAZE = "ant_maze"

def print_configs():
    print(f"[{MOUNTAIN_CAR_CONFIG}, {CUP_CATCH_CONFIG}, {HALF_CHEETAH_RUN_CONFIG}, {HALF_CHEETAH_FLIP_CONFIG}, {REACHER_CONFIG}, {ANT_MAZE}, {DEBUG_CONFIG} ")

def get_config(args):
    if args.config_name == MOUNTAIN_CAR_CONFIG:
        config = MountainCarConfig()
    elif args.config_name == CUP_CATCH_CONFIG:
        config = CupCatchConfig()
    elif args.config_name == HALF_CHEETAH_RUN_CONFIG:
        config = HalfCheetahRunConfig()
    elif args.config_name == HALF_CHEETAH_FLIP_CONFIG:
        config = HalfCheetahFlipConfig()
    elif args.config_name == REACHER_CONFIG:
        config = ReacherConfig()
    elif args.config_name == ANT_MAZE:
        config = AntMazeConfig()
    elif args.config_name == DEBUG_CONFIG:
        config = DebugConfig()
    elif args.config_name == CARTPOLE_CONFIG:
        config = CartpoleConfig()
    elif args.config_name == PENDULUM_CONFIG:
        config = PendulumConfig()
    elif args.config_name == BARL_REACHER_CONFIG:
        config = BARLReacherConfig()
    elif args.config_name == BETA_TRACKING_CONFIG:
        config = BetaTrackingConfig()
    elif args.config_name == BETA_ROTATION_CONFIG:
        config = BetaRotationConfig()
    else:
        raise ValueError("`{}` is not a valid config ID".format(args.config_name))

    config.set_logdir(args.logdir)
    config.set_seed(args.seed)
    config.set_strategy(args.strategy)
    return config


class Config(object):
    def __init__(self):
        self.logdir = "log"
        self.seed = 0
        self.n_episodes = 50
        self.n_seed_episodes = 5
        self.record_every = None
        self.coverage = False

        self.env_name = None
        self.max_episode_len = 500
        self.action_repeat = 3
        self.action_noise = None

        self.ensemble_size = 10
        self.hidden_size = 200

        self.n_train_epochs = 100
        self.batch_size = 50
        self.learning_rate = 1e-3
        self.epsilon = 1e-8
        self.grad_clip_norm = 1000

        self.plan_horizon = 30
        self.optimisation_iters = 5
        self.n_candidates = 500
        self.top_candidates = 50

        self.expl_strategy = "information"
        self.use_reward = True
        self.use_exploration = True
        self.use_mean = False

        self.expl_scale = 1.0
        self.reward_scale = 1.0

    def set_logdir(self, logdir):
        self.logdir = logdir

    def set_seed(self, seed):
        self.seed = seed

    def set_strategy(self, strategy):
        self.strategy = strategy

    def __repr__(self):
        return pprint.pformat(vars(self))


class DebugConfig(Config):
    def __init__(self):
        super().__init__()
        self.env_name = "Pendulum-v0"
        self.n_episodes = 5
        self.max_episode_len = 100
        self.hidden_size = 64
        self.plan_horizon = 5


class MountainCarConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "mountain_car"
        self.env_name = "SparseMountainCar"
        self.max_episode_len = 500
        self.n_train_epochs = 100
        self.n_seed_episodes = 1
        self.expl_scale = 1.0
        self.n_episodes = 30
        self.ensemble_size = 25
        self.record_every = None
        self.n_episodes = 50


class CupCatchConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "catch"
        self.env_name = "DeepMindCatch"
        self.max_episode_len = 1000
        self.action_repeat = 4
        self.plan_horizon = 12
        self.expl_scale = 0.1
        self.record_every = None
        self.n_episodes = 50


class HalfCheetahRunConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "half_cheetah_run"
        self.env_name = "HalfCheetahRun"
        self.n_episodes = 100
        self.n_seed_episodes = 5
        self.max_episode_len = 100
        self.action_repeat = 2

        self.ensemble_size = 15
        self.hidden_size = 400

        self.n_train_epochs = 100
        self.batch_size = 50

        self.plan_horizon = 15
        self.optimisation_iters = 7
        self.n_candidates = 700
        self.top_candidates = 70

        self.use_exploration = True
        self.use_mean = True
        self.expl_scale = 0.1


class HalfCheetahFlipConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "half_cheetah_flip"
        self.env_name = "HalfCheetahFlip"
        self.n_episodes = 100
        self.n_seed_episodes = 5
        self.max_episode_len = 100
        self.action_repeat = 2

        self.ensemble_size = 15
        self.hidden_size = 400

        self.n_train_epochs = 100
        self.batch_size = 50

        self.plan_horizon = 15
        self.optimisation_iters = 7
        self.n_candidates = 700
        self.top_candidates = 70

        self.use_exploration = True
        self.use_mean = True
        self.expl_scale = 0.1


class AntMazeConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "ant_maze"
        self.env_name = "AntMaze"
        self.n_episodes = 50
        self.n_seed_episodes = 5
        self.max_episode_len = 300
        self.action_repeat = 4
        self.coverage = True

        self.ensemble_size = 15
        self.hidden_size = 400

        self.n_train_epochs = 200
        self.batch_size = 50

        self.plan_horizon = 30
        self.optimisation_iters = 7
        self.n_candidates = 700
        self.top_candidates = 70

        self.use_exploration = True
        self.use_reward = False
        self.use_mean = True
        self.expl_scale = 1.0


class ReacherConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "reacher"
        self.env_name = "DeepMindReacher"
        self.n_episodes = 100
        self.n_seed_episodes = 5
        self.max_episode_len = 1000
        self.action_repeat = 4

        self.ensemble_size = 15
        self.hidden_size = 400

        self.n_train_epochs = 100
        self.batch_size = 50

        self.plan_horizon = 30
        self.optimisation_iters = 5
        self.n_candidates = 500
        self.top_candidates = 50

        self.use_exploration = True
        self.use_reward = True
        self.use_mean = True
        self.expl_scale = 0.1


class CartpoleConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "cartpole"
        self.env_name = "pilcocartpole-v0"
        self.max_episode_len = 25
        self.n_train_epochs = 100
        self.n_seed_episodes = 1
        self.expl_scale = 0.1
        self.n_episodes = 100
        self.ensemble_size = 25
        self.record_every = None


class PendulumConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "pendulum"
        self.env_name = "bacpendulum-v0"
        self.max_episode_len = 200
        self.n_train_epochs = 100
        self.n_seed_episodes = 1
        self.expl_scale = 1.0
        self.n_episodes = 30
        self.ensemble_size = 25
        self.record_every = None


class BARLReacherConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "barl_reacher"
        self.env_name = "bacreacher-v0"
        self.max_episode_len = 50
        self.n_train_epochs = 500
        self.n_seed_episodes = 5
        self.expl_scale = 0.1
        self.n_episodes = 100
        self.batch_size = 50
        self.plan_horizon = 30
        self.optimisation_iters = 5
        self.n_candidates = 500
        self.top_canditates = 50
        self.use_mean = True
        self.ensemble_size = 15
        self.action_repeat = 4
        self.record_every = None


class BetaTrackingConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "beta_tracking"
        self.env_name = "betatracking-v0"
        self.max_episode_len = 15
        self.n_train_epochs = 100
        self.n_seed_episodes = 1
        self.expl_scale = 0.1
        self.n_episodes = 100
        self.ensemble_size = 25
        self.record_every = None

class BetaRotationConfig(Config):
    def __init__(self):
        super().__init__()
        self.logdir = "beta_rotation"
        self.env_name = "newbetarotation-v0"
        self.max_episode_len = 10
        self.n_train_epochs = 100
        self.n_seed_episodes = 1
        self.expl_scale = 1.0
        self.n_episodes = 100
        self.ensemble_size = 25
        self.record_every = None
