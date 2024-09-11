from plantuml import PlantUML

def generate_uml(classes):
    uml_code = '@startuml\n'
    uml_code += 'skinparam backgroundColor #F9F9F9\n'
    uml_code += 'skinparam classBackgroundColor #FFFFF\n'
    uml_code += 'skinparam classBorderColor #000000\n'
    uml_code += 'skinparam classFontColor #0000FF\n'
    uml_code += 'skinparam classFontSize 14\n'
    uml_code += 'skinparam classAttributeIconSize 16\n'
    uml_code += 'skinparam classMethodIconSize 16\n'

    for class_name, class_info in classes.items():
        # Add class definitions with styling
        uml_code += f'class {class_name} {{\n'
        for attr in class_info['attributes']:
            uml_code += f'    {attr}\n'
        for method in class_info['methods']:
            uml_code += f'    +{method}()\n'
        uml_code += '}\n'
        
        # Add inheritance relationships
        for base_class in class_info['inherits']:
            uml_code += f'{base_class} <|-- {class_name}\n'

    uml_code += '@enduml'
    return uml_code



def save_uml_to_file(uml_code, filename='diagram.puml'):
    with open(filename, 'w') as f:
        f.write(uml_code)

def render_uml(uml_code, output_path='uml_diagram.png'):
    # Write the UML code to a .puml file
    puml_file_path = 'uml_diagram.puml'
    with open(puml_file_path, 'w') as file:
        file.write(uml_code)

    # Set up PlantUML server
    plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    
    # Process the .puml file and save as PNG
    plantuml.processes_file(puml_file_path, output_path)
