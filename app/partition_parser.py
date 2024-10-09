# app/partition_parser.py

def parse_partition(lines):
    sequence = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            print(f"Ligne ignorée (format incorrect) : {line}")
            continue
        note, duration_str = parts
        try:
            duration = float(duration_str)
        except ValueError:
            print(f"Durée invalide sur la ligne : {line}")
            continue
        
        # Si la note est "0", cela représente un silence
        if note == "0":
            sequence.append(("silence", duration))  # Ajoute un silence
        else:
            sequence.append((note, duration))
    
    return sequence
