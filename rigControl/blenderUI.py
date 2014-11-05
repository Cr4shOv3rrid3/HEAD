# This module controls the user interface in Blender that
# is used to manage the rigControl

import bpy
import pdb

class BLRigControl(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "RigControl"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_context = "object"


	# bpy.types.Scene.commandListenerActive = bpy.props.BoolProperty( name = "commandListenerActive", default=False)

	def draw(self, context):
		layout = self.layout
		obj = context.object

		row = layout.row()
		if bpy.context.scene['commandListenerActive']:
			prop = row.operator("wm.command_listener", text='Command Listener Running')
		else:
			prop = row.operator("wm.command_listener", text='Start Command Listener', icon='CONSOLE')
		

		row = layout.row()
		layout.label(text="Gestures:")

		row = layout.row()
		prop = row.operator("wm.animation_playback", text='Start Gestures Control', icon='ARMATURE_DATA')
		prop.option = 'ges'


		for action in bpy.data.actions:
			if "GST" in action.name:
				row = layout.row()
				label = action.name.replace("GST-","")
				props = row.operator("eva.gestures", text=label)
				props.evaAction = action.name
		

		row = layout.row()
		layout.label(text="Emotions:")

		row = layout.row()
		prop = row.operator("wm.animation_playback", text='Test Emotion Cycle')
		prop.option = 'emo'


def register():
	bpy.utils.register_class(BLRigControl)


def unregister():
	bpy.utils.unregister_class(BLRigControl)


def refresh():
	try:
		register()
	except ValueError:
		print('Re-registering')
		unregister()
		register()
	