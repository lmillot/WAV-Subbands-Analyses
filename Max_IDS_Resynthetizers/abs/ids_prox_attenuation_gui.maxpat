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
		"openrect" : [ 65.0, 273.0, 1026.0, 347.0 ],
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
		"devicewidth" : 1026.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-71",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 965.5, 39.5, 29.5, 22.0 ],
					"style" : "",
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 965.5, 4.0, 68.0, 22.0 ],
					"style" : "",
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 968.0, 130.0, 63.0, 22.0 ],
					"style" : "",
					"text" : "select 111"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-25",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 916.0, 301.0, 67.0, 22.0 ],
					"style" : "",
					"text" : "s Att_onoff"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 886.0, 51.0, 50.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 4,
					"outlettype" : [ "int", "int", "int", "int" ],
					"patching_rect" : [ 886.0, 16.0, 50.5, 22.0 ],
					"style" : "",
					"text" : "key"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-4",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 965.5, 206.5, 68.0, 38.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 739.25, 91.5, 86.5, 22.0 ],
					"style" : "",
					"text" : "ON/OFF (O)",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.815686, 0.266667, 0.454902, 1.0 ],
					"checkedcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"id" : "obj-3",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 914.5, 203.0, 41.0, 41.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 831.5, 68.5, 45.0, 45.0 ],
					"style" : "",
					"uncheckedcolor" : [ 0.815686, 0.266667, 0.454902, 1.0 ],
					"varname" : "att_onoff"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-65",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 687.0, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 675.0, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-64",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 615.333313, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 602.530884, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-63",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 543.666687, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 530.061707, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-62",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 472.0, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 457.59259, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-61",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 400.333344, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 385.123444, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-58",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 328.666656, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 312.654327, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-56",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 257.0, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 240.185181, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-55",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 185.333328, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 167.716049, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-54",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 113.666664, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 95.246918, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-51",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 42.0, 190.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 22.777779, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"format" : 6,
					"id" : "obj-50",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 831.0, 203.0, 60.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 752.5, 55.0, 60.0, 29.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 686.5, 94.0, 64.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-59",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 615.0, 94.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb9"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-57",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 543.0, 94.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb8"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-53",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 472.0, 94.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb7"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-49",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 400.5, 94.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb6"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 328.5, 94.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 257.5, 93.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 185.5, 93.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb3"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 114.0, 93.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 42.0, 93.0, 57.0, 22.0 ],
					"style" : "",
					"text" : "r att_sb1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 831.0, 94.0, 31.0, 22.0 ],
					"style" : "",
					"text" : "r att"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 14.0,
					"id" : "obj-52",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 828.5, 156.0, 117.0, 38.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 748.5, 9.0, 114.0, 38.0 ],
					"style" : "",
					"text" : "MEAN ATTENUATION",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 831.0, 253.0, 105.0, 22.0 ],
					"style" : "",
					"text" : "s snd_remix_gain"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 686.5, 251.0, 108.0, 22.0 ],
					"style" : "",
					"text" : "s 10-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-44",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 703.0, 158.0, 28.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 691.0, 16.0, 28.0, 24.0 ],
					"style" : "",
					"text" : "10",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 614.5, 285.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 9-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-40",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 634.333313, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 621.530884, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "9",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 543.5, 319.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 8-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-35",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 562.666687, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 549.061707, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "8",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 471.5, 353.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 7-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-31",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 486.0, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 476.59259, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "7",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 400.5, 387.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 6-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-27",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 419.333344, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 404.123444, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "6",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 328.5, 253.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 5-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-23",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 347.666656, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 331.654327, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "5",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 255.5, 283.25, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 4-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-19",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 276.0, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 259.185181, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "4",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 184.5, 313.5, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 3-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-15",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 204.333328, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 186.716049, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "3",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 112.5, 343.75, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 2-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-11",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 132.666656, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 114.246918, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "2",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 41.5, 374.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 1-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-5",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 56.0, 158.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 41.777779, 16.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "1",
					"textjustification" : 1
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-50", 0 ],
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 1,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"order" : 0,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-61", 0 ],
					"source" : [ "obj-49", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"source" : [ "obj-50", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-62", 0 ],
					"source" : [ "obj-53", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-54", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-56", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"source" : [ "obj-57", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 0 ],
					"source" : [ "obj-59", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"source" : [ "obj-61", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-62", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-64", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-71", 0 ],
					"source" : [ "obj-67", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-54", 0 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"source" : [ "obj-71", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-55", 0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-56", 0 ],
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"dependency_cache" : [  ],
		"autosave" : 0
	}

}
