"""
Theseus 24-Bit Core Master Simulator
Executes multi-architecture pipeline benchmarks for comparison tracking.
"""

import sys
from src.theseus_core import TheseusCore
from src.theseus_core_rc2 import TheseusCoreRC2

# Base-70 Alphanumeric Matrix for Human-Readable Ingestion Tracing
ALPHANUMERIC_MAP = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',
    '!','@','#','$','%','^','&','*'
]

def run_comparative_simulation(numeric_vector):
    # Initialize both core candidates
    core_rc1 = TheseusCore()
    core_rc2 = TheseusCoreRC2()
    
    print("=" * 70)
    print("▶ INITIALIZING THESEUS MULTI-CORE SIMULATION BENCHMARK")
    print("=" * 70)
    
    # 1. Translate numeric indices using modulo-70 constraints
    translated_chars = [ALPHANUMERIC_MAP[val % 70] for val in numeric_vector]
    payload_string = "".join(translated_chars)
    
    print(f"[*] Raw Ingested Input Code Vector : {numeric_vector}")
    print(f"[*] Base-70 Alphanumeric Code String: '{payload_string}'\n")
    
    print(f"{'Round':<7} | {'Input':<5} | {'RC1 State (Hex)':<18} | {'RC2 Avalanche Ciphertext':<24}")
    print("-" * 70)
    
    rc1_outputs = []
    rc2_outputs = []
    
    # 2. Run synchronous forward processing passes
    for step, val in enumerate(numeric_vector):
        out_rc1 = core_rc1.forward(val)
        out_rc2 = core_rc2.forward(val)
        
        rc1_outputs.append(out_rc1)
        rc2_outputs.append(out_rc2)
        
        print(f"Step [{step+1}] | {val:02d}    | 0x{out_rc1:06X}           | 0x{out_rc2:06X}")
        
    print("-" * 70)
    print("⚡ VERIFYING DECRYPTION STABILITY (ROUND-TRIP RECOVERY)")
    
    # 3. Enforce reciprocal reverse recovery path testing
    rc1_recovered = [core_rc1.inverse(y) for y in rc1_outputs]
    rc2_recovered = [core_rc2.inverse(y) for y in rc2_outputs]
    
    rc1_status = "PASS" if rc1_recovered == numeric_vector else "FAIL"
    rc2_status = "PASS" if rc2_recovered == numeric_vector else "FAIL"
    
    print(f"[*] RC1 Reversibility Audit : [{rc1_status}]")
    print(f"[*] RC2 Reversibility Audit : [{rc2_status}]")
    
    print("=" * 70)
    print("✅ SIMULATION BATCH ENGINE PROCESSING RELEASES COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    # Target execution parameters submitted to the simulator
    target_vector = [11, 23, 44, 52, 67, 19]
    run_comparative_simulation(target_vector)
