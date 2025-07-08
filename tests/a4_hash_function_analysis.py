import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

M = 512
K = 9
N_values = [2, 3, 4, 5, 6]
TOTAL_REQUESTS = 10000

def default_H(i):
    return (i + 2 * i + 17) % M

def default_Phi(i, j):
    return (i + j + 2 * j + 25) % M

def hash_A_H(i):
    return (i * 37) % M

def hash_A_Phi(i, j):
    return (i * 53 + j * 19) % M

def hash_B_H(i):
    return ((i << 3) ^ (i >> 1)) % M

def hash_B_Phi(i, j):
    return ((i * j) ^ (j << 2)) % M

def build_hash_ring(N, Phi_func):
    ring = {}
    server_ids = list(range(1, N+1))
    for sid in server_ids:
        for j in range(K):
            slot = Phi_func(sid, j) % M
            while slot in ring:
                slot = (slot + 1) % M
            ring[slot] = sid
    return dict(sorted(ring.items())), server_ids

def assign_requests(H_func, ring):
    slots = sorted(ring.keys())
    load_counter = Counter()
    for _ in range(TOTAL_REQUESTS):
        rid = random.randint(100000, 999999)
        h = H_func(rid)
        idx = next((slot for slot in slots if slot >= h), slots[0])
        server = ring[idx]
        load_counter[server] += 1
    return load_counter

def run_a41():
    results = {}
    hash_sets = {
        "Default": (default_H, default_Phi),
        "Hash A": (hash_A_H, hash_A_Phi),
        "Hash B": (hash_B_H, hash_B_Phi),
    }

    for name, (Hf, Pf) in hash_sets.items():
        ring, servers = build_hash_ring(3, Pf)
        counts = assign_requests(Hf, ring)
        results[name] = [counts[s] for s in servers]

    bar_width = 0.2
    x = np.arange(3)
    fig, ax = plt.subplots()
    for idx, (label, data) in enumerate(results.items()):
        ax.bar(x + idx * bar_width, data, bar_width, label=label)

    ax.set_xlabel("Server ID")
    ax.set_ylabel("Requests Handled")
    ax.set_title("A-4.1: Load Distribution Across 3 Servers")
    ax.set_xticks(x + bar_width)
    ax.set_xticklabels(['Server 1', 'Server 2', 'Server 3'])
    ax.legend()
    plt.tight_layout()
    plt.savefig("a4_1_load_distribution.png")
    plt.show()

def run_a42():
    hash_sets = {
        "Default": (default_H, default_Phi),
        "Hash A": (hash_A_H, hash_A_Phi),
        "Hash B": (hash_B_H, hash_B_Phi),
    }

    fig, ax = plt.subplots()
    for label, (Hf, Pf) in hash_sets.items():
        avg_loads = []
        for N in N_values:
            ring, servers = build_hash_ring(N, Pf)
            counts = assign_requests(Hf, ring)
            avg = sum(counts.values()) / len(servers)
            avg_loads.append(avg)
        ax.plot(N_values, avg_loads, marker='o', label=label)

    ax.set_xlabel("Number of Servers (N)")
    ax.set_ylabel("Average Requests per Server")
    ax.set_title("A-4.2: Scalability Test with Different Hash Functions")
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("a4_2_scalability.png")
    plt.show()

if __name__ == "__main__":
    run_a41()
    run_a42()
