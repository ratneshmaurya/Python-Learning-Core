spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")


# Initial spice mix id: 2409277409312
# Initial spice mix id: set()
# Initial spice mix id: {'lemon', 'cardamom', 'Ginger'}
# After spice mix id: 2409277409312