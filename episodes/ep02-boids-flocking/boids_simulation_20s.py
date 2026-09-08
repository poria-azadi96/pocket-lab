import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ==========================================
# 1. SIMULATION SETUP & CONSTANTS (20 SECONDS)
# ==========================================
FPS = 25
DURATION_SEC = 20
TOTAL_FRAMES = DURATION_SEC * FPS  # Exactly 500 frames

NUM_BOIDS = 130
WIDTH, HEIGHT = 100.0, 177.7       # Exact 9:16 vertical ratio

# Behavioral Radii & Kinematics
VISUAL_RADIUS = 16.0
MIN_DISTANCE = 4.2
MAX_SPEED = 2.6
MAX_FORCE = 0.14

W_SEP = 1.8  # Rule 1: Separation (Avoid collisions)
W_ALI = 1.1  # Rule 2: Alignment (Match neighbors' heading)
W_COH = 0.9  # Rule 3: Cohesion (Stay close to group center)

# Initialize positions and randomized velocities
np.random.seed(42)
positions = np.random.rand(NUM_BOIDS, 2) * [WIDTH, HEIGHT]
angles = np.random.rand(NUM_BOIDS) * 2 * np.pi
velocities = np.column_stack([np.cos(angles), np.sin(angles)]) * MAX_SPEED

# ==========================================
# 2. NUMERICAL KINEMATICS ENGINE
# ==========================================
def update_physics(pos, vel):
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dist = np.linalg.norm(diff, axis=2)

    in_range = (dist > 0) & (dist < VISUAL_RADIUS)
    too_close = (dist > 0) & (dist < MIN_DISTANCE)

    sep_steer = np.zeros_like(vel)
    ali_steer = np.zeros_like(vel)
    coh_steer = np.zeros_like(vel)
    local_order = np.zeros(NUM_BOIDS)

    for i in range(NUM_BOIDS):
        neighbors = in_range[i]
        close_neighbors = too_close[i]

        # 1. Separation
        if np.any(close_neighbors):
            repulsion = -diff[i, close_neighbors] / (dist[i, close_neighbors, np.newaxis] + 1e-4)
            sep_steer[i] = np.sum(repulsion, axis=0)

        # 2. Alignment & 3. Cohesion
        if np.any(neighbors):
            avg_vel = np.mean(vel[neighbors], axis=0)
            ali_steer[i] = avg_vel - vel[i]
            coh_steer[i] = np.mean(diff[i, neighbors], axis=0)
            
            # Local alignment index (0.0 = chaotic, 1.0 = aligned)
            v_norm = vel[i] / np.linalg.norm(vel[i])
            n_norms = vel[neighbors] / (np.linalg.norm(vel[neighbors], axis=1, keepdims=True) + 1e-5)
            local_order[i] = max(0.0, np.mean(np.dot(n_norms, v_norm)))

    def limit(vectors, max_val):
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return np.where(norms > max_val, (vectors / norms) * max_val, vectors)

    sep = limit(sep_steer, MAX_FORCE) * W_SEP
    ali = limit(ali_steer, MAX_FORCE) * W_ALI
    coh = limit(coh_steer, MAX_FORCE) * W_COH

    # Soft boundary turning force
    boundary_force = np.zeros_like(vel)
    margin = 12.0
    turn_factor = 0.28

    boundary_force[pos[:, 0] < margin, 0] += turn_factor
    boundary_force[pos[:, 0] > WIDTH - margin, 0] -= turn_factor
    boundary_force[pos[:, 1] < margin, 1] += turn_factor
    boundary_force[pos[:, 1] > HEIGHT - margin, 1] -= turn_factor

    acceleration = sep + ali + coh + boundary_force
    new_vel = limit(vel + acceleration, MAX_SPEED)
    new_pos = pos + new_vel

    new_pos[:, 0] = np.clip(new_pos[:, 0], 1, WIDTH - 1)
    new_pos[:, 1] = np.clip(new_pos[:, 1], 1, HEIGHT - 1)

    return new_pos, new_vel, local_order

# Precompute trajectory
print(f"Calculating flocking physics ({DURATION_SEC}s, {TOTAL_FRAMES} frames)...")
pos_seq = np.zeros((TOTAL_FRAMES, NUM_BOIDS, 2))
vel_seq = np.zeros((TOTAL_FRAMES, NUM_BOIDS, 2))
order_seq = np.zeros((TOTAL_FRAMES, NUM_BOIDS))
global_order_metric = np.zeros(TOTAL_FRAMES)

curr_pos = positions.copy()
curr_vel = velocities.copy()

for f in range(TOTAL_FRAMES):
    pos_seq[f] = curr_pos
    vel_seq[f] = curr_vel
    curr_pos, curr_vel, local_ord = update_physics(curr_pos, curr_vel)
    order_seq[f] = local_ord

    # Global Polarization Order Parameter (0% to 100%)
    mean_velocity = np.mean(curr_vel, axis=0)
    avg_speed = np.mean(np.linalg.norm(curr_vel, axis=1))
    global_order_metric[f] = (np.linalg.norm(mean_velocity) / (avg_speed + 1e-5)) * 100.0

# ==========================================
# 3. HIGH-CONTRAST MOBILE RENDERER (9:16)
# ==========================================
fig, ax = plt.subplots(figsize=(6, 10.66), facecolor="#020202")
ax.set_facecolor("#020202")
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.axis("off")

cmap = plt.cm.plasma

quiver = ax.quiver(
    pos_seq[0, :, 0], pos_seq[0, :, 1],
    vel_seq[0, :, 0], vel_seq[0, :, 1],
    order_seq[0],
    cmap=cmap, clim=[0.0, 1.0],
    scale=34, width=0.008,
    headwidth=4.5, headlength=5.0, headaxislength=4.5,
    pivot='mid', alpha=0.95
)

glow = ax.scatter(
    pos_seq[0, :, 0], pos_seq[0, :, 1],
    c=order_seq[0], cmap=cmap, vmin=0.0, vmax=1.0,
    s=55, alpha=0.35, edgecolors='none'
)

# HUD elements
hud_title = ax.text(0.05, 0.95, "EPISODE 02 // BOIDS EMERGENCE", transform=ax.transAxes,
                    color="#FFFFFF", fontsize=11, fontfamily="monospace", weight="bold")
hud_timer = ax.text(0.05, 0.92, "", transform=ax.transAxes,
                    color="#A0A0A0", fontsize=9, fontfamily="monospace")
hud_order = ax.text(0.05, 0.89, "", transform=ax.transAxes,
                    color="#00E5FF", fontsize=10, fontfamily="monospace", weight="bold")
hud_state = ax.text(0.05, 0.86, "", transform=ax.transAxes,
                    color="#FFD700", fontsize=9, fontfamily="monospace")

ax.text(0.05, 0.03, "RULES: 1.Separate  2.Align  3.Cohere", transform=ax.transAxes,
        color="#666666", fontsize=8, fontfamily="monospace")

def update(frame):
    pos = pos_seq[frame]
    vel = vel_seq[frame]
    ord_val = order_seq[frame]
    current_time = frame / FPS
    order_pct = global_order_metric[frame]

    quiver.set_offsets(pos)
    quiver.set_UVC(vel[:, 0], vel[:, 1])
    quiver.set_array(ord_val)

    glow.set_offsets(pos)
    glow.set_array(ord_val)

    hud_timer.set_text(f"TIME: {current_time:04.1f}s / {DURATION_SEC}.0s")
    bar_length = int(order_pct / 10)
    bar_display = "[" + "#" * bar_length + "-" * (10 - bar_length) + "]"
    hud_order.set_text(f"SWARM ORDER: {order_pct:04.1f}% {bar_display}")

    if current_time < 3.5:
        hud_state.set_text("PHASE: 1. RANDOM DISPERSION (CHAOS)")
        hud_state.set_color("#FF5555")
    elif current_time < 9.0:
        hud_state.set_text("PHASE: 2. LOCAL SYNC (CLUSTER FORMATION)")
        hud_state.set_color("#FFAA00")
    else:
        hud_state.set_text("PHASE: 3. GLOBAL SWARM INTELLIGENCE")
        hud_state.set_color("#00FFCC")

    return quiver, glow, hud_timer, hud_order, hud_state

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

output_name = "boids_flocking_20s.gif"
print(f"Rendering 500 frames to {output_name}...")
ani.save(output_name, writer=PillowWriter(fps=FPS))
print(f"Export successful: {output_name}")
