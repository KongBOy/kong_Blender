bpy.data
['actions', 'armatures', 'bl_rna', 'brushes', 'cache_files', 
'cameras', 'curves', 'filepath', 'fonts', 'grease_pencil', 'groups', 
'images', 'is_dirty', 'is_saved', 
'lamps', 'lattices', 'libraries', 'linestyles', 'masks', 
'materials', 
'meshes', 'metaballs', 'movieclips', 'node_groups', 
'objects', 'paint_curves', 'palettes', 'particles', 'rna_type', 
'scenes', 'screens', 'shape_keys', 'sounds', 'speakers', 'texts', 
'textures', 'use_autopack', 'user_map', 'version', 'window_managers', 
'worlds']

bpy.data.meshes
['bl_rna', 'find', 'foreach_get', 'foreach_set', 'get', 'is_updated', 'items', 'keys', 'new', 'new_from_object', 'remove', 'rna_type', 'tag', 'values']

bpy.data.meshes[0]
['animation_data', 'animation_data_clear', 'animation_data_create', 'auto_smooth_angle', 'auto_texspace', 'bl_rna', 'calc_normals', 'calc_normals_split', 'calc_smooth_groups', 'calc_tangents', 'calc_tessface', 'copy', 'create_normals_split', 'cycles', 
'edge_keys', 'edges', 'flip_normals', 'free_normals_split', 'free_tangents', 'from_pydata', 'has_custom_normals', 'is_editmode', 'is_library_indirect', 'is_updated', 'is_updated_data', 'library', 'loops', 'make_local', 
'materials', 'name', 'normals_split_custom_set', 'normals_split_custom_set_from_vertices', 'polygon_layers_float', 'polygon_layers_int', 'polygon_layers_string', 'polygons', 'preview', 'rna_type', 'shape_keys', 'show_double_sided', 'show_edge_bevel_weight', 'show_edge_crease', 'show_edge_seams', 'show_edge_sharp', 'show_edges', 'show_extra_edge_angle', 'show_extra_edge_length', 'show_extra_face_angle', 'show_extra_face_area', 'show_extra_indices', 'show_faces', 'show_freestyle_edge_marks', 'show_freestyle_face_marks', 'show_normal_face', 'show_normal_loop', 'show_normal_vertex', 'show_statvis', 'show_weight', 'skin_vertices', 'split_faces', 
'tag', 'tessface_uv_textures', 'tessface_vertex_colors', 'tessfaces', 'texco_mesh', 'texspace_location', 'texspace_size', 'texture_mesh', 'total_edge_sel', 'total_face_sel', 'total_vert_sel', 'transform', 'unit_test_compare', 'update', 'update_tag', 'use_auto_smooth', 'use_auto_texspace', 'use_customdata_edge_bevel', 'use_customdata_edge_crease', 'use_customdata_vertex_bevel', 'use_fake_user', 'use_mirror_topology', 'use_mirror_x', 'use_paint_mask', 'use_paint_mask_vertex', 'user_clear', 'user_of_id', 'user_remap', 'users', 
'uv_layer_clone', 'uv_layer_clone_index', 'uv_layer_stencil', 'uv_layer_stencil_index', 'uv_layers', 'uv_texture_clone', 'uv_texture_clone_index', 'uv_texture_stencil', 'uv_texture_stencil_index', 'uv_textures', 
'validate', 'validate_material_indices', 'vertex_colors', 'vertex_layers_float', 'vertex_layers_int', 'vertex_layers_string', 'vertex_paint_masks', 
'vertices']

unwarp前：
uv_layer_clone None
uv_layer_clone_index -1
uv_layer_stencil None
uv_layer_stencil_index -1
uv_layers <bpy_collection[0], UVLoopLayers>
uv_texture_clone None
uv_texture_clone_index -1
uv_texture_stencil None
uv_texture_stencil_index -1
uv_textures <bpy_collection[0], UVTextures>

unwarp後：
uv_layer_clone <bpy_struct, MeshUVLoopLayer("UVMap")>
uv_layer_clone_index 0
uv_layer_stencil <bpy_struct, MeshUVLoopLayer("UVMap")>
uv_layer_stencil_index 0
uv_layers <bpy_collection[1], UVLoopLayers>
data <bpy_struct, MeshUVLoopLayer("UVMap")>
uv_texture_clone <bpy_struct, MeshTexturePolyLayer("UVMap")>
uv_texture_clone_index 0
uv_texture_stencil <bpy_struct, MeshTexturePolyLayer("UVMap")>
uv_texture_stencil_index 0
uv_textures <bpy_collection[1], UVTextures>
data <bpy_struct, MeshTexturePolyLayer("UVMap")>



bpy.data.meshes[0].vertices[0]
['bevel_weight', 'bl_rna', 
'co', 'groups', 
'hide', 
'index', 
'normal', 'rna_type', 
'select', 'undeformed_co']

bm.verts
['ensure_lookup_table', 'index_update', 'layers', 'new', 'remove', 'sort']

bm.verts[]
['calc_edge_angle', 'calc_shell_factor', 
'co', 'copy_from', 'copy_from_face_interp', 'copy_from_vert_interp', 
'hide', 'hide_set', 
'index', 'is_boundary', 'is_manifold', 'is_valid', 'is_wire', 'link_edges', 'link_faces', 'link_loops', 
'normal', 'normal_update', 
'select', 'select_set', 'tag']

bpy.ops.uv
['align', 'average_islands_scale', 'circle_select', 'cube_project', 'cursor_set', 'cylinder_project', 'export_layout', 'follow_active_quads', 'hide', 'lightmap_pack', 'mark_seam', 'minimize_stretch', 'pack_islands', 'pin', 'project_from_view', 'remove_doubles', 'reset', 'reveal', 'seams_from_islands', 'select', 'select_all', 'select_border', 'select_lasso', 'select_less', 'select_linked', 'select_linked_pick', 'select_loop', 'select_more', 'select_pinned', 'select_split', 'smart_project', 'snap_cursor', 'snap_selected', 'sphere_project', 'stitch', 'tile_set', 'unwrap', 'weld']


out_node
['active_input_index', 
'base_path', 'bl_description', 'bl_height_default', 'bl_height_max', 'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type', 'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons', 'draw_buttons_ext', 
'file_slots', 
'format', 
'height', 
'hide', 'input_template', 
'inputs', 'internal_links', 'is_registered_node_type', 
'label', 'layer_slots', 
'location', 'mute', 
'name', 'output_template', 
'outputs', 'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'shading_compatibility', 'show_options', 'show_preview', 'show_texture', 
'socket_value_update', 'tag_need_exec', 
'type', 'update', 'use_custom_color', 
'width', 'width_hidden']


out_node.file_slots
['bl_rna', 'clear', 'find', 'foreach_get', 'foreach_set', 'get', 'items', 'keys', 'move', 
'new', 
'remove', 'rna_type', 'values']

out_node.file_slots[0]
['bl_rna', 
'format', 
'path', 'rna_type', 
'use_node_format']

out_node.file_slots[1].format
['bl_rna', 'cineon_black', 'cineon_gamma', 'cineon_white', 'color_depth', 'color_mode', 'compression', 'display_settings', 'exr_codec', 
'file_format', 'jpeg2k_codec', 'quality', 'rna_type', 'stereo_3d_format', 'tiff_codec', 'use_cineon_log', 'use_jpeg2k_cinema_48', 'use_jpeg2k_cinema_preset', 'use_jpeg2k_ycc', 'use_preview', 'use_zbuffer', 'view_settings', 'views_format']


bpy.data.scenes['Scene'].render.layers
['active', 'active_index', 'bl_rna', 'find', 'foreach_get', 'foreach_set', 'get', 'items', 'keys', 'new', 'remove', 'rna_type', 'values']


scene.render.layers["RenderLayer"]
['bl_rna', 'cycles', 'exclude_ambient_occlusion', 'exclude_emit', 'exclude_environment', 'exclude_indirect', 'exclude_reflection', 'exclude_refraction', 'exclude_shadow', 'exclude_specular', 'freestyle_settings', 'invert_zmask', 
'layers', 'layers_exclude', 'layers_zmask', 'light_override', 
'material_override', 
'name', 'pass_alpha_threshold', 'rna_type', 'samples', 'update_render_passes', 'use', 'use_all_z', 'use_ao', 'use_edge_enhance', 'use_freestyle', 'use_halo', 'use_pass_ambient_occlusion', 'use_pass_color', 'use_pass_combined', 'use_pass_diffuse', 'use_pass_diffuse_color', 'use_pass_diffuse_direct', 'use_pass_diffuse_indirect', 'use_pass_emit', 'use_pass_environment', 'use_pass_glossy_color', 'use_pass_glossy_direct', 'use_pass_glossy_indirect', 'use_pass_indirect', 'use_pass_material_index', 'use_pass_mist', 'use_pass_normal', 'use_pass_object_index', 'use_pass_reflection', 'use_pass_refraction', 'use_pass_shadow', 'use_pass_specular', 'use_pass_subsurface_color', 'use_pass_subsurface_direct', 'use_pass_subsurface_indirect', 'use_pass_transmission_color', 'use_pass_transmission_direct', 'use_pass_transmission_indirect', 
'use_pass_uv', 'use_pass_vector', 'use_pass_z', 'use_sky', 'use_solid', 'use_strand', 'use_zmask', 'use_ztransp']



bpy.context.scene.objects
['active', 'bl_rna', 'find', 'foreach_get', 'foreach_set', 'get', 'items', 'keys', 'link', 'rna_type', 'unlink', 'values']
