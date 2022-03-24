sg.Pane(
	[col5, sg.Column([

		[sg.Pane([col1, col2, col4], 
		handle_size=15, 
		orientation='v',  
		background_color=None, 
		show_handle=True, 
		visible=True, 
		key='_PANE_', 
		border_width=0,  
		relief=sg.RELIEF_GROOVE),]]),col3 ], 
	orientation='h', 
	background_color=None, 
	size=(160,160), 
	relief=sg.RELIEF_RAISED, 
	border_width=0)