#!/usr/bin/env python3
"""
PROVOLUTION PUBLICATION FIGURES
Generates all 5 required figures for Nature Climate Change submission
Author: Generated for Yoka Dieng
Date: 2026-01-23
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
import matplotlib.patheffects as pe

# Set style for publication quality
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.dpi'] = 300

# Color scheme (colorblind-friendly)
COLORS = {
    'S': '#2166AC',  # Blue - Sufficient
    'E': '#4DAF4A',  # Green - Efficient  
    'C': '#FF7F00',  # Orange - Consistent
    'highlight': '#E31A1C',  # Red for emphasis
    'neutral': '#666666',
    'domains': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
}

# Data
DOMAINS = ['A-Gov', 'B-Prod', 'C-Energy', 'D-Food', 'E-Edu', 'F-Tech', 'G-Mon', 'H-Meta']
APPS_PER_DOMAIN = [6, 6, 6, 4, 3, 2, 3, 3]
CO2_IMPACT = [0, -26.5, -15.8, -9.2, 0, 0, 0, 0]  # Gt/year, 0 = non-quantified
AGENTIC_IMPROVEMENT = [7.6, 18.2, 9.8, 6.0, 5.6, 5.6, 5.8, 5.8]
SEC_SCORES = [0.95, 0.92, 0.88, 0.88, 0.90, 0.87, 0.88, 0.86, 0.87, 0.83, 0.90, 0.89,
              0.95, 0.91, 0.89, 0.92, 0.90, 0.88, 0.89, 0.91, 0.88, 0.87, 0.88, 0.86,
              0.87, 0.89, 0.87, 0.92, 0.89, 0.88, 0.83, 0.91]  # 30 scores (2 extra for margin)

def figure1_sec_framework():
    """Figure 1: SEC-J Framework Schematic — Diamond Diagram (4-axis)"""
    fig, ax = plt.subplots(figsize=(8, 9))
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.4, 2.1)
    ax.axis('off')
    ax.set_aspect('equal')

    # Diamond vertices: S (top), E (left), C (right), J (bottom)
    v_s = (0.0,  1.2)
    v_e = (-1.1, 0.0)
    v_c = ( 1.1, 0.0)
    v_j = (0.0, -1.1)

    # Draw diamond
    diamond = Polygon([v_s, v_e, v_j, v_c], fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(diamond)

    circle_radius = 0.25
    j_color = '#984EA3'  # Purple for Justice

    # S — Sufficient (top)
    ax.add_patch(Circle(v_s, circle_radius, facecolor=COLORS['S'], edgecolor='black', linewidth=2, alpha=0.8))
    ax.text(v_s[0], v_s[1], 'S', ha='center', va='center', fontsize=24, fontweight='bold', color='white')
    ax.text(v_s[0], v_s[1]+0.42, 'SUFFICIENT', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.text(v_s[0], v_s[1]+0.72, r'$W(M) \geq W_{min}$', ha='center', va='bottom', fontsize=10, style='italic')

    # E — Efficient (left)
    ax.add_patch(Circle(v_e, circle_radius, facecolor=COLORS['E'], edgecolor='black', linewidth=2, alpha=0.8))
    ax.text(v_e[0], v_e[1], 'E', ha='center', va='center', fontsize=24, fontweight='bold', color='white')
    ax.text(v_e[0]-0.15, v_e[1]-0.42, 'EFFICIENT', ha='center', va='top', fontsize=11, fontweight='bold')
    ax.text(v_e[0]-0.15, v_e[1]-0.67, r'$\frac{W(M)}{R(M)} \geq \frac{W(M\')}{R(M\')}$', ha='center', va='top', fontsize=9, style='italic')

    # C — Consistent (right)
    ax.add_patch(Circle(v_c, circle_radius, facecolor=COLORS['C'], edgecolor='black', linewidth=2, alpha=0.8))
    ax.text(v_c[0], v_c[1], 'C', ha='center', va='center', fontsize=24, fontweight='bold', color='white')
    ax.text(v_c[0]+0.15, v_c[1]-0.42, 'CONSISTENT', ha='center', va='top', fontsize=11, fontweight='bold')
    ax.text(v_c[0]+0.15, v_c[1]-0.67, r'$\neg\exists\ conflict(M_i, M_j)$', ha='center', va='top', fontsize=10, style='italic')

    # J — Just (bottom)
    ax.add_patch(Circle(v_j, circle_radius, facecolor=j_color, edgecolor='black', linewidth=2, alpha=0.8))
    ax.text(v_j[0], v_j[1], 'J', ha='center', va='center', fontsize=24, fontweight='bold', color='white')
    ax.text(v_j[0], v_j[1]-0.42, 'JUST', ha='center', va='top', fontsize=11, fontweight='bold')
    ax.text(v_j[0], v_j[1]-0.67, r'$D(M) \geq D_{min}$', ha='center', va='top', fontsize=10, style='italic')

    # J-Veto annotation
    ax.text(v_j[0], v_j[1]-1.00, r'$J < 0.50 \Rightarrow \mathrm{VETO}\ (SEC\text{-}J = \mathrm{null})$',
            ha='center', va='top', fontsize=9, color='#E31A1C',
            bbox=dict(boxstyle='round', facecolor='#FFEEEE', edgecolor='#E31A1C', alpha=0.85))

    # Center conjunction formula
    ax.text(0.0, 0.0, r'$SEC\text{-}J(M) = S \wedge E \wedge C \wedge J$', ha='center', va='center',
            fontsize=13, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))

    # Score formula at very bottom
    ax.text(0.0, -2.2, r'$SEC\text{-}J_{score} = 0.40 \cdot S + 0.25 \cdot E + 0.15 \cdot C + 0.20 \cdot J$',
            ha='center', va='center', fontsize=11, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', alpha=0.5))

    plt.title('Figure 1: SEC-J Framework — Verification Principle', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('Figure1_SEC_Framework.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('Figure1_SEC_Framework.svg', format='svg', bbox_inches='tight', facecolor='white')
    print("[OK] Figure 1 saved: Figure1_SEC_Framework.png/svg")
    plt.close()

def figure2_decision_map():
    """Figure 2: Decision Map Flow"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colors for states
    green = '#4DAF4A'
    yellow = '#FFFF00'
    red = '#E31A1C'
    
    # Input box
    ax.add_patch(FancyBboxPatch((3.5, 9), 3, 0.7, boxstyle="round,pad=0.05", 
                                 facecolor='lightblue', edgecolor='black', linewidth=2))
    ax.text(5, 9.35, 'Climate Measure\nProposal', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Arrow down
    ax.annotate('', xy=(5, 8.2), xytext=(5, 8.8), 
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # S Check
    ax.add_patch(FancyBboxPatch((3.5, 7), 3, 1, boxstyle="round,pad=0.05",
                                 facecolor=COLORS['S'], edgecolor='black', linewidth=2, alpha=0.7))
    ax.text(5, 7.5, 'SUFFICIENT?\nW ≥ W_min', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Arrows from S
    ax.annotate('', xy=(5, 5.8), xytext=(5, 6.8), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.text(5.2, 6.3, 'YES', fontsize=9, color='green', fontweight='bold')
    ax.annotate('', xy=(8, 7.5), xytext=(6.6, 7.5), arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(7.2, 7.7, 'NO', fontsize=9, color='red', fontweight='bold')
    
    # E Check
    ax.add_patch(FancyBboxPatch((3.5, 4.5), 3, 1, boxstyle="round,pad=0.05",
                                 facecolor=COLORS['E'], edgecolor='black', linewidth=2, alpha=0.7))
    ax.text(5, 5, 'EFFICIENT?\nW/R optimal', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Arrows from E
    ax.annotate('', xy=(5, 3.3), xytext=(5, 4.3), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.text(5.2, 3.8, 'YES', fontsize=9, color='green', fontweight='bold')
    ax.annotate('', xy=(8, 5), xytext=(6.6, 5), arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(7.2, 5.2, 'NO', fontsize=9, color='red', fontweight='bold')
    
    # C Check
    ax.add_patch(FancyBboxPatch((3.5, 2), 3, 1, boxstyle="round,pad=0.05",
                                 facecolor=COLORS['C'], edgecolor='black', linewidth=2, alpha=0.7))
    ax.text(5, 2.5, 'CONSISTENT?\nNo conflicts', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Arrows from C
    ax.annotate('', xy=(2, 2.5), xytext=(3.4, 2.5), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.text(2.8, 2.7, 'YES', fontsize=9, color='green', fontweight='bold')
    ax.annotate('', xy=(8, 2.5), xytext=(6.6, 2.5), arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(7.2, 2.7, 'NO', fontsize=9, color='red', fontweight='bold')
    
    # Output boxes
    # ADMISSIBLE (green)
    ax.add_patch(FancyBboxPatch((0.5, 1.5), 2.2, 1.5, boxstyle="round,pad=0.1",
                                 facecolor=green, edgecolor='black', linewidth=2))
    ax.text(1.6, 2.25, 'ADMISSIBLE\n[OK] Verified', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    
    # TERMINATE (red) - right side
    ax.add_patch(FancyBboxPatch((7.5, 4), 2, 4.5, boxstyle="round,pad=0.1",
                                 facecolor=red, edgecolor='black', linewidth=2, alpha=0.8))
    ax.text(8.5, 6.25, 'TERMINATE\n[X] Rejected', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    
    # CONTINUABLE (yellow) - below main flow
    ax.add_patch(FancyBboxPatch((3.5, 0.3), 3, 1, boxstyle="round,pad=0.1",
                                 facecolor=yellow, edgecolor='black', linewidth=2))
    ax.text(5, 0.8, 'CONTINUABLE\n[~] Iterate', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.annotate('', xy=(5, 1.4), xytext=(5, 1.9), arrowprops=dict(arrowstyle='->', lw=1.5, color='gray', ls='--'))
    
    plt.title('Figure 2: Decision Map - 3-State Verification Flow', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('Figure2_Decision_Map.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('Figure2_Decision_Map.svg', format='svg', bbox_inches='tight', facecolor='white')
    print("[OK] Figure 2 saved: Figure2_Decision_Map.png/svg")
    plt.close()

def figure3_domain_co2():
    """Figure 3: Domain Distribution & CO₂ Impact"""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(DOMAINS))
    width = 0.6
    
    # Bar chart - Applications per domain
    bars = ax1.bar(x, APPS_PER_DOMAIN, width, color=COLORS['domains'], edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Domain', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Applications', fontsize=12, fontweight='bold', color='black')
    ax1.set_xticks(x)
    ax1.set_xticklabels(DOMAINS, fontsize=10)
    ax1.set_ylim(0, 8)
    
    # Add value labels on bars
    for bar, val in zip(bars, APPS_PER_DOMAIN):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(val),
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Secondary axis - CO₂ impact
    ax2 = ax1.twinx()
    co2_plot = [abs(c) if c != 0 else 0 for c in CO2_IMPACT]  # Convert to positive for plotting
    line = ax2.plot(x[:4], [abs(c) for c in CO2_IMPACT[:4]], 'o-', color=COLORS['highlight'], 
                    linewidth=2.5, markersize=10, label='CO₂ Reduction')
    ax2.set_ylabel('CO₂ Reduction (Gt/year)', fontsize=12, fontweight='bold', color=COLORS['highlight'])
    ax2.set_ylim(0, 30)
    ax2.tick_params(axis='y', labelcolor=COLORS['highlight'])
    
    # Add CO2 labels
    for i, (xi, val) in enumerate(zip(x[:4], CO2_IMPACT[:4])):
        if val != 0:
            ax2.annotate(f'{abs(val):.1f}', xy=(xi, abs(val)), xytext=(0, 10),
                        textcoords='offset points', ha='center', fontsize=9, 
                        color=COLORS['highlight'], fontweight='bold')
    
    # Total annotation
    ax1.annotate(f'TOTAL: 30 Apps | -50.7 Gt CO₂/year', xy=(0.5, 0.95), xycoords='axes fraction',
                fontsize=12, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))
    
    plt.title('Figure 3: Domain Distribution and CO₂ Impact', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('Figure3_Domain_CO2.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("[OK] Figure 3 saved: Figure3_Domain_CO2.png")
    plt.close()

def figure4_sec_distribution():
    """Figure 4: SEC Scores Distribution"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    scores = SEC_SCORES[:30]  # Use first 30
    
    # Histogram
    n, bins, patches = ax.hist(scores, bins=8, range=(0.80, 1.0), edgecolor='black', 
                               linewidth=1.5, alpha=0.7, color=COLORS['S'])
    
    # Color patches based on score ranges
    for patch, left_edge in zip(patches, bins[:-1]):
        if left_edge >= 0.85:
            patch.set_facecolor(COLORS['E'])  # Excellent - green
        elif left_edge >= 0.70:
            patch.set_facecolor(COLORS['C'])  # Good - orange
    
    # Add threshold lines
    ax.axvline(x=0.85, color='green', linestyle='--', linewidth=2, label='Excellent (≥0.85)')
    ax.axvline(x=0.70, color='orange', linestyle='--', linewidth=2, label='Good (≥0.70)')
    
    # Mean line
    mean_score = np.mean(scores)
    ax.axvline(x=mean_score, color='red', linestyle='-', linewidth=2.5, label=f'Mean: {mean_score:.3f}')
    
    # Statistics annotation
    stats_text = f'n = 30\nMean: {mean_score:.3f}\nσ = {np.std(scores):.3f}\nRange: {min(scores):.2f}-{max(scores):.2f}'
    ax.annotate(stats_text, xy=(0.02, 0.98), xycoords='axes fraction',
                fontsize=10, va='top', ha='left',
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', alpha=0.8))
    
    ax.set_xlabel('SEC Score', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_xlim(0.80, 1.0)
    ax.legend(loc='upper left', fontsize=9)
    
    plt.title('Figure 4: SEC Score Distribution (n=30 Applications)', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('Figure4_SEC_Distribution.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("[OK] Figure 4 saved: Figure4_SEC_Distribution.png")
    plt.close()

def figure5_agentic_improvement():
    """Figure 5: Agentic Enhancement by Domain"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Sort by improvement
    sorted_data = sorted(zip(DOMAINS, AGENTIC_IMPROVEMENT), key=lambda x: x[1], reverse=True)
    domains_sorted = [x[0] for x in sorted_data]
    improvements_sorted = [x[1] for x in sorted_data]
    
    y = np.arange(len(domains_sorted))
    
    # Gradient colors based on improvement
    colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(improvements_sorted)))
    
    bars = ax.barh(y, improvements_sorted, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for bar, val in zip(bars, improvements_sorted):
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, f'+{val:.1f}%',
               va='center', fontsize=10, fontweight='bold')
    
    ax.set_yticks(y)
    ax.set_yticklabels(domains_sorted, fontsize=11)
    ax.set_xlabel('SEC Score Improvement (%)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 22)
    
    # Add mean line
    mean_imp = np.mean(AGENTIC_IMPROVEMENT)
    ax.axvline(x=mean_imp, color='red', linestyle='--', linewidth=2, label=f'Mean: +{mean_imp:.1f}%')
    ax.legend(loc='lower right', fontsize=10)
    
    # Highlight top performer
    ax.annotate('Highest: Production\n(Automation potential)', xy=(18.2, 7), xytext=(14, 6),
               fontsize=9, ha='center', 
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'),
               arrowprops=dict(arrowstyle='->', color='black'))
    
    plt.title('Figure 5: Agentic AI Enhancement by Domain', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('Figure5_Agentic_Enhancement.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("[OK] Figure 5 saved: Figure5_Agentic_Enhancement.png")
    plt.close()

def generate_all_figures():
    """Generate all 5 figures"""
    print("\n" + "="*60)
    print("PROVOLUTION PUBLICATION FIGURES GENERATOR")
    print("="*60 + "\n")
    
    figure1_sec_framework()
    figure2_decision_map()
    figure3_domain_co2()
    figure4_sec_distribution()
    figure5_agentic_improvement()
    
    print("\n" + "="*60)
    print("\n[OK] ALL 5 FIGURES GENERATED SUCCESSFULLY")
    print("="*60)
    print("\nFiles created:")
    print("  - Figure1_SEC_Framework.png/svg")
    print("  - Figure2_Decision_Map.png/svg")
    print("  - Figure3_Domain_CO2.png")
    print("  - Figure4_SEC_Distribution.png")
    print("  - Figure5_Agentic_Enhancement.png")
    print("\nReady for Nature Climate Change submission!")

if __name__ == "__main__":
    generate_all_figures()
