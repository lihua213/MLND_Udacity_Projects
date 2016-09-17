import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        valid_actions = [None, 'forward', 'left', 'right']
        TL_valid_states = [True, False]

        state_desc = {'light': TL_valid_states, 
                        'oncoming': valid_actions, 
                        'left': valid_actions, 
                        'right': valid_actions,
                        'next_waypoint': ['forward', 'left', 'right']}

        self.Q_prev = dict()
        self.gamma = 0.1
        self.alpha = 0.2
        self.p_threshold = 1
        
    

        # self.state = TrafficLight





    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        valid_actions = [None, 'forward', 'left', 'right']
        # TODO: Update state
        self.state = (inputs['light'],inputs['oncoming'],inputs['left'],inputs['right'],self.next_waypoint)



        # TODO: Select action according to your policy

        Q_actions = []

        for action_i in valid_actions:
            str_state_action = [str(s) for s in self.state ]
            str_state_action.append(str(action_i))
            str_state_action  = ",".join(str_state_action)
            if len(self.Q_prev)==0:
                self.Q_prev[str_state_action] = 0
                Q_actions.append(0)
            else:
                if str_state_action in self.Q_prev.keys():
                    Q_actions.append(self.Q_prev[str_state_action])
                else:
                    self.Q_prev[str_state_action] = 0
                    Q_actions.append(0)

        Q_max = max(Q_actions)
        action_max_inds = [valid_actions[i] for i in range(len(valid_actions)) if Q_max == Q_actions[i]]
        action = random.choice(action_max_inds)

        str_state_action_now = [str(s) for s in self.state ]
        str_state_action_now.append(str(action))
        str_state_action_now  = ",".join(str_state_action_now)

        #action_random = [None, 'forward', 'left', 'right']
        #rand_action = action_random[random.randint(0,3)]
        #action = rand_action

        #print (self.state,action)


        # Execute action and get reward
        reward = self.env.act(self, action)
        self.Q_prev[str_state_action_now] += self.alpha*(reward + self.gamma*Q_max)




        # TODO: Learn policy based on state, action, reward
        

        #Q(state,action) = 

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=False)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=.5, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=10)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
