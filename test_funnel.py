from daedalus.mechanics.conversion_path import ConversionPath

funnel = ConversionPath()
funnel.define_default()
print("Causal funnel:")
print(funnel.show_path())

