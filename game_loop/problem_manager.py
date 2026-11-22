from enum import Enum

class COMPONENTS(Enum):
    RAM = 0
    CPU = 1
    PLACAMAE = 2

QUESTS = [
    [(COMPONENTS.RAM, "Memória RAM danificada") , { COMPONENTS.CPU:"Very bad sir" }, (COMPONENTS.RAM, "Trocar resolveu o problema")]
]