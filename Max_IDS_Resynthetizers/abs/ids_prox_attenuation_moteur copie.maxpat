{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 7,
			"minor" : 3,
			"revision" : 5,
			"architecture" : "x86",
			"modernui" : 1
		}
,
		"openrect" : [ 117.0, 173.0, 820.0, 504.0 ],
		"bgcolor" : [ 0.484327, 0.566228, 0.413382, 1.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 0,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 0,
		"enablevscroll" : 0,
		"devicewidth" : 820.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 405.5, 50.0, 29.5, 22.0 ],
					"style" : "",
					"text" : "0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-56",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 405.5, 21.0, 60.0, 22.0 ],
					"style" : "",
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-55",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 526.5, 25.5, 77.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 223.5, 7.5, 77.0, 24.0 ],
					"style" : "",
					"text" : "RESET",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.815686, 0.266667, 0.454902, 1.0 ],
					"id" : "obj-54",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 473.5, 14.0, 39.0, 39.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 242.5, 37.0, 39.0, 39.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontsize" : 16.0,
					"id" : "obj-32",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 190.0, 46.5, 31.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 173.0, 56.5, 31.0, 24.0 ],
					"style" : "",
					"text" : "cm"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontsize" : 16.0,
					"id" : "obj-30",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 58.0, 46.5, 68.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 44.0, 56.5, 68.0, 24.0 ],
					"style" : "",
					"text" : "distance"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 800.0, 379.5, 189.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 800.0, 420.0, 66.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 607.0, 379.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 9"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 607.0, 420.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb9"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 414.0, 379.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 8"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 414.0, 420.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb8"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 221.0, 379.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 7"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 221.0, 420.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb7"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 28.0, 420.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb6"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-21",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 28.0, 379.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 6"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 800.0, 263.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 800.0, 304.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 607.0, 263.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 607.0, 304.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 414.0, 263.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 3"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 414.0, 304.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb3"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 12,
					"outlettype" : [ "int", "int", "int", "int", "int", "int", "int", "int", "int", "int", "int", "int" ],
					"patching_rect" : [ 20.0, 92.0, 353.5, 22.0 ],
					"style" : "",
					"text" : "t i i i i i i i i i i i i"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 354.5, 132.0, 26.0, 22.0 ],
					"style" : "",
					"text" : "s x"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 221.0, 264.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 324.0, 165.0, 151.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_level_law_cardio"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 135.0, 46.5, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 117.5, 57.5, 50.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 221.0, 305.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 31.0, 304.0, 59.0, 22.0 ],
					"style" : "",
					"text" : "s att_sb1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 324.0, 205.0, 33.0, 22.0 ],
					"style" : "",
					"text" : "s att"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-17",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 31.0, 263.5, 182.0, 22.0 ],
					"style" : "",
					"text" : "ids_load_subband_law_cardio 1"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-37",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : 2.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"orientation" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 20.0, 12.5, 201.0, 26.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 12.0, 22.5, 201.0, 26.0 ],
					"size" : 199.0,
					"style" : ""
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"source" : [ "obj-1", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-1", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"source" : [ "obj-1", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-1", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-1", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"source" : [ "obj-1", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"source" : [ "obj-1", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-1", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"source" : [ "obj-1", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-1", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-1", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"source" : [ "obj-54", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"source" : [ "obj-56", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "ids_load_subband_law_cardio.maxpat",
				"bootpath" : "~/Desktop/Max7_work/abs",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb1_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "ids_load_level_law_cardio.maxpat",
				"bootpath" : "~/Desktop/Max7_work/abs",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb2_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb3_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb4_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb5_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb6_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb7_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb8_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb9_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "attenuation_cardio_sb10_dB.txt",
				"bootpath" : "~/Desktop/Max7_work/Eloigneur_data/lois_Max_cardio",
				"patcherrelativepath" : "../Eloigneur_data/lois_Max_cardio",
				"type" : "TEXT",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
