from graphviz import Digraph

# Crear el diagrama de flujo
dot = Digraph('XR_Flujo_Decision', filename='XR_Flujo_Decision.gv', format='png')
dot.attr(rankdir='TB', size='8,10')

# Estilos generales
dot.attr('node', shape='rectangle', style='filled', fillcolor='#E0E7FF', color='#6366F1', fontname='Arial')

# Nodos del flujo
dot.node('A', 'Inicio')
dot.node('B', '¿Interacción con el entorno real?')
dot.node('C', 'RA: ARCore, ARKit, HoloLens')
dot.node('D', '¿Nivel de inmersión deseado?')
dot.node('E', 'RV: Unity XR, Meta Quest, HTC Vive')
dot.node('F', 'RA avanzada o RM: Magic Leap, MRTK')
dot.node('G', 'Implementar flujo colaborativo')
dot.node('H', 'Evaluar rendimiento y compatibilidad')
dot.node('I', 'Optimización final y pruebas')

# Conexiones
dot.edge('A', 'B')
dot.edge('B', 'C', label='Sí')
dot.edge('B', 'D', label='No')
dot.edge('D', 'E', label='Alto')
dot.edge('D', 'F', label='Medio')
dot.edge('E', 'G')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')

# Exportar el diagrama como imagen PNG
dot.render('XR_Flujo_Decision', format='png', cleanup=True)

print("✅ Diagrama 'XR_Flujo_Decision.png' generado exitosamente.")
