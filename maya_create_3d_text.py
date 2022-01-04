import maya.cmds as cmds
    
def convert_str_to_hex(text):
    final = list()
    for char in text:
        final.append(format(ord(char), "x"))
    return ' '.join(final)
    
  
 def create_text_object(text):
    hex_text = convert_str_to_hex(text)
    # Create the text object
    cmds.CreatePolygonType()
    # get the object name
    obj_name = cmds.ls(sl=True)[0]
    # Get the type node.
    type_node = cmds.listConnections(f"{obj_name}.message")[0]
    # Sets the alignment mode, the text and font size of the text object.
    cmds.setAttr(f'{type_node}.alignmentMode', 3)
    cmds.setAttr(f'{type_node}.textInput', hex_text, type='string')
    cmds.setAttr(f'{type_node}.fontSize', 5.0)

    cmds.rotate(-90,0,0, obj_name)
    cmds.move(-10,0,1.5, obj_name)
    cmds.rename(obj_name, text) 