# maya-python-3d-text
A simple way to create 3D Text in Maya (Like using the Type Tooll) using it's Python API

## Details
I needed to create some 3d text in Maya using Python but I struggled to find any concrete way to do this, as strangely the API offered by maya gives no easy way to do this. After stitching together a lot of things I found on the internet, I managed to find a way to do it.


At it's core, the text is created using the **cmds.CreatePolygonType()** function, which directly creates the 3D Text itself, but the function has no documentation anywhere on how to manipulate the created object.

## Editing the created object using attributes


### Finding the object
The way I found you can edit this created object is using **cmds.setAttr()**. In order to fully manipulate this object, you firstly need to find the object itself.

```
obj_name = cmds.ls(sl=True)[0]
```

Due to the way the Polygon Type works, we also need the name of the type node, which I found is usually **type1, type2, type3, ...** increasing for subsequent objects created.

```
type_node = cmds.listConnections(f"{obj_name}.message")[0]
```

### Editing the text

After we have the name of the type node, editing the text is straight forward, but there is a catch. The text we input needs to be a string formed of the hexadecimal representation of each character, separated by a space.

For example, the word **Hello** would look like **48 65 6c 6c 6f**.

To do this, I used the **convert_str_to_hex(text)** function.

After we have the hex input, we just set it using **cmds.setAttr()**, using **.textInput**.

### Editing other attributes

In order to edit other attributes, you need to find the attribute name it takes. To do this, we can use the [**cmds.listAttr()**](https://download.autodesk.com/us/maya/2009help/CommandsPython/listAttr.html) like this:

```
print(cmds.listAttr(f'{type_node}'))
```
This will print out a list of all the available attributes, like *alignmentMode, textInput, fontSize* and many, many more.

You can then easily set that attribute using the **cmds.setAttr()** command now.

### Knowing what values to use in  cmds.setAttr()

Each attribute has a different type of required value, for example *fontSize* takes in a float, whilst *alignmentMode* takes the numbers **1, 2, or 3**.

An easy way to see how the value should look is using the [**cmds.getAttr()**](https://download.autodesk.com/us/maya/2009help/CommandsPython/getAttr.html) function.

```
print(cmds.getAttr(f'{type_node}.fontSize'))
```

In this case, it would print *"5.0"*.

## Further manipulating the object

To do any other basic manipulations like moving, rotating, etc you can just use normal commands like **cmds.move()**.