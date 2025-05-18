from daedalus.mechanics.conversion_path import ConversionPath
from daedalus.visualizations.dag_plotter import plot_dag

funnel = ConversionPath()
funnel.define_default()
plot_dag(funnel.graph, title="Marketing Conversion DAG")
