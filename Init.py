
import os
from random import randint
import sys
import shutil
import json
from tkinter.constants import SEL, TRUE
from traceback import print_tb

import PySimpleGUI as sg

from pprint import pprint, pformat
from ast import Pass, literal_eval


from libs.JSON import JsonClass
from libs.winTitle import WintTitle
from main import AppLayout
from datetime import date, datetime


#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()

COLORS_APP       = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/themeApp" )
THEMES_APP       = JSLOAD.json_read(name_file = "database/theme" )


PROJECT_NAME     = JSLOAD.json_read(name_file = "database/projectName" )



#-----------------------------------------------------------------------------------------------
class WindInitApp():
    def __init__(self ):
        sg.theme("Dark")

        # THME MODE UI LEMENTS -------------------------------------------------------------------------

        self.theme_mode         = "Dark"

        self.background_color   = THEMES_APP[ self.theme_mode ]["background_general"]   





        #-----------------------------------------------------------------------------------------------
        self.data_hor = datetime.now() 
        self.horr = self.data_hor.timetuple()
        
        print( self.data_hor.day , self.data_hor.month , self.data_hor.year , self.horr[3] , self.horr[4] , self.horr[5] )

        self.path_project_files_name  = [ "database/projects_datas/"]

        self.trava_comands      = True
        self.buttons_sizes      = (10 , 2)

        

        self.list_name_append   = [""]

        self.HEADINGS           = [ "Projeto" + " "*20 , "Data" + " "*20 ]
        
        self.dict_name_project  = PROJECT_NAME

        #print( self.data_selected )


        self.LIST_MATRIZ        = {
                                    "COL_1": [],
                                    "COL_2": [],
                                    "COL_3": [],
                                    "COL_4": []
                                }

        #----------- Layouts ----------------------------------------------------------------------------
        self.lay_buttons = [
                            [self.layoutButtons( text_button = "Abrir projeto" , 
                                                key_button  = "_BUTTON_OPEN_PROJECT_",
                                                button_type = 7 ,
                                                button_size = self.buttons_sizes )],

                            [self.layoutButtons( text_button = "Novo projeto" , 
                                                key_button  = "_BUTTON_NEW_PROJECT_DATA_",
                                                button_type = 7 ,
                                                button_size = self.buttons_sizes )
                            ]
                            ]

        self.table_lay  = [
                            [ self.tabelas( list_heanding     =  self.HEADINGS  , 
                                            list_values_table =  PROJECT_NAME["NAME_PR"]  , 
                                            key               =  "_TABLE_PROJECTS_") ]
                            ]

        self.one_layouts = [                        
                            #self.layoutText( text_str = "Titulo Project Name" , key_element = "_TEXT_")
                            #[sg.Input(key = "INPUT_TITULO") ],

                            [
                            sg.Column( self.lay_buttons, background_color = self.background_color , 
                                                        pad = 10 ,
                                                        expand_x = False, 
                                                        expand_y = True  ),
                            
                            sg.Column( self.table_lay , background_color = self.background_color , 
                                                        pad = 0 ,
                                                        expand_x = True, 
                                                        expand_y = True  )
                            ]

                            

                            ]

        #--------------------------------------------------------------------------------------------------------------------

        self.windons  = sg.Window( "PROJECT_GAMES_DEVELOPMENT_PROGRESSEC...",
                                    background_color        = self.background_color,
                                    size                    = (640 , 480) ,
                                    #icon                   = "Icon.ico",
                                    #titlebar_icon          = base64.icone , 
                                    #use_custom_titlebar    = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = False

                                    ).layout( self.one_layouts )

    #-------------------------------------------------------------------------------------------------------------------------
    def tabelas( self , list_heanding , list_values_table , key ):
        
        tablets = sg.Table(
                        values                  = list_values_table, 
                        headings                = list_heanding,
                        select_mode             = sg.TABLE_SELECT_MODE_BROWSE,
                        #change_submits          = False,
                        justification           = 'center',
                        text_color              = THEMES_APP[ self.theme_mode ]["texts_general"] ,
                        background_color        = THEMES_APP[ self.theme_mode ]["background_coluns_list_cards"][0],
                        selected_row_colors     = ( THEMES_APP[ self.theme_mode ]["texts_general"] , THEMES_APP[ self.theme_mode ]["buttons_general"] ),
                        header_background_color = THEMES_APP[ self.theme_mode ]["background_coluns_list_cards"][0],


                        border_width            = False ,
                        enable_events           = True,
                        enable_click_events     = True,
                        bind_return_key         = True,
                        alternating_row_color   = THEMES_APP[ self.theme_mode ]["background_coluns_list_cards"][0],
                        expand_x                = True,
                        expand_y                = True,

                        size                    = ( 2 , 2 ),
                        key                     = key,
                        right_click_menu        = [ "menu" , ["Abrir" , "Excluir"] ],
                        pad                     = 0 ,
                        
                        row_height              = 60 ,
                        col_widths              = [0 , 0, 0, 0],
                        hide_vertical_scroll    = True
                    )

        return tablets

    #-------------------------------------------------------------------------------------------------------------------------
    def layoutButtons(self , text_button , key_button , button_type , button_size  ):
        
        buttons  = sg.Button(   button_text             = text_button,
                                button_color            = ( THEMES_APP[ self.theme_mode ]["texts_general"] ,  THEMES_APP[ self.theme_mode ]["buttons_general"] ) ,
                                #disabled_button_color   = None,
                                mouseover_colors        = (   THEMES_APP[ self.theme_mode ]["buttons_general"] , THEMES_APP[ self.theme_mode ]["texts_general"] ),

                                button_type             = button_type ,
                                s                       = button_size, 
                                key                     = key_button ,
                                pad                     = 5,
                                border_width            = 0,
                                #image_data              = base64.buttons_greens 
                    )

        return buttons

    #-------------------------------------------------------------------------------------------------------------------------
    def saveValuesProject( self , events):
        
        if events == "_BUTTON_NEW_PROJECT_DATA_":
            data_hor = datetime.now()
            #-----------------------
            app         = WintTitle( type_windtitle = "LAYOUT_APP_INIT_PROJECTS_LIST" )
            name , imag = app.update()
            #-----------------------
            
            if name != "":
                self.dict_name_project["NAME_PR"].append(  [name , str( data_hor ) ]  )
                #self.dict_name_project["NAME_PR"].append( [name] )
                
                
                with open( "database/" + "projectName.json" , "w" , encoding="utf8") as js_file:
                    json.dump( self.dict_name_project , js_file , sort_keys = False, indent = 4)
                    pass

                with open( "database/projects_datas/" + name + ".json" , "w" , encoding="utf8") as js_file:
                    json.dump( self.LIST_MATRIZ , js_file , sort_keys = False, indent = 4)
                    pass
                
                
                PROJECTS = JSLOAD.json_read(name_file = "database/projectName" )
                #self.dict_name_project["NAME_PR"].append( PROJECTS["NAME_PR"] )

                self.windons["_TABLE_PROJECTS_"].update( values = PROJECTS["NAME_PR"]  )

                
        pass
    
    #-------------------------------------------------------------------------------------------------------------------------
    def saveProjectInListData(self , list_data_to_save ):
        
        self.dict_name_project["NAME_PR"].append( list_data_to_save )

        with open( "database//projectName.json" , "w" , encoding="utf8") as js_file:
            json.dump( self.dict_name_project , js_file , sort_keys = False, indent = 4)
            pass
        
        with open( "database/projects_datas/" + list_data_to_save[0] + ".json" , "w" , encoding="utf8") as js_file:
            json.dump( self.LIST_MATRIZ , js_file , sort_keys = False, indent = 4)
            pass



        PROJECTS = JSLOAD.json_read(name_file = "database/projectName" )
        self.windons["_TABLE_PROJECTS_"].update( values = PROJECTS["NAME_PR"]  )
        
    #-------------------------------------------------------------------------------------------------------------------------
    def selectElementTable(self , events, name_event ):
        
        #if events == name_event :
        try:
            table_selected_name = [ self.dict_name_project["NAME_PR"][row] for row in self.values["_TABLE_PROJECTS_"] ][0][0]
            self.list_name_append.append( table_selected_name )

        except:
            #print('An exception occurred')
            pass

        return self.list_name_append[-1] 
    
    #-------------------------------------------------------------------------------------------------------------------------
    def deletElement(self , events , table_key , name_event ):
        

        if events == name_event :
            try:
                PROJECTS = JSLOAD.json_read(name_file = "database/projectName" )

                data_selected = [ PROJECTS["NAME_PR"][row] for row in self.values[ table_key ]]
                

                for i in data_selected:
                    PROJECTS["NAME_PR"].remove(  i  )
                    
                    project_n =  "database/projects_datas/" + i[0] + ".json"

                    with open( "database/" + "projectName.json" , "w" , encoding="utf8") as js_file:
                        json.dump( PROJECTS , js_file , sort_keys = False, indent = 4)
                        pass

                    os.remove( project_n )

            except TypeError as e :
                #print(" Erro em codigo ---> " , e )
                pass

            self.windons[ table_key ].update( values = PROJECTS["NAME_PR"]  )

    #-------------------------------------------------------------------------------------------------------------------------
    
    def update(self):
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            
            try:

                self.deletElement( events = self.events  , table_key = "_TABLE_PROJECTS_"  , name_event = "Excluir" )
                
                if self.events == "_BUTTON_NEW_PROJECT_DATA_":
                    new_project_wind    = WintTitle()
                    new_name_project    = new_project_wind.update()
                    data_today_card     = str(self.data_hor.day) + " / " +  str(self.data_hor.month) + " / " + str(self.data_hor.year)
                    hminseg             = self.data_hor.timetuple()
                    horas_min_seg       = str(hminseg[3]) + " : " + str(hminseg[4]) + " : " + str(hminseg[5]) 
                    data_hor_ms         = data_today_card + "\n" +  horas_min_seg 

                    if new_name_project != "":
                        self.saveProjectInListData( list_data_to_save = [ new_name_project , data_hor_ms ] )

                        
                if self.events == "_BUTTON_OPEN_PROJECT_":
                    selected = self.selectElementTable( events =  self.events  , name_event = "_TABLE_PROJECTS_")
                    open_app = AppLayout( project_name =  selected )
                    open_app.update()


                if self.events == "Abrir":
                    selected = self.selectElementTable( events =  self.events  , name_event = "_TABLE_PROJECTS_")
                    open_app = AppLayout( project_name =  selected )
                    open_app.update()

            except:
                pass


        pass



#-------------------------------------------------------------------------------------------------------------------------
app = WindInitApp()
app.update()