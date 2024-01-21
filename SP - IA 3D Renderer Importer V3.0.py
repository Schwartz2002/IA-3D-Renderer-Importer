import os


# This script will take an input of 3D points and import them into a craft file that can display and
# 	rotate them on a label. You can specify the point coordinates and their colors. The object you
# 	generate can rotate on the X and Y axes, controller by the inputs you set (default is Roll and
# 	Pitch). You can also modify the zoom paramater, with the default control for it being Throttle.







 
# WARNING: CRAFT_NAME WILL OVERWRITE A CRAFT IF IT ALREADY EXISTS, SO DO NOT USE A NAME OF A CRAFT
# 		       THAT YOU ALREADY HAVE SAVED UNLESS YOU WANT TO OVERWRITE IT

# Name of the craft when it is generated, you can change this to what you want, but 
# 	don't use the following characters: \ / : * ? < >
CRAFT_NAME = "IA 3D Renderer"





# This should automatically detect the directory of your SP craft files. 
# 	If for some reason it doesn't manually set "craft_directory" to the path to your craft files directory
crafts_directory = os.getenv('APPDATA')[:-7] + r"LocalLow\Jundroo\SimplePlanes\AircraftDesigns"



# This will get the final path of the craft that will be generated
file_path = os.path.join(crafts_directory, CRAFT_NAME) + ".xml"




#Set these to the input you want to control xRotation, yRotation, and zoom
rotXVar = "sum(Roll)"
rotYVar = "sum(Pitch)"
zoomVar = "Throttle"


# Whether or not to have the cube automatically spin unless you press AG1
# Pressing AG1 in-game will disable auto mode
AUTO_MODE = True


# The speed that the object rotates when in auto mode (only useful if AUTO_MODE is enabled)
rotateScalarX = 70
rotateScalarY = 150





# Here is where you create the points you want to be rendered, for an example, a cube has been created with the points 
#	and an arbitrary color for each point, but you can add more or take away some or modify the points however you like

points = [
# x   y   z  hex color
[-1,  1,  1, "FF0000"],
[ 1,  1,  1, "00FF00"],
[-1, -1,  1, "0000FF"],
[ 1, -1,  1, "FFFF00"],
[-1,  1, -1, "00FFFF"],
[ 1,  1, -1, "FF00FF"],
[-1, -1, -1, "FFFFFF"],
[ 1, -1, -1, "FC6600"],

]











# Data for the base craft file
xml_1 = f"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Aircraft name=\"{CRAFT_NAME}\" url=\"\" theme=\"Default\" size=\"1.365933,1.275001,0.5050002\" boundsMin=\"-0.6642165,1.651864,-0.2500002\" xmlVersion=\"7\" legacyJointIdentification=\"false\" clientVersion=\"1.12.203.0\">\n  <Variables>\n"
xml_2 = "  </Variables>\n  <Assembly>\n    <Parts>\n      <Part id=\"4\" partType=\"Label-1\" position=\"-0.2142162,2.289364,0.25\" rotation=\"270,180,0\" drag=\"0,0,0,0,0,0\" materials=\"0,1,2\" scale=\"1,1,1\" calculateDrag=\"false\" partCollisionResponse=\"Default\">\n        <Label.State designText=\""
xml_3 = "\" fontName=\"Default\" fontSize=\"1.5\" horizontalAlignment=\"Left\" verticalAlignment=\"Middle\" width=\"0.6\" height=\"0.849999964\" outlineWidth=\"0\" emission=\"1\" offset=\"0,0.006,0\" rotation=\"90,0,0\" gradient=\"None\" curvature=\"0\" curvatureDirection=\"Horizontal\" />\n      </Part>\n      <Part id=\"5\" partType=\"FlightComputer-1\" position=\"0.2017166,2.608354,1.49012E-08\" rotation=\"0,0,0\" drag=\"0,0,0,0,0,0\" materials=\"0,1,2,3\" partCollisionResponse=\"Default\">\n        <Cockpit.State primaryCockpit=\"True\">\n          <Variables />\n        </Cockpit.State>\n      </Part>\n      <Part id=\"6\" partType=\"Fuselage-Body-1\" position=\"0.2017166,2.233354,-4.470348E-08\" rotation=\"90,0,0\" drag=\"1,1,0.5,0.5,0.5,0.5\" materials=\"19\" partCollisionResponse=\"Default\">\n        <FuelTank.State fuel=\"0\" capacity=\"0\" />\n        <Fuselage.State version=\"2\" frontScale=\"2,1\" rearScale=\"2,1\" offset=\"0,0,2\" deadWeight=\"0\" buoyancy=\"0\" fuelPercentage=\"0\" smoothFront=\"False\" smoothBack=\"False\" fillCutFace=\"true\" autoSizeOnConnected=\"false\" cornerTypes=\"0,0,0,0,0,0,0,0\" />\n      </Part>\n    </Parts>\n    <Connections>\n      <Connection partA=\"4\" partB=\"6\" attachPointsA=\"0\" attachPointsB=\"2\" />\n      <Connection partA=\"5\" partB=\"6\" attachPointsA=\"0\" attachPointsB=\"1\" />\n    </Connections>\n    <Bodies>\n      <Body partIds=\"4,6,5\" position=\"0,0,0\" rotation=\"0,0,0\" velocity=\"0,0,0\" angularVelocity=\"0,0,0\" />\n    </Bodies>\n  </Assembly>\n  <Theme name=\"Custom\">\n    <Material color=\"000000\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" hidden=\"true\" />\n    <Material color=\"FFFFFF\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" hidden=\"true\" />\n    <Material color=\"000000\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" hidden=\"true\" />\n    <Material color=\"D0D0D0\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" hidden=\"true\" />\n    <Material color=\"E9E9E9\" r=\"0.15\" m=\"0.5\" s=\"0.7\" e=\"0\" />\n    <Material color=\"000000\" r=\"0.3\" m=\"0.5\" s=\"0.83\" e=\"0\" />\n    <Material color=\"001F7F\" r=\"0.3\" m=\"0.5\" s=\"0.83\" e=\"0\" />\n    <Material color=\"AA2A00\" r=\"0.15\" m=\"0.5\" s=\"0.7\" e=\"0\" />\n    <Material color=\"3F3F3F\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"5C0000\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"FFFFFF\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"FFF0F0\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"FF0F0F\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"AAAAAA\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"3F3F3F\" r=\"0.15\" m=\"0.5\" s=\"0.7\" e=\"0\" />\n    <Material color=\"ABABAB\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"446677\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"FF1143\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"FF6A12\" r=\"0\" m=\"0.65\" s=\"0.08\" e=\"0\" />\n    <Material color=\"0080FF\" r=\"0.3\" m=\"0.54\" s=\"1\" e=\"0\" />\n    <Material color=\"74B9FF\" r=\"0\" m=\"0\" s=\"0\" e=\"0\" />\n    <Material color=\"232323\" r=\"0\" m=\"0.5\" s=\"0.5\" e=\"0\" />\n    <Material color=\"FFFFFF\" r=\"0\" m=\"0\" s=\"0\" e=\"1\" />\n    <Material color=\"171717\" r=\"0.15\" m=\"0.5\" s=\"0.7\" e=\"0\" />\n  </Theme>\n  <Instructions>Welcome to IA 3D Renderer v1.0!\n\n\n\nControls:\n  Action Group 1: Toggle Manual Mode on/off\n  Throttle: Zoom\n\n\n\nWhile Manual Mode is on:\n  Roll: Rotate on X Axis\n  Pitch: Rotate on Y Axis\n\n\n</Instructions>\n</Aircraft>"












xmlFile = open(file_path, "w")






xmlFile.write(xml_1)



# Write the variables
if AUTO_MODE:
	xmlFile.write(f"    <Setter variable=\"rotX\" function=\"(Activate1?{rotXVar}*180:Time*{rotateScalarX})\" priority=\"0\" />\n")
	xmlFile.write(f"    <Setter variable=\"rotY\" function=\"(Activate1?{rotYVar}*180:Time*{rotateScalarY})\" priority=\"0\" />\n")
else:
	xmlFile.write(f"    <Setter variable=\"rotX\" function=\"{rotXVar}*180\" priority=\"0\" />\n")
	xmlFile.write(f"    <Setter variable=\"rotY\" function=\"{rotYVar}*180\" priority=\"0\" />\n")


xmlFile.write(f"    <Setter variable=\"zoom\" function=\"(1+{zoomVar})\" priority=\"0\" />\n")
xmlFile.write(f"    <Setter variable=\"renderClock\" function=\"abs(rate(rotX))|abs(rate(rotY))|abs(rate(zoom))|Time&lt;1\" priority=\"0\" />\n")

for x in range(len(points)):
    xmlFile.write(f"    <Setter variable=\"pointXRender{x}\" function=\"(zoom*({points[x][0]}*cos(rotX)+sin(rotX)*({points[x][1]}*sin(rotY)+{points[x][2]}*cos(rotY))))\" priority=\"0\" activator=\"renderClock\" />\n")
    xmlFile.write(f"    <Setter variable=\"pointYRender{x}\" function=\"(zoom*({points[x][1]}*cos(rotY)-{points[x][2]}*sin(rotY)))\" priority=\"0\" activator=\"renderClock\" />\n")

xmlFile.write("\n")




xmlFile.write(xml_2)





# Write the label data
xmlFile.write("&lt;line-height=-0px&gt;&#xD;&lt;br&gt;")

for i in range(len(points)):
    xmlFile.write(f"&lt;color=#{str(points[i][3])}&gt;&lt;pos={{pointXRender{i}}}px&gt;&lt;voffset={{pointYRender{i}}}px&gt;.&#xD;&lt;br&gt;")

xmlFile.write("&lt;color=#FFFFFF&gt;&lt;pos=0&gt;&lt;voffset=0&gt; ")





xmlFile.write(xml_3)






print(f"Your craft rendering {len(points)} points has been saved to {file_path}")
