import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

taste = ctrl.Antecedent(np.arange(0, 11, 1), 'taste')
atmosphere = ctrl.Antecedent(np.arange(0, 11, 1), 'atmosphere')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')

tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

taste.automf(3)  
atmosphere.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 10])
tip['medium'] = fuzz.trimf(tip.universe, [5, 10, 20])
tip['high'] = fuzz.trimf(tip.universe, [10, 20, 25])

rule1 = ctrl.Rule(taste['poor'] | atmosphere['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(taste['average'] & atmosphere['average'] & service['average'], tip['medium'])
rule3 = ctrl.Rule(taste['good'] | atmosphere['good'] | service['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['taste'] = 8
tipping.input['atmosphere'] = 7
tipping.input['service'] = 9

tipping.compute()
print(f"Чаевые: {tipping.output['tip']:.2f}%")
