from gym.envs.registration import register
# from envs.env import CommonsGame

# Note: I'm not sure why this wouldn't work for me but I was able to move it directly to the example.py script
# Source: https://stackoverflow.com/questions/52727233/how-can-i-register-a-custom-environment-in-openais-gym
register(
    id='CommonsGame-v0',
    entry_point='CommonsGame.envs:CommonsGame',
)