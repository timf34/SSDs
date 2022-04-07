import numpy as np
import gym
from gym.envs.registration import register

register(
    id='CommonsGame_v0',
    entry_point='CommonsGame.envs:CommonsGame',
)

numAgents = 11

env = gym.make('CommonsGame_v0', numAgents=numAgents, visualRadius=4)
env.reset()
for t in range(1000):
    nActions = np.random.randint(low=0, high=env.action_space.n, size=(numAgents,)).tolist()
    nObservations, nRewards, nDone, nInfo = env.step(nActions)
    env.render()
