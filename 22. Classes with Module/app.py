import Agent

agent_1 = Agent.agent('Shaktimaan', 32)
agent_1.health = agent_1.health * 100
print(agent_1.info())
print('-'*30)

agent_2 = Agent.agent('Gangadhar', 32)
print(agent_2.info())
print('-'*30)

boss = Agent.agent('Kilvish', 200)
boss.health *= 1000
print(boss.info())
print('-'*30)
