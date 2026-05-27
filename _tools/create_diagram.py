import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')

# Title
ax.text(5, 9.5, 'Provolution GHG Scopes & Systemgrenzen', ha='center', fontsize=16, weight='bold')

# Main boundary (dashed)
main = FancyBboxPatch((0.8, 1.5), 8.4, 6.8, boxstyle="round,pad=0.1", ec='black', fc='#E8F4F8', lw=2.5, ls='--')
ax.add_patch(main)
ax.text(5, 8, 'PROVOLUTION SYSTEMGRENZE', ha='center', fontsize=13, weight='bold')

# Scope 1 (Red)
s1 = Rectangle((1.2, 6), 2.3, 1.5, ec='#C41E3A', fc='#FFD6D6', lw=2)
ax.add_patch(s1)
ax.text(2.35, 7.4, 'SCOPE 1', ha='center', fontsize=11, weight='bold', color='#C41E3A')
ax.text(2.35, 7.05, 'Direkte Emissionen', ha='center', fontsize=9)
ax.text(2.35, 6.7, '• Diesel, Heizung', ha='center', fontsize=8)
ax.text(2.35, 6.4, '• Eigene Fahrzeuge', ha='center', fontsize=8)

# Scope 2 (Orange)
s2 = Rectangle((3.8, 6), 2.3, 1.5, ec='#FF8C00', fc='#FFE4B5', lw=2)
ax.add_patch(s2)
ax.text(4.95, 7.4, 'SCOPE 2', ha='center', fontsize=11, weight='bold', color='#FF8C00')
ax.text(4.95, 7.05, 'Indirekte Energie', ha='center', fontsize=9)
ax.text(4.95, 6.7, '• Eingek. Strom', ha='center', fontsize=8)
ax.text(4.95, 6.4, '• Eingek. Wärme', ha='center', fontsize=8)

# Scope 3 Upstream (Yellow)
s3up = Rectangle((6.4, 6), 2.3, 1.5, ec='#FFD700', fc='#FFFACD', lw=2)
ax.add_patch(s3up)
ax.text(7.55, 7.4, 'SCOPE 3', ha='center', fontsize=11, weight='bold', color='#B8860B')
ax.text(7.55, 7.15, 'Upstream', ha='center', fontsize=9, style='italic')
ax.text(7.55, 6.85, '• Eingek. Güter', ha='center', fontsize=8)
ax.text(7.55, 6.6, '• Transport', ha='center', fontsize=8)
ax.text(7.55, 6.35, '• Dienstreisen', ha='center', fontsize=8)

# Scope 3 Downstream (Green)
s3down = Rectangle((6.4, 4.2), 2.3, 1.5, ec='#228B22', fc='#E0FFE0', lw=2)
ax.add_patch(s3down)
ax.text(7.55, 5.6, 'SCOPE 3', ha='center', fontsize=11, weight='bold', color='#228B22')
ax.text(7.55, 5.35, 'Downstream', ha='center', fontsize=9, style='italic')
ax.text(7.55, 5.05, '• Produkt-Nutzung', ha='center', fontsize=8)
ax.text(7.55, 4.8, '• End-of-Life', ha='center', fontsize=8)
ax.text(7.55, 4.55, '• Distribution', ha='center', fontsize=8)

# Outside Box (Grey - Excluded)
out = Rectangle((1.2, 2), 3, 1.2, ec='grey', fc='#F0F0F0', lw=1.5, ls=':')
ax.add_patch(out)
ax.text(2.7, 2.9, 'AUSGESCHLOSSEN', ha='center', fontsize=10, weight='bold', color='grey')
ax.text(2.7, 2.6, '• Privates Verhalten', ha='center', fontsize=8, color='grey')
ax.text(2.7, 2.35, '• Politische Effekte', ha='center', fontsize=8, color='grey')

# Arrows (Material/Energy flows)
arr_props = dict(arrowstyle='->', lw=1.5, color='#666')
ax.annotate('', xy=(3.8, 6.75), xytext=(3.5, 6.75), arrowprops=arr_props)  # 1->2
ax.annotate('', xy=(6.4, 6.75), xytext=(6.1, 6.75), arrowprops=arr_props)  # 2->3up
ax.annotate('', xy=(7.55, 5.7), xytext=(7.55, 6), arrowprops=arr_props)    # 3up->3down

# Legend
legend_elements = [
    mpatches.Patch(fc='#FFD6D6', ec='#C41E3A', label='Scope 1: Direkt'),
    mpatches.Patch(fc='#FFE4B5', ec='#FF8C00', label='Scope 2: Energie'),
    mpatches.Patch(fc='#FFFACD', ec='#FFD700', label='Scope 3: Upstream'),
    mpatches.Patch(fc='#E0FFE0', ec='#228B22', label='Scope 3: Downstream'),
    mpatches.Patch(fc='#F0F0F0', ec='grey', label='Ausgeschlossen')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9, framealpha=0.9)

# Standards
ax.text(5, 0.5, 'Standards: GHG Protocol Corporate Standard, ISO 14064-1, IPCC AR6 Guidelines', 
        ha='center', fontsize=8, style='italic', color='#555')

plt.tight_layout()
plt.savefig('20_CANON/docs/figures/systemgrenzen_provolution.png', dpi=300, bbox_inches='tight')
print("OK: Systemgrenzen-Diagramm erstellt: 20_CANON/docs/figures/systemgrenzen_provolution.png")
