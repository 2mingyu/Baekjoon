"""
진흥원 세미나
"""
T = {'Algorithm': 204,
     'DataAnalysis': 207,
     'ArtificialIntelligence': 302,
     'CyberSecurity': 'B101',
     'Network': 303,
     'Startup': 501,
     'TestStrategy': 105
     }
N = int(input())
for _ in range(N):
    print(T[input()])