from graphviz import Digraph

# Crear el diagrama de flujo
dot = Digraph('XR_Flujo_Decision_Refinado', filename='XR_Flujo_Decision_Refinado.gv', format='png')
dot.attr(rankdir='TB', size='8,10')

# Estilos generales
dot.attr('node', shape='rectangle', style='filled', fillcolor='#E0E7FF', color='#6366F1', fontname='Arial')
dot.attr('edge', fontname='Arial', fontsize='10')

# Nodos del flujo
dot.node('Inicio', 'Inicio del Proyecto XR')

# Pregunta inicial (Según tu descripción)
dot.node('Q_EXP', '¿Qué tipo de experiencia deseas crear?')

# Ramificaciones principales (Inmersión, Superposición, Combinación)
dot.node('Q_INM', '¿Prioridad: Inmersión total?')
dot.node('Q_SUP', '¿Prioridad: Superposición en entorno real?')
dot.node('Q_COMB', '¿Prioridad: Combinación inmersiva o Colaboración XR?')


# Rutas de Tecnología
dot.node('VR', 'Realidad Virtual (VR)\n(Unity XR, Meta Quest, HTC Vive)')
dot.node('AR', 'Realidad Aumentada (AR)\n(ARCore, ARKit, HoloLens)')
dot.node('XR', 'Realidad Mixta/Extendida (XR)\n(Magic Leap, MRTK)') # Renombrado de 'F' a 'XR' para claridad

# Factores de decisión adicionales
dot.node('Q_HW', '¿Recursos de hardware disponibles?')
dot.node('Q_COMP', '¿Compatibilidad con plataformas educativas/simulación?')

# Pasos finales
dot.node('IMPL', 'Implementar flujo colaborativo')
dot.node('EVAL', 'Evaluar rendimiento y compatibilidad') # Mantenemos evaluación final de rendimiento
dot.node('OPTIM', 'Optimización final y pruebas')

# Conexiones
dot.edge('Inicio', 'Q_EXP')
dot.edge('Q_EXP', 'Q_INM', label='Inmersión')
dot.edge('Q_EXP', 'Q_SUP', label='Superposición')
dot.edge('Q_EXP', 'Q_COMB', label='Combinación/Colaboración')

# Decisiones de Tecnología
dot.edge('Q_INM', 'VR', label='Sí')
dot.edge('Q_INM', 'Q_SUP', label='No (Verificar AR)') # Si no es inmersión total, se evalúa superposición

dot.edge('Q_SUP', 'AR', label='Sí')
dot.edge('Q_SUP', 'Q_COMB', label='No (Verificar XR)') # Si no es superposición, se evalúa combinación

dot.edge('Q_COMB', 'XR', label='Sí')
dot.edge('Q_COMB', 'Q_EXP', label='No (Reevaluar)') # Si nada aplica, se vuelve a la pregunta inicial (ciclo de refinamiento)

# Conexiones de los factores adicionales
dot.edge('VR', 'Q_HW')
dot.edge('AR', 'Q_HW')
dot.edge('XR', 'Q_HW')

dot.edge('Q_HW', 'Q_COMP', label='Adecuado')
dot.edge('Q_HW', 'Q_EXP', label='Limitado (Reevaluar)') # Si el hardware es limitado, se reevalúa el tipo de experiencia

dot.edge('Q_COMP', 'IMPL', label='Compatible')
dot.edge('Q_COMP', 'Q_EXP', label='No Compatible (Reevaluar)') # Si no es compatible, se reevalúa

dot.edge('IMPL', 'EVAL')
dot.edge('EVAL', 'OPTIM')

# Exportar el diagrama como imagen PNG
dot.render(format='png', cleanup=True)

print("✅ Diagrama 'XR_Flujo_Decision_Refinado.png' generado exitosamente según tus preguntas.")
