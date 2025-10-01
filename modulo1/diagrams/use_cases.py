from graphviz import Digraph

# Crear diagrama
dot = Digraph('UseCases_XR_Education', filename='modulo1/diagrams/use_cases', format='png')
dot.attr(rankdir='LR', size='8,5')  # izquierda -> derecha

# Estilo de nodos
dot.attr('node', shape='ellipse', fontsize='12', style='filled', fontname='Arial')

# Actores
dot.node('Student', 'Estudiante', shape='box', fillcolor='#AED6F1')
dot.node('Teacher', 'Profesor', shape='box', fillcolor='#F9E79F')

# Casos de uso
dot.node('Lab', 'Laboratorios virtuales', fillcolor='#ABEBC6')
dot.node('History', 'Aprendizaje inmersivo de historia', fillcolor='#ABEBC6')
dot.node('Science', 'Simulaciones de ciencias', fillcolor='#ABEBC6')
dot.node('Manage', 'Configurar experiencias XR', fillcolor='#F5CBA7')

# Conexiones
dot.edges([
    ('Student', 'Lab'),
    ('Student', 'History'),
    ('Student', 'Science'),
    ('Teacher', 'Manage'),
    ('Teacher', 'Lab'),
    ('Teacher', 'History'),
    ('Teacher', 'Science')
])

# Renderizar
print("Rendering use_cases SVG...")
dot.render(cleanup=False)
print("Diagrama generado en modulo1/diagrams/use_cases.png")

