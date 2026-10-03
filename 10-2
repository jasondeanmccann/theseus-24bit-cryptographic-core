import sys

# Define the Alphabet-First character map (0-69 base distribution)
ALPHANUMERIC_MAP = [
    # 0 - 25: a-z
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # 26 - 51: A-Z
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # 52 - 61: 0-9
    '0','1','2','3','4','5','6','7','8','9',
    # 62 - 69: Structural control symbols/padding tokens
    '!','@','#','$','%','^','&','*'
]

# Simulate the custom 24-bit cryptographic permutation logic
class TheseusSimulationCore:
    def forward(self, state: int) -> int:
        """
        Executes a 24-bit forward substitution-diffusion step.
        Enforces standard cryptographic state space bounds (2^24).
        """
        # Step 1: Reversible structural bit-mix layer (non-destructive XOR)
        mixed_state = (state ^ 0x5A5A5A) & 0xFFFFFF
        
        # Step 2: Modulo arithmetic dispersion step (dynamic rotation emulation)
        # Note: Bounded securely within the 24-bit active range
        dispersed = (mixed_state * 16777213 + 70) & 0xFFFFFF
        
        return dispersed

def submit_code_to_simulation(numeric_vector):
    core = TheseusSimulationCore()
    
    print("=" * 60)
    print("▶ LAUNCHING THESEUS CORE 24-BIT PERMUTATION SIMULATOR")
    print("=" * 60)
    
    # Translate vector values to alphanumeric string sequence
    translated_chars = []
    for val in numeric_vector:
        # Enforce Modulo 70 constraint to safely map index to available character space
        mapped_idx = val % 70
        translated_chars.append(ALPHANUMERIC_MAP[mapped_idx])
        
    payload_string = "".join(translated_chars)
    print(f"[*] Ingested Input Code String : '{payload_string}'")
    print(f"[*] Processing Numeric Vector  : {numeric_vector}\n")
    
    # Run the cryptographic state transitions
    print("--- Running Permutation State Transitions ---")
    final_states = []
    for step, val in enumerate(numeric_vector):
        permuted_output = core.forward(val)
        final_states.append(permuted_output)
        print(f" Round [{step+1}] | Input: {val:02d} -> 24-Bit Transformed State: 0x{permuted_output:06X}")
        
    print("\n" + "=" * 60)
    print("✅ SIMULATION PIPELINE COMPLETE")
    print(f"[*] Final Batch State Outputs : {final_states}")
    print("=" * 60)

if __name__ == "__main__":
    # The user target numbers submitted to the code execution pipeline
    target_vector = [11, 23, 44, 52, 67, 19]
    submit_code_to_simulation(target_vector)
