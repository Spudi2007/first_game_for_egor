# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    'name': 'BlenRig script',
    'author': 'Bart Crouch',
    'version': (122,),
    'blender': (2, 5, 7),
    'api': 36489,
    'location': 'View3D > Properties > BlenRig Controls panel',
    'warning': '',
    'description': 'Tools for controlling BlenRig rigs',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Rigging'}


import bpy
rig_name = "BlenRig"


# used for Full Bake
proportions_baker = ["zepam_mesh", "zepam_nails", "blenrig_mesh", "blenrig_mask", "blenrig_mask_jaw", "teeth_up_mesh", "teeth_low_mesh", "cornea_right", "eye_right", "eye_left", "cornea_left"]
reparent = ["blenrig_mask", "blenrig_mask_jaw", "blenrig_mask_rig"]
armature_baker = ["blenrig_mask_rig", "blenrig"]


# bones that should not be baked by Armature Baker
exclude_bones = []


arm_l = ["elbow_str.L", "shoulder.L", "arm_art.L", "elbow.L", "elbow_str.L", "elbow_line.L", "forearm.L", "hand_fk_target.L", "hand_ik.L", "hand_ik_master.L"]
arm_r = ["elbow_str.R", "shoulder.R", "arm_art.R", "elbow.R", "elbow_str.R", "elbow_line.R", "forearm.R", "hand_fk_target.R", "hand_ik.R", "hand_ik_master.R"]
foot_l = ["toe_lit_ctrl.L", "toe_fourth_ctrl.L", "toe_mid_ctrl.L", "toe_index_ctrl.L", "toe_big_ctrl.L", "toes_spread.L", "toes_ctrl.L", "toe_lit_1.L", "toe_lit_2.L", "toe_lit_3.L", "toe_lit_ik.L", "toe_fourth_1.L", "toe_fourth_2.L", "toe_fourth_3.L", "toe_fourth_4.L", "toe_fourth_ik.L", "toe_mid_1.L", "toe_mid_2.L", "toe_mid_3.L", "toe_mid_4.L", "toe_mid_ik.L", "toe_index_1.L", "toe_index_2.L", "toe_index_3.L", "toe_index_4.L", "toe_index_ik.L", "toe_big_1.L", "toe_big_2.L", "toe_big_3.L", "toe_big_ik.L", "toe_lit_str_1.L", "toe_lit_str_2.L", "toe_lit_str_3.L", "toe_fourth_str_1.L", "toe_fourth_str_2.L", "toe_fourth_str_3.L", "toe_fourth_str_4.L", "toe_mid_str_1.L", "toe_mid_str_2.L", "toe_mid_str_3.L", "toe_mid_str_4.L", "toe_big_str_1.L", "toe_big_str_2.L", "toe_big_str_3.L", "toe_index_str_1.L", "toe_index_str_2.L", "toe_index_str_3.L", "toe_index_str_4.L", "toe_str.L", "foot.L", "foot_roll_ctrl.L", "foot_ik.L", "heel_ctrl.L", "sole_ctrl.L"]
foot_r = ["toe_lit_ctrl.R", "toe_fourth_ctrl.R", "toe_mid_ctrl.R", "toe_index_ctrl.R", "toe_big_ctrl.R", "toes_spread.R", "toes_ctrl.R", "toe_lit_1.R", "toe_lit_2.R", "toe_lit_3.R", "toe_lit_ik.R", "toe_fourth_1.R", "toe_fourth_2.R", "toe_fourth_3.R", "toe_fourth_4.R", "toe_fourth_ik.R", "toe_mid_1.R", "toe_mid_2.R", "toe_mid_3.R", "toe_mid_4.R", "toe_mid_ik.R", "toe_index_1.R", "toe_index_2.R", "toe_index_3.R", "toe_index_4.R", "toe_index_ik.R", "toe_big_1.R", "toe_big_2.R", "toe_big_3.R", "toe_big_ik.R", "toe_lit_str_1.R", "toe_lit_str_2.R", "toe_lit_str_3.R", "toe_fourth_str_1.R", "toe_fourth_str_2.R", "toe_fourth_str_3.R", "toe_fourth_str_4.R", "toe_mid_str_1.R", "toe_mid_str_2.R", "toe_mid_str_3.R", "toe_mid_str_4.R", "toe_big_str_1.R", "toe_big_str_2.R", "toe_big_str_3.R", "toe_index_str_1.R", "toe_index_str_2.R", "toe_index_str_3.R", "toe_index_str_4.R", "toe_str.R", "foot.R", "foot_roll_ctrl.R", "foot_ik.R", "heel_ctrl.R", "sole_ctrl.R"]
hand_l = ["fing_spread.L", "fing_lit_ctrl.L", "fing_ring_ctrl.L", "fing_mid_ctrl.L", "fing_ind_ctrl.L", "fing_thumb_ctrl.L", "fing_thumb_1.L", "fing_thumb_2.L", "fing_thumb_3.L", "fing_thumb_hinge.L", "fing_ind_1.L", "fing_ind_2.L", "fing_ind_3.L", "fing_ind_4.L", "fing_ind_hinge.L", "fing_mid_1.L", "fing_mid_2.L", "fing_mid_3.L", "fing_mid_4.L", "fing_mid_hinge.L", "fing_ring_1.L", "fing_ring_2.L", "fing_ring_3.L", "fing_ring_4.L", "fing_ring_hinge.L", "fing_lit_1.L", "fing_lit_2.L", "fing_lit_3.L", "fing_lit_4.L", "fing_lit_hinge.L", "fing_thumb_str_1.L", "fing_thumb_str_2.L", "fing_thumb_str_3.L", "fing_thumb_str_4.L", "fing_ind_str_1.L", "fing_ind_str_2.L", "fing_ind_str_3.L", "fing_ind_str_4.L", "fing_ind_str_5.L", "fing_mid_str_1.L", "fing_mid_str_2.L", "fing_mid_str_3.L", "fing_mid_str_4.L", "fing_mid_str_5.L", "fing_ring_str_1.L", "fing_ring_str_2.L", "fing_ring_str_3.L", "fing_ring_str_4.L", "fing_ring_str_5.L", "fing_lit_str_1.L", "fing_lit_str_2.L", "fing_lit_str_3.L", "fing_lit_str_4.L", "fing_lit_str_5.L", "fing_str.L"]
hand_r = ["fing_spread.R", "fing_lit_ctrl.R", "fing_ring_ctrl.R", "fing_mid_ctrl.R", "fing_ind_ctrl.R", "fing_thumb_ctrl.R", "fing_thumb_1.R", "fing_thumb_2.R", "fing_thumb_3.R", "fing_thumb_hinge.R", "fing_ind_1.R", "fing_ind_2.R", "fing_ind_3.R", "fing_ind_4.R", "fing_ind_hinge.R", "fing_mid_1.R", "fing_mid_2.R", "fing_mid_3.R", "fing_mid_4.R", "fing_mid_hinge.R", "fing_ring_1.R", "fing_ring_2.R", "fing_ring_3.R", "fing_ring_4.R", "fing_ring_hinge.R", "fing_lit_1.R", "fing_lit_2.R", "fing_lit_3.R", "fing_lit_4.R", "fing_lit_hinge.R", "fing_thumb_str_1.R", "fing_thumb_str_2.R", "fing_thumb_str_3.R", "fing_thumb_str_4.R", "fing_ind_str_1.R", "fing_ind_str_2.R", "fing_ind_str_3.R", "fing_ind_str_4.R", "fing_ind_str_5.R", "fing_mid_str_1.R", "fing_mid_str_2.R", "fing_mid_str_3.R", "fing_mid_str_4.R", "fing_mid_str_5.R", "fing_ring_str_1.R", "fing_ring_str_2.R", "fing_ring_str_3.R", "fing_ring_str_4.R", "fing_ring_str_5.R", "fing_lit_str_1.R", "fing_lit_str_2.R", "fing_lit_str_3.R", "fing_lit_str_4.R", "fing_lit_str_5.R", "fing_str.R"]
head = ["look_str_loc", "head_str", "neck_1", "neck_ctrl_1", "neck_2", "neck_ctrl_2", "neck_3", "head_ctrl", "head" ]
leg_l = ["butt_str.L", "knee_str.L", "butt_ctrl.L", "thigh.L", "thigh_art.L", "knee_line.L", "knee.L", "calf.L"]
leg_r = ["butt_str.R", "knee_str.R", "butt_ctrl.R", "thigh.R", "thigh_art.R", "knee_line.R", "knee.R", "calf.R"]
torso = ["spine_ctrl_4", "spine_3", "spine_ctrl_3", "spine_2", "spine_ctrl_2", "spine_1", "spine_ctrl_1", "pelvis", "pelvis_ctrl", "torso_ctrl"]


# Inherit Scale Groups
s_torso = ["master", "master_body", "master_torso", "ball.L", "ball.R", "ball", "dicky_1", "dicky_2", "pelvis_ik", "pelvis.L", "pelvis.R", "butt_str.L", "butt_str.R", "butt.L", "butt.R", "spine_1_ik", "2ik_spine_2", "spine_2_ik", "2ik_spine_1", "back_fix.L", "back_fix.R", "chest_fix.L", "chest_fix.R", "2ik_spine_base", "clavi.L", "clavi.R", "clavi", "look.L", "look.R", "look", "look_head", "look_body", "look_master"]
s_head = ["lip_up_2.R", "lip_up_2.L","neck_1", "neck_2", "neck_3", "head", "maxi_ctrl", "lip_low_ctrl_2.L", "lip_low_ctrl_2.R", "lip_up_ctrl_2.L", "lip_up_ctrl_2.R", "head_str", "look_str_loc", "neck_ctrl_1", "neck_ctrl_2", "head_ctrl", "lip_up_7.L", "lip_up_7.R", "cheek_2.L", "cheek_2.R", "cheek_3.L", "cheek_3.R", "cheek_4.L", "cheek_4.R", "lip_up_5.L", "lip_up_5.R", "lip_up_6.L", "lip_up_6.R", "lip_low", "chin_ctrl", "chin", "lip_low_1.L", "lip_low_1.R", "lip_low_4.L", "lip_low_4.R", "lip_up_3.L", "lip_up_3.R", "lip_low_3.L", "lip_low_3.R", "lip_low_6.L", "lip_low_6.R", "cheek_1.L", "cheek_1.R", "chin_1.L", "chin_1.R", "lip_up_ctrl_3.L", "lip_up_ctrl_3.R", "smile_ctrl.L", "smile_ctrl.R", "lip_ctrl.L", "lip_ctrl.R", "lip_up_ctrl", "lip_low_ctrl", "lip_low_ctrl_2", "lip_up_ctrl_2", "brow_ctrl.L", "brow_ctrl.R", "neck_base_ctrl", "neck_base_hinge", "2ik_neck_3", "neck_1_ik", "2ik_neck_2", "neck_2_ik", "2ik_neck_1", "2ik_neck_base", "ear_1.L", "ear_2.L", "ear_3.L", "ear_1.R", "ear_2.R", "ear_3.R", "maxi_master", "maxi_inner", "maxi_outer", "maxi", "maxi_shp_at", "tongue_ctrl_1", "tongue_ctrl_2", "tongue_ctrl_3", "tongue_ctrl_4", "tongue_1", "tongue_2", "tongue_3", "eyelid_low_1.L", "eyelid_low_2.L", "eyelid_low_3.L", "eyelid_low_4.L", "eyelid_up_1.L", "eyelid_up_2.L", "eyelid_up_3.L", "eyelid_up_4.L", "eyelid_low_ctrl_1.L", "eyelid_low_ctrl_2.L", "eyelid_low_ctrl_3.L", "eyelid_low_ctrl_4.L", "eyelid_low_ctrl_5.L", "eyelid_up_ctrl_1.L", "eyelid_up_ctrl_2.L", "eyelid_up_ctrl_3.L", "eyelid_up_ctrl_4.L", "eyelid_up_ctrl_5.L", "eyelid_up_ctrl.L", "eyelid_low_ctrl.L", "eye.R", "eye.L", "eyelid_low_1.R", "eyelid_low_2.R", "eyelid_low_3.R", "eyelid_low_4.R", "eyelid_up_1.R", "eyelid_up_2.R", "eyelid_up_3.R", "eyelid_up_4.R", "eyelid_low_ctrl_1.R", "eyelid_low_ctrl_2.R", "eyelid_low_ctrl_3.R", "eyelid_low_ctrl_4.R", "eyelid_low_ctrl_5.R", "eyelid_up_ctrl_1.R", "eyelid_up_ctrl_2.R", "eyelid_up_ctrl_3.R", "eyelid_up_ctrl_4.R", "eyelid_up_ctrl_5.R", "eyelid_up_ctrl.R", "eyelid_low_ctrl.R", "eye.R", "forhead", "forhead_1.L", "forhead_2.L", "forhead_3.L", "forhead_1.R", "forhead_2.R", "forhead_3.R", "frown", "brow_1.L", "brow_2.L", "brow_3.L", "brow_1.R", "brow_2.R", "brow_3.R", "cheekbone_10.L", "cheekbone_1.L", "cheekbone_2.L", "cheekbone_3.L", "cheekbone_4.L", "cheekbone_5.L", "cheekbone_6.L", "cheekbone_7.L", "cheekbone_8.L", "cheekbone_9.L", "cheekbone_10.R", "cheekbone_1.R", "cheekbone_2.R", "cheekbone_3.R", "cheekbone_4.R", "cheekbone_5.R", "cheekbone_6.R", "cheekbone_7.R", "cheekbone_8.R", "cheekbone_9.R", "nose_frown.L", "nose_frown.R", "nose_frown", "cheekbone_up_ctrl.L", "cheekbone_up_ctrl.R", "cheek_ctrl.L", "cheek_ctrl.R", "cheekbone_low_ctrl.L", "cheekbone_low_ctrl.R", "nose", "nostril.L", "nostril.R", "lip_up_2", "lip_up_ctrl_3", "lip_up", "lip_up_ctrl_1", "lip_low_ctrl_1", "lip_low", "maxi_ctrl", "chin_ctrl", "chin", "cheek_1.L", "cheek_2.L", "cheek_3.L", "cheek_4.L", "cheek_1.R", "cheek_2.R", "cheek_3.R", "cheek_4.R", "lip_up_ctrl_2.L", "lip_up_ctrl_2.R", "lip_low_ctrl_2.L", "lip_low_ctrl_2.R", "lip_up_2.L", "lip_up_3.L", "lip_up_5.L", "lip_up_6.L", "lip_up_7.L", "lip_up_2.R", "lip_up_3.R", "lip_up_5.R", "lip_up_6.R", "lip_up_7.R", "lip_low_1.L", "lip_low_3.L", "lip_low_4.L", "lip_low_6.L", "lip_low_1.R", "lip_low_3.R", "lip_low_4.R", "lip_low_6.R", "chin_1.L", "chin_1.R"]  
s_arm_l = ["elbow_hinge.L", "elbow_master.L", "arm_master.L", "arm_hinge.L", "hand_ik_hinge.L", "hand_fk.L", "arm.L", "arm_fix.L", "elbow_fix.L", "arm_twist.L", "forearm_twist.L", "wrist_fix_low.L", "wrist_fix_up.L"]
s_arm_r = ["elbow_hinge.R", "elbow_master.R", "arm_master.R", "arm_hinge.R", "hand_ik_hinge.R", "hand_fk.R", "arm.R", "arm_fix.R", "elbow_fix.R", "arm_twist.R", "forearm_twist.R", "wrist_fix_low.R", "wrist_fix_up.R"]
s_hand_l = ["fing_thumb_ctrl_shp_at.L", "fing_thumb_3_rot.L", "fing_ind_ctrl_shp_at.L", "fing_ind_3_rot.L", "fing_ind_4_rot.L", "fing_mid_ctrl_shp_at.L", "fing_mid_3_rot.L", "fing_mid_4_rot.L", "fing_ring_ctrl_shp_at.L", "fing_ring_3_rot.L", "fing_ring_4_rot.L", "fing_lit_ctrl_shp_at.L", "fing_lit_3_rot.L", "fing_lit_4_rot.L", "fing_ind_fix.L", "fing_mid_fix.L", "fing_ring_fix.L", "fing_lit_fix.L", "fing_thumb_shp_at.L", "fing_ind_shp_at.L", "fing_mid_shp_at.L", "fing_ring_shp_at.L", "fing_lit_shp_at.L"]
s_hand_r = ["fing_thumb_ctrl_shp_at.R", "fing_thumb_3_rot.R", "fing_ind_ctrl_shp_at.R", "fing_ind_3_rot.R", "fing_ind_4_rot.R", "fing_mid_ctrl_shp_at.R", "fing_mid_3_rot.R", "fing_mid_4_rot.R", "fing_ring_ctrl_shp_at.R", "fing_ring_3_rot.R", "fing_ring_4_rot.R", "fing_lit_ctrl_shp_at.R", "fing_lit_3_rot.R", "fing_lit_4_rot.R", "fing_ind_fix.R", "fing_mid_fix.R", "fing_ring_fix.R", "fing_lit_fix.R", "fing_thumb_shp_at.R", "fing_ind_shp_at.R", "fing_mid_shp_at.R", "fing_ring_shp_at.R", "fing_lit_shp_at.R"]
s_leg_l = ["knee_str_loc.L", "floor.L", "thigh_twist.L", "thigh_twist.L", "knee_fix.L", "knee_pole_limit.L", "calf_twist.L"]
s_leg_r = ["knee_str_loc.R", "floor.R", "thigh_twist.R", "thigh_twist.R", "knee_fix.R", "knee_pole_limit.R", "calf_twist.R"]
s_foot_l = ["toe_big_ctrl_shp_at.L", "toe_index_ctrl_shp_at.L", "toe_mid_ctrl_shp_at.L", "toe_fourth_ctrl_shp_at.L", "toe_lit_ctrl_shp_at.L", "toe_big_3_rot.L", "toe_index_3_rot.L", "toe_index_4_rot.L", "toe_mid_3_rot.L", "toe_mid_4_rot.L", "toe_fourth_3_rot.L", "toe_fourth_4_rot.L", "toe_lit_3_rot.L", "toe_lit_fix.L", "toe_fourth_fix.L", "toe_mid_fix.L", "toe_index_fix.L", "toe_big_fix.L", "toe_lit_shp_at.L", "toe_fourth_shp_at.L", "toe_mid_shp_at.L", "toe_index_shp_at.L", "toe_big_shp_at.L", "foot_roll.L", "sole.L", "floor.L", "floor.R", "foot.L", "foot.R", "foot_roll_master.L", "foot_roll_master.R"]
s_foot_r = ["toe_big_ctrl_shp_at.R", "toe_index_ctrl_shp_at.R", "toe_mid_ctrl_shp_at.R", "toe_fourth_ctrl_shp_at.R", "toe_lit_ctrl_shp_at.R", "toe_big_3_rot.R", "toe_index_3_rot.R", "toe_index_4_rot.R", "toe_mid_3_rot.R", "toe_mid_4_rot.R", "toe_fourth_3_rot.R", "toe_fourth_4_rot.R", "toe_lit_3_rot.R", "toe_lit_fix.R", "toe_fourth_fix.R", "toe_mid_fix.R", "toe_index_fix.R", "toe_big_fix.R", "toe_lit_shp_at.R", "toe_fourth_shp_at.R", "toe_mid_shp_at.R", "toe_index_shp_at.R", "toe_big_shp_at.R", "foot_roll.R", "sole.R"]


# User interface
class BlenRigInterface(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'BlenRig Controls'
    
    @classmethod
    def poll(cls, context):
        if not bpy.context.active_object:
            return False
        return (context.active_object.type in ["ARMATURE", "MESH"])

    def draw(self, context):
        layout = self.layout
        arm = context.active_object.data
        props = context.window_manager.blenrig_props
        
        try:
            selected_bones = [bone.name for bone in context.selected_pose_bones]
        except:
            selected_bones = []
        try:
            blenrig = context.active_object.data["rig_name"]==rig_name
        except:
            blenrig = False
        
        def is_selected(names):
            for name in names:
                if name in selected_bones:
                    return True
            return False
        
        if context.mode=="POSE" and blenrig:
    
########### IK - FK box
            #if is_selected(arm_l + arm_r + leg_l + foot_l + leg_r + foot_r + torso + head) or arm["gui_ik_all"]:
            if "gui_ik" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            # expanded box
            if "gui_ik" in arm and arm["gui_ik"]:
                # general
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_ik"
                row.label("IK / FK", 'OUTLINER_OB_ARMATURE')
                row = row.row()
                row.alignment = "RIGHT"
                row.prop(props, "gui_ik_all", text="All")
                row = col.row()
                row.label("IK")
                row = row.row()
                row.alignment = "RIGHT"
                row.label("FK")
                    
                # meta-slider hack
#                if arm["ik_meta"] != arm["ik_meta_old"]:
#                    ik_sliders = ["ik_meta_old", "ik_arm.L", "ik_arm.R", "ik_leg.L", "ik_foot.L",
#                        "ik_leg.R", "ik_foot.R", "ik_torso", "ik_head"]
#                    for slider in ik_sliders:
#                        arm[slider] = arm["ik_meta"]
#                    context.active_object.update(context.scene)

                # properties
#                col.prop(arm, '["ik_meta"]', "All", slider=True)
#                col.separator()
                if is_selected(head) or props.gui_ik_all:
                    col.prop(arm, '["ik_head"]', "Head", slider=True)
                if is_selected(torso) or props.gui_ik_all:
                    col.prop(arm, '["ik_torso"]', "Torso", slider=True)
                if is_selected(arm_l) or props.gui_ik_all:
                    col.prop(arm, '["ik_arm.L"]', "Arm_Left", slider=True)
                if is_selected(arm_r) or props.gui_ik_all:
                    col.prop(arm, '["ik_arm.R"]', "Arm_Right", slider=True)
                if is_selected(leg_l + foot_l) or props.gui_ik_all:
                    col.prop(arm, '["ik_leg.L"]', "Leg_Left", slider=True)
                if is_selected(foot_l + leg_l) or props.gui_ik_all:
                    col.prop(arm, '["ik_foot.L"]', "Foot_Left", slider=True)
                if is_selected(leg_r + foot_r) or props.gui_ik_all:
                    col.prop(arm, '["ik_leg.R"]', "Leg_Right", slider=True)
                if is_selected(foot_r + leg_r) or props.gui_ik_all:
                    col.prop(arm, '["ik_foot.R"]', "Foot_Right", slider=True)


            # collapsed box
            elif "gui_ik" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_ik"
                row.label("IK / FK", 'MOD_ARMATURE')

########### Hinge box
            #if is_selected(torso + hand_l + hand_r + arm_l + arm_r + head) or arm["gui_hinge_all"]:
            if "gui_hinge" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            # expanded box
            if "gui_hinge" in arm and arm["gui_hinge"]:
                # general
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_hinge"
                row.label("HINGE", 'OUTLINER_DATA_ARMATURE')
                row = row.row()
                row.alignment = "RIGHT"
                row.prop(props, "gui_hinge_all", text="All")
                row = col.row()
                row.label("No")
                row = row.row()
                row.alignment = "RIGHT"
                row.label("Yes")
                    
                # meta-slider hack
#                if arm["hinge_fing_meta.L"] != arm["hinge_fing_meta_old.L"]:
#                    hinge_sliders = ["hinge_fing_meta_old.L", "hinge_fing_ind.L", "hinge_fing_ind.L", "hinge_fing_mid.L", "hinge_fing_ring.L", "hinge_fing_lit.L", "hinge_fing_thumb.L"]
#                    for slider in hinge_sliders:
#                        arm[slider] = arm["hinge_fing_meta.L"]
#                    context.active_object.update(context.scene)
#                if arm["hinge_fing_meta.R"] != arm["hinge_fing_meta_old.R"]:
#                    hinge_sliders = ["hinge_fing_meta_old.R", "hinge_fing_ind.R", "hinge_fing_ind.R", "hinge_fing_mid.R", "hinge_fing_ring.R", "hinge_fing_lit.R", "hinge_fing_thumb.R"]
#                    for slider in hinge_sliders:
#                        arm[slider] = arm["hinge_fing_meta.R"]
#                    context.active_object.update(context.scene)

                # properties
                if is_selected(head + torso) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_head"]', "Head", slider=True)
                if is_selected(arm_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_arm.L"]', "Arm_Left", slider=True)
                if is_selected(arm_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_arm.R"]', "Arm_Right", slider=True)
                    col.separator()
#                if is_selected(hand_l) or props.gui_hinge_all:
#                    col.prop(arm, '["hinge_fing_meta.L"]', "All_Fingers_Left", slider=True)
#                    col.separator()
                if is_selected(hand_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_thumb.L"]', "Thumb_Left", slider=True)
                if is_selected(hand_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_ind.L"]', "Index_Left", slider=True)
                if is_selected(hand_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_mid.L"]', "Middle_Left", slider=True)
                if is_selected(hand_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_ring.L"]', "Ring_Left", slider=True)
                if is_selected(hand_l) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_lit.L"]', "Little_Left", slider=True)
                    col.separator()
#                if is_selected(hand_r) or props.gui_hinge_all:
#                    col.prop(arm, '["hinge_fing_meta.R"]', "All_Fingers_Right", slider=True)
#                    col.separator()
                if is_selected(hand_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_thumb.R"]', "Thumb_Right", slider=True)
                if is_selected(hand_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_ind.R"]', "Index_Right", slider=True)
                if is_selected(hand_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_mid.R"]', "Middle_Right", slider=True)
                if is_selected(hand_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_ring.R"]', "Ring_Right", slider=True)
                if is_selected(hand_r) or props.gui_hinge_all:
                    col.prop(arm, '["hinge_fing_lit.R"]', "Little_Right", slider=True)
            # collapsed box
            elif "gui_hinge" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_hinge"
                row.label("HINGE", 'ARMATURE_DATA')

########### Stretch box
            #if is_selected(arm_l + hand_l + arm_r + hand_r + leg_l + foot_l + leg_r + foot_r + torso + head) or arm["gui_stretch_all"]:
            if "gui_stretch" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            # expanded box
            if "gui_stretch" in arm and arm["gui_stretch"]:
                # general
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_stretch"
                row.label("STRETCH", 'POSE_HLT')
                row = row.row()
                row.alignment = "RIGHT"
                row.prop(props, "gui_stretch_all", text="All")
                row = col.row()
                row.label("No")
                row = row.row()
                row.alignment = "RIGHT"
                row.label("Yes")

                # meta-slider hack
#                if arm["str_meta"] != arm["str_meta_old"]:
#                    stretch_sliders = ["str_meta_old", "str_head", "str_torso", "str_arm.L", "str_hand.L", "str_arm.R",
#                        "str_hand.R", "str_leg.L", "str_foot.L", "str_leg.R", "str_foot.R"]
#                    for slider in stretch_sliders:
#                        arm[slider] = arm["str_meta"]
#                    context.active_object.update(context.scene)
                
                # properties
#                col.prop(arm, '["str_meta"]', "All", slider=True)
#                col.separator()
                if is_selected(head) or props.gui_stretch_all:
                    col.prop(arm, '["str_head"]', "Head", slider=True)
                if is_selected(torso) or props.gui_stretch_all:
                    col.prop(arm, '["str_torso"]', "Torso", slider=True)
                if is_selected(arm_l) or props.gui_stretch_all:
                    col.prop(arm, '["str_arm.L"]', "Arm_Left", slider=True)
                if is_selected(hand_l) or props.gui_stretch_all:
                    col.prop(arm, '["str_hand.L"]', "Hand_Left", slider=True)
                if is_selected(arm_r) or props.gui_stretch_all:
                    col.prop(arm, '["str_arm.R"]', "Arm_Right", slider=True)
                if is_selected(hand_r) or props.gui_stretch_all:
                    col.prop(arm, '["str_hand.R"]', "Hand_Right", slider=True)
                if is_selected(leg_l) or props.gui_stretch_all:
                    col.prop(arm, '["str_leg.L"]', "Leg_Left", slider=True)
                if is_selected(foot_l) or props.gui_stretch_all:
                    col.prop(arm, '["str_foot.L"]', "Foot_Left", slider=True)
                if is_selected(leg_r) or props.gui_stretch_all:
                    col.prop(arm, '["str_leg.R"]', "Leg_Right", slider=True)
                if is_selected(foot_r) or props.gui_stretch_all:
                    col.prop(arm, '["str_foot.R"]', "Foot_Right", slider=True)
            # collapsed box
            elif "gui_stretch" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_stretch"
                row.label("STRETCH", 'OUTLINER_DATA_POSE')

########### Inherit scale box
            if "gui_scale" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            # expanded box
            if "gui_scale" in arm and arm["gui_scale"]:
                # general
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_scale"
                row.label("INHERIT SCALE", 'GROUP_BONE')
                row = col.split(percentage=0.15)
                col_left = row.column()
                col_right = row.column()
                col_left.separator()
                col_right.separator()
                # properties
                #Toggle ALL
                #col_right.label("All")
                #if arm["scale_meta"]:
                #    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_meta"
                #else:
                #    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_meta"
                #col_right.separator()
                #col_left.separator()
                #
                col_right.label("Head")
                if arm["scale_head"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_head"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_head"
                col_right.label("Torso")
                body = col.row()
                if arm["scale_torso"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_torso"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_torso"
                col_right.label("Arm_Left")
                if arm["scale_arm.L"]:
                        col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_arm.L"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_arm.L"
                col_right.label("Hand_Left")
                if arm["scale_hand.L"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_hand.L"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_hand.L"
                col_right.label("Arm_Right")
                if arm["scale_arm.R"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_arm.R"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_arm.R"
                col_right.label("Hand_Right")
                if arm["scale_hand.R"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_hand.R"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_hand.R"
                col_right.label("Leg_Left")
                if arm["scale_leg.L"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_leg.L"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_leg.L"
                col_right.label("Foot_Left")
                if arm["scale_foot.L"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_foot.L"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_foot.L"
                col_right.label("Leg_Right")
                if arm["scale_leg.R"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_leg.R"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_leg.R"
                col_right.label("Foot_Right")
                if arm["scale_foot.R"]:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_HLT").group = "scale_foot.R"
                else:
                    col_left.operator("armature.scale_inherit", icon="CHECKBOX_DEHLT").group = "scale_foot.R"

            # collapsed box
            elif "gui_scale" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_scale"
                row.label("INHERIT SCALE", 'GROUP_BONE')

########### Eyes and breathing box
            if "gui_misc" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            # expanded box
            if "gui_misc" in arm and arm["gui_misc"]:
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_misc"
                row.label("EYES & BREATHING", 'RESTRICT_VIEW_OFF')
                # Eyes part
                col = box.column()
                row = col.row()
                row.label("Free")
                row.label("Torso")
                row = row.row()
                row.alignment = "RIGHT"
                row.label("Head")
                col.prop(arm, '["look_switch"]', "Look", slider=True)

                box.separator()

                # Breathing part
                col = box.column()
                col.prop(arm, '["breathing"]', "Breathing", slider=True)
            # collapsed box
            elif "gui_misc" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_misc"
                row.label("EYES & BREATHING", 'RESTRICT_VIEW_OFF')

########### Armature Layers
            if "gui_layers" in arm:
                box = layout.box()
                col = box.column()
                row = col.row()
            if "gui_layers" in arm and arm["gui_layers"]:
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_layers"
                row.label("ARMATURE LAYERS", 'RENDERLAYERS')
                # expanded box
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=3, toggle=True, text="FACIAL")
                body.prop(arm, "layers", index=4, toggle=True, text="FACIAL EXTRAS")
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=0 , toggle=True, text="IK")
                body.prop(arm, "layers", index=1, toggle=True, text="IK EXTRAS")
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=2, toggle=True, text="FK")
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=6, toggle=True, text="FINGERS HINGE")
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=7 , toggle=True, text="STRETCH")
                col.separator()
                body = col.row()
                body.prop(arm, "layers", index=5 , toggle=True, text="EXTRAS")
                col.separator()
                col.label("WEIGHT PAINTING LAYER")
                col.prop(context.active_object.data, "layers", index=15, toggle=True, text="WP Bones")
                # collapsed box
            elif "gui_layers" in arm:
                row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_layers"
                row.label("ARMATURE LAYERS", 'RENDERLAYERS')

####### bake scripts
        box = layout.box()
        col = box.column()
        row = col.row()
        try:
            gui_bake = arm["gui_bake"]
        except:
            gui_bake = -1
        if gui_bake:
            if gui_bake < 0:
                grey_out = row.column()
                grey_out.enabled = False
                grey_out.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_bake"
            else:
                row.operator("armature.blenrig_gui", icon="TRIA_DOWN").tab = "gui_bake"
            row.label("RIGGING & BAKING", 'LAMP_SPOT')
            col.separator()
            col.label("CHARACTER BAKING")
            row = col.row()
            row.operator("armature.proportions_baker", text="Proportions").bake_selected = True
            row.operator("armature.armature_baker", text="Armature")
            row = col.row()
            row.operator("armature.full_bake", text="Full Bake")
            col.separator()
            col.label("ARMATURE EXTRAS")
            split = col.split()
           #row = split.row(align=True)
           #if context.active_object.type == 'ARMATURE':
               #row.prop_enum(arm, "pose_position", 'POSE', text="Pose")
               #row.prop_enum(arm, "pose_position", 'REST', text="Rest")
           #else:
               #row.active = False
               #row.label('Pose positions')
            row = split.row()
            row.operator("armature.reset_constraints")
            
            
        else:
            row.operator("armature.blenrig_gui", icon="TRIA_RIGHT").tab = "gui_bake"
            row.label("RIGGING & BAKING", 'LAMP_SPOT')


# Display or hide tabs (sets the appropriate id-property)
class ARMATURE_OT_blenrig_gui(bpy.types.Operator):
    "Display tab"
    bl_label = ""
    bl_idname = "armature.blenrig_gui"

    tab = bpy.props.StringProperty(name="Tab", description="Tab of the gui to expand")
    
    def invoke(self, context, event):
        arm = bpy.context.active_object.data
        if self.properties.tab in arm:
            arm[self.properties.tab] = not arm[self.properties.tab]
        return{'FINISHED'}


# Toggle scale-inherit property of all bones in group
class ARMATURE_OT_scale_inherit(bpy.types.Operator):
    "Mass toggle for the Inherit Scale property"
    bl_label = ""
    bl_idname = "armature.scale_inherit"

    group = bpy.props.StringProperty(name="Group")
    
    def invoke(self, context, event):
        group = self.properties.group
        arm = bpy.context.active_object.data
        arm[group] = not arm[group]
        
        toggles = []
        #Toggle All
        #if group == "scale_meta":
        #    toggles = hand_l + s_hand_l + hand_r + s_hand_r + s_arm_l + arm_l + s_arm_r + arm_r + leg_l + s_leg_l + leg_r + s_leg_r + foot_l + s_foot_l + foot_r + s_foot_r + s_head + head + s_torso + torso
        #    all_groups = ["scale_hand.L", "scale_hand.R", "scale_arm.L", "scale_arm.R", "scale_leg.L", "scale_leg.R", "scale_foot.L", "scale_foot.R", "scale_head", "scale_torso"]
        #    for g in all_groups:
        #        arm[g] = arm[group]
        if group == "scale_hand.L":
            toggles = hand_l + s_hand_l
        elif group == "scale_hand.R":
            toggles = hand_r + s_hand_r
        elif group == "scale_arm.L":
            toggles = s_arm_l + arm_l
        elif group == "scale_arm.R":
            toggles = s_arm_r + arm_r
        elif group == "scale_leg.L":
            toggles = leg_l + s_leg_l 
        elif group == "scale_leg.R":
            toggles = leg_r + s_leg_r 
        elif group == "scale_foot.L":
            toggles = foot_l + s_foot_l 
        elif group == "scale_foot.R":
            toggles = foot_r + s_foot_r 
        elif group == "scale_head":
            toggles = s_head + head
        elif group == "scale_torso":
            toggles = s_torso + torso

        for bone in toggles:
            arm.bones[bone].use_inherit_scale = arm[group]
        return{'FINISHED'}


# Proportions Baker operator
class ARMATURE_OT_proportions_baker(bpy.types.Operator):
    bl_label = "Proportions Baker"
    bl_idname = "armature.proportions_baker"
    bl_description = "Bake the proportions to the meshes"
    
    # set to False to bake the meshes defined in "proportions_baker"
    bake_selected = bpy.props.BoolProperty(name="Bake selected", default=True, description="Bake the meshes that are selected in the 3d-view") 
    
    @classmethod
    def poll(cls, context):
        if not bpy.context.object:
            return False
        return (bpy.context.object.type == "MESH" and context.mode=='OBJECT')
    
    def restore_shape_settings(self, old_shape, new_shape):
        new_shape.interpolation = old_shape["interpolation"]
        new_shape.mute = old_shape["mute"]
        new_shape.name = old_shape["name"]
        new_shape.relative_key = old_shape["relative_key"]
        new_shape.slider_max = old_shape["slider_max"]
        new_shape.slider_min = old_shape["slider_min"]
        new_shape.value = old_shape["value"]
        new_shape.vertex_group = old_shape["vertex_group"]
    
    def bake(self, context):
        old_ob = bpy.context.active_object
        if self.properties.bake_selected:
            bake_meshes = [ob.name for ob in bpy.context.selected_objects if ob.type=="MESH"]
        else:
            bake_meshes = proportions_baker[:]
        for name in bake_meshes:
            if name in bpy.data.objects:
                ob = bpy.data.objects[name]
            else:
                continue
            bpy.context.scene.objects.active = ob
            
            # store shapekeys
            mesh = ob.data
            key = mesh.shape_keys
            if key:
                slurph = key.slurph
                use_relative = key.use_relative
                reference = key.reference_key.name
                data_reference = dict([[i, shapekeypoint.co.copy()] for i, shapekeypoint in enumerate(key.reference_key.data)])
                
                store_shapes = []
                shapes = key.key_blocks
                for shape in shapes:
                    cur_shape = {}
                    cur_shape["data"] = dict([[i, shapekeypoint.co - data_reference[i]] for i, shapekeypoint in enumerate(shape.data)])
                    cur_shape["interpolation"] = shape.interpolation
                    cur_shape["mute"] = shape.mute
                    cur_shape["name"] = shape.name
                    cur_shape["relative_key"] = shape.relative_key
                    cur_shape["slider_max"] = shape.slider_max
                    cur_shape["slider_min"] = shape.slider_min
                    cur_shape["value"] = shape.value
                    cur_shape["vertex_group"] = shape.vertex_group
                    store_shapes.append(cur_shape)
                
                # remove shapekeys
                for i in range(len(shapes) - 1, -1, -1):
                    ob.active_shape_key_index = i
                    bpy.ops.object.shape_key_remove()
            else:
                store_shapes = False
            
            # apply modifiers
            mods = []
            for i in range(len(ob.modifiers)):
                mod = ob.modifiers[i]
                if mod.type in ['ARMATURE', 'MESH_DEFORM']:
                    mods.append([mod, i])
            for data in mods:
                mod, i = data
                vg = mod.vertex_group
                invert = mod.invert_vertex_group
                name = mod.name
                bpy.ops.object.modifier_copy(modifier=mod.name)
                bpy.ops.object.modifier_apply(modifier=mod.name)
                new_mod = ob.modifiers[i]
                new_mod.name = name
                new_mod.vertex_group = vg
                new_mod.invert_vertex_group = invert
            
            # restore shapekeys
            if store_shapes:
                # base key
                bpy.ops.object.shape_key_add()
                key = mesh.shape_keys
                key.slurph = slurph
                key.use_relative = use_relative
                
                old_shape = [shape for shape in store_shapes if shape["name"] == reference][0]
                new_shape = key.key_blocks[0]
                self.restore_shape_settings(old_shape, new_shape)
                data_reference = dict([[vertex.index, vertex.co.copy()] for vertex in mesh.vertices])
                
                # other keys
                for old_shape in store_shapes:
                    if old_shape["name"] == reference:
                        continue
                    bpy.ops.object.shape_key_add()
                    new_shape = key.key_blocks[-1]
                    self.restore_shape_settings(old_shape, new_shape)
                    ob.active_shape_key_index = len(key.key_blocks) - 1
                    for i, shapekeypoint in enumerate(new_shape.data):
                        shapekeypoint.co = old_shape["data"][i] + data_reference[i]
        
        bpy.context.scene.objects.active = old_ob
    
    def invoke(self, context, event):
        self.bake(context)
        self.report('INFO', "Baking done")
        return{'FINISHED'}
    
    def execute(self, context):
        self.bake(context)
        return{'FINISHED'}


# Armature Baker operator
class ARMATURE_OT_armature_baker(bpy.types.Operator):
    bl_label = "Armature Baker"
    bl_idname = "armature.armature_baker"
    bl_description = "Bake the current pose to the edit-mode armature"
    
    @classmethod
    def poll(cls, context):
        if not bpy.context.object:
            return False
        else:
            return (bpy.context.object.type == "ARMATURE")
    
    def bake(self, context):
        old_edit_matrices = {}
        old_pose_matrices = {}
        
        bpy.ops.object.mode_set(mode='EDIT')
        editbones = bpy.context.object.data.edit_bones
        for name in exclude_bones:
            b = editbones[name]
            old_edit_matrices[name] = [b.head[:], b.tail[:], b.roll]
        
        bpy.ops.object.mode_set(mode='POSE')
        posebones = bpy.context.object.pose.bones
        for name in exclude_bones:
            b = posebones[name]
            old_pose_matrices[name] = [b.location[:], b.rotation_quaternion.copy(), b.scale[:]]
        
        bpy.ops.pose.armature_apply()
        
        bpy.ops.object.mode_set(mode='EDIT')
        for name in exclude_bones:
            b = editbones[name]
            b.head, b.tail, b.roll = old_edit_matrices[name]
        
        bpy.ops.object.mode_set(mode='POSE')
        for name in exclude_bones:
            b = posebones[name]
            b.location, b.rotation_quaternion, b.scale = old_pose_matrices[name]
        
        arm = bpy.context.object.data
        bpy.ops.object.mode_set(mode='EDIT')
        old_active = arm.edit_bones.active.name
        old_layers = [i for i in arm.layers]
        arm.layers = [True]*32
        for b in posebones:
            for con in b.constraints:
                if con.type not in ['LIMIT_DISTANCE', 'STRETCH_TO', 'CHILD_OF']:
                    continue
                if con.type == 'LIMIT_DISTANCE':
                    con.distance = 0
                elif con.type == 'STRETCH_TO':
                    con.rest_length = 0
                elif con.type == 'CHILD_OF':
                    bpy.ops.object.mode_set(mode='EDIT')
                    arm.edit_bones.active = arm.edit_bones[b.name]
                    bpy.ops.object.mode_set(mode='POSE')
                    bpy.ops.constraint.childof_clear_inverse(constraint=con.name, owner='BONE')
                    bpy.ops.constraint.childof_set_inverse(constraint=con.name, owner='BONE')
                    # somehow it only works if you run it twice
                    bpy.ops.constraint.childof_set_inverse(constraint=con.name, owner='BONE')
                    bpy.ops.object.mode_set(mode='EDIT')
                    arm.edit_bones[b.name].select = False
        bpy.ops.object.mode_set(mode='EDIT')
        arm.edit_bones.active = arm.edit_bones[old_active]
        arm.layers = old_layers
        bpy.ops.object.mode_set(mode='POSE')

    def invoke(self, context, event):
        self.bake(context)
        self.report('INFO', "Baking done")
        return{'FINISHED'}

    def execute(self, context):
        self.bake(context)
        return{'FINISHED'}


# Full Bake operator
class ARMATURE_OT_full_bake(bpy.types.Operator):
    bl_label = "Full Bake"
    bl_idname = "armature.full_bake"
    bl_description = "Full automatic proportion and armature baking"
    
    @classmethod
    def poll(cls, context):
        return bpy.context.active_object

    def invoke(self, context, event):
        if proportions_baker[0] not in bpy.data.objects:
            self.report('ERROR', "Couldn't find zepam mesh, bake not started.")
            return{'CANCELLED'}
        
        # preparing scene
        bpy.ops.object.mode_set(mode='OBJECT')
        old_active = bpy.context.active_object
        old_selected = bpy.context.selected_objects
        old_layers = [i for i in bpy.context.scene.layers]
        for ob in old_selected:
            ob.select = False
        bpy.context.scene.objects.active = bpy.data.objects[proportions_baker[0]]

        # baking proportions
        bpy.ops.armature.proportions_baker(bake_selected=False)

        # unparenting
        parent_pairs = []
        for name in reparent:
            if name in bpy.data.objects:
                ob = bpy.data.objects[name]
            else:
                continue
            bpy.context.scene.layers = ob.layers
            bpy.context.scene.objects.active = ob
            ob.select = True
            parent_pairs.append([ob, ob.parent, ob.parent_bone])
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            ob.select = False

        # baking armatures
        for name in armature_baker:
            if name in bpy.data.objects:
                ob = bpy.data.objects[name]
            else:
                continue
            bpy.context.scene.layers = ob.layers
            bpy.context.scene.objects.active = ob
            bpy.ops.armature.armature_baker()

        # re-parenting
        for pp in parent_pairs:
            ob, parent, bone = pp
            ob.parent = parent
            ob.parent_type = 'BONE'
            ob.parent_bone = bone

        # cleaning up        
        for ob in bpy.context.selected_objects:
            ob.select = False
        bpy.context.scene.layers = old_layers
        bpy.context.scene.objects.active = old_active
        for ob in old_selected:
            ob.select = True
        
        self.report('INFO', "Baking done")
        return{'FINISHED'}


class ARMATURE_OT_reset_constraints(bpy.types.Operator):
    bl_label = "Reset Constraints"
    bl_idname = "armature.reset_constraints"
    bl_description = "Reset all posebone constraints"
    
    @classmethod
    def poll(cls, context):
        if not bpy.context.object:
            return False
        else:
            return (bpy.context.object.type=='ARMATURE' and \
                context.mode=='POSE')
    
    def invoke(self, context, event):
        pbones = context.active_object.pose.bones
        if len(pbones) < 1:
            self.report('INFO', "No bones found")
            return{'FINISHED'}
        
        amount = 0
        for pbone in pbones:
            for con in pbone.constraints:
                if con.type == 'LIMIT_DISTANCE':
                    amount += 1
                    con.distance = 0
                elif con.type == 'STRETCH_TO':
                    amount += 1
                    con.rest_length = 0
        self.report('INFO', str(amount) + " constraints reset")
        
        return{'FINISHED'}


# Needed for property registration
class BlenrigProps(bpy.types.PropertyGroup):
    gui_ik_all = bpy.props.BoolProperty(default=False, description="Display all, regardless of selection in the 3d-view")
    gui_hinge_all = bpy.props.BoolProperty(default=False, description="Display all, regardless of selection in the 3d-view")
    gui_stretch_all = bpy.props.BoolProperty(default=False, description="Display all, regardless of selection in the 3d-view")


classes = [ARMATURE_OT_reset_constraints,
    ARMATURE_OT_full_bake,
    ARMATURE_OT_armature_baker,
    ARMATURE_OT_proportions_baker,
    ARMATURE_OT_scale_inherit,
    ARMATURE_OT_blenrig_gui,
    BlenRigInterface,
    BlenrigProps
    ]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.WindowManager.blenrig_props = bpy.props.PointerProperty(type = BlenrigProps)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()