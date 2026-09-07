import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ==========================================
# 1. PHYSICAL CONSTANTS & EQUATIONS OF MOTION
# ==========================================
G = 9.81           # Acceleration due to gravity (m/s^2)
L1, L2 = 1.0, 1.0  # Pendulum rod lengths (meters)
M1, M2 = 1.0, 1.0  # Bob masses (kg)

def derivatives(state):
    """
    Computes angular accelerations using coupled Lagrangian mechanics.
    state = [theta1, omega1, theta2, omega2]
    """
    t1, w1, t2, w2 = state
    delta = t1 - t2
    den = 2 * M1 + M2 - M2 * np.cos(2 * t1 - 2 * t2)

    # Angular acceleration for bob 1 (alpha1)
    num1 = (-G * (2 * M1 + M2) * np.sin(t1) 
            - M2 * G * np.sin(t1 - 2 * t2) 
            - 2 * np.sin(delta) * M2 * (w2**2 * L2 + w1**2 * L1 * np.cos(delta)))
    alpha1 = num1 / (L1 * den)

    # Angular acceleration for bob 2 (alpha2)
    num2 = (2 * np.sin(delta) * (w1**2 * L1 * (M1 + M2) 
            + G * (M1 + M2) * np.cos(t1) 
            + w2**2 * L2 * M2 * np.cos(delta)))
    alpha2 = num2 / (L2 * den)

    return np.array([w1, alpha1, w2, alpha2])

def rk4_step(state, dt):
    """4th-order Runge-Kutta numerical integration step."""
    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)
    return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

# ==========================================
# 2. SIMULATION TIMING & INITIAL PERTURBATION
# ==========================================
FPS = 25
DURATION_SEC = 20                  # Exact 20 seconds duration
TOTAL_FRAMES = DURATION_SEC * FPS  # Exactly 500 frames
DT_FRAME = 1.0 / FPS
SUB_STEPS = 5                      # 5 steps per frame for high numerical stability
DT_SUB = DT_FRAME / SUB_STEPS

# Initial angles: Released from horizontal position (90 degrees)
INITIAL_THETA1 = np.pi / 2
INITIAL_THETA2 = np.pi / 2

# Exact 1.0 degree perturbation for system B
DELTA_THETA = np.radians(1.0)

state_a = np.array([INITIAL_THETA1, 0.0, INITIAL_THETA2, 0.0])
state_b = np.array([INITIAL_THETA1 + DELTA_THETA, 0.0, INITIAL_THETA2, 0.0])

history_a = np.zeros((TOTAL_FRAMES, 4))
history_b = np.zeros((TOTAL_FRAMES, 4))

print(f"Integrating physics for {DURATION_SEC}s ({TOTAL_FRAMES} frames)...")
for frame in range(TOTAL_FRAMES):
    history_a[frame] = state_a
    history_b[frame] = state_b
    for _ in range(SUB_STEPS):
        state_a = rk4_step(state_a, DT_SUB)
        state_b = rk4_step(state_b, DT_SUB)

# Convert polar angles to Cartesian coordinates (X, Y)
# System A (Cyan)
x1_a = L1 * np.sin(history_a[:, 0])
y1_a = -L1 * np.cos(history_a[:, 0])
x2_a = x1_a + L2 * np.sin(history_a[:, 2])
y2_a = y1_a - L2 * np.cos(history_a[:, 2])

# System B (Magenta)
x1_b = L1 * np.sin(history_b[:, 0])
y1_b = -L1 * np.cos(history_b[:, 0])
x2_b = x1_b + L2 * np.sin(history_b[:, 2])
y2_b = y1_b - L2 * np.cos(history_b[:, 2])

# ==========================================
# 3. VISUALIZATION (VERTICAL 9:16 FORMAT)
# ==========================================
fig, ax = plt.subplots(figsize=(6, 10.6), facecolor="#020202")
ax.set_facecolor("#020202")
ax.set_xlim(-2.3, 2.3)
ax.set_ylim(-2.5, 1.5)
ax.axis("off")

# Fixed center anchor
ax.plot(0, 0, marker="o", markersize=6, color="#FFFFFF", alpha=0.9)

# System A (Cyan - Base Pendulum)
trail_a, = ax.plot([], [], color="#00E5FF", lw=1.6, alpha=0.75, label="Base Pendulum")
line_a, = ax.plot([], [], "o-", color="#80F0FF", lw=2.2, markersize=7, zorder=4)

# System B (Neon Magenta - Perturbed by 1.0 Degree)
trail_b, = ax.plot([], [], color="#FF0077", lw=1.6, alpha=0.75, label="Perturbed (+1.0°)")
line_b, = ax.plot([], [], "o-", color="#FFA0CF", lw=2.2, markersize=7, zorder=5)

# Digital HUD overlay metrics
time_text = ax.text(0.05, 0.94, "", transform=ax.transAxes, color="#FFFFFF",
                    fontsize=12, family="monospace", weight="bold")
delta_text = ax.text(0.05, 0.90, "Delta Theta: 1.0°", 
                     transform=ax.transAxes, color="#FFD700", fontsize=10, family="monospace")

# High-contrast legend
ax.legend(loc="upper right", facecolor="#101010", edgecolor="#2B2B2B",
          labelcolor="#E0E0E0", fontsize=9, framealpha=0.85)

TRAIL_LENGTH = 100  # 4 seconds of dynamic neon trajectory history

def update(frame):
    start_idx = max(0, frame - TRAIL_LENGTH)

    # Update neon trails
    trail_a.set_data(x2_a[start_idx:frame], y2_a[start_idx:frame])
    trail_b.set_data(x2_b[start_idx:frame], y2_b[start_idx:frame])

    # Update physical arms
    line_a.set_data([0, x1_a[frame], x2_a[frame]], [0, y1_a[frame], y2_a[frame]])
    line_b.set_data([0, x1_b[frame], x2_b[frame]], [0, y1_b[frame], y2_b[frame]])

    # Update real-time clock
    current_time = frame * DT_FRAME
    time_text.set_text(f"Time: {current_time:.1f}s / {DURATION_SEC}.0s")

    return trail_a, trail_b, line_a, line_b, time_text

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

# ==========================================
# 4. EXPORT ANIMATION
# ==========================================
output_filename = "double_pendulum_chaos_20s.gif"
print(f"Rendering {TOTAL_FRAMES} frames ({DURATION_SEC}s)...")
ani.save(output_filename, writer=PillowWriter(fps=FPS))
print(f"Done! File saved successfully as: {output_filename}")
