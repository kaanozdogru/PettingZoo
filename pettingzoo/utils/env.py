class AECEnv(object):
    def __init__(self):
        pass

    def step(self, action, observe=True):
        raise NotImplementedError

    def reset(self, observe=True):
        raise NotImplementedError

    def observe(self, agent):
        raise NotImplementedError
    
    def last_cycle(self):
        agent = self.agent_selection
        return self.rewards[agent], self.dones[agent], self.infos[agent]

    def render(self, mode='human'):
        raise NotImplementedError

    def close(self):
        pass

class MarkovEnv(object):
    def __init__(self):
        pass
    
    def step(self, action):
        raise NotImplementedError
    
    def reset(self):
        raise NotImplementedError
        
    def render(self, mode='human'):
        raise NotImplementedError
    
    def close(self):
        pass
