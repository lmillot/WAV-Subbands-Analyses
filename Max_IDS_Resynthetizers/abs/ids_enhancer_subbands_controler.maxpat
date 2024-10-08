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
		"openrect" : [ 68.0, 163.0, 994.0, 501.0 ],
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
		"devicewidth" : 994.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-53",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 616.0, 67.5, 29.5, 22.0 ],
					"style" : "",
					"text" : "53"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 566.5, 62.0, 29.5, 22.0 ],
					"style" : "",
					"text" : "60"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 566.75, 11.0, 39.0, 39.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 637.5, 110.0, 39.0, 39.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 344.5, 47.0, 29.5, 22.0 ],
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
					"patching_rect" : [ 344.5, 18.0, 60.0, 22.0 ],
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
					"patching_rect" : [ 465.5, 18.0, 77.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 618.5, 64.0, 77.0, 24.0 ],
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
					"patching_rect" : [ 412.5, 11.0, 39.0, 39.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 637.5, 18.0, 39.0, 39.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-52",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 793.5, 306.0, 77.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 546.0, 191.0, 77.0, 24.0 ],
					"style" : "",
					"text" : "MASTER",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 793.5, 335.0, 105.0, 22.0 ],
					"style" : "",
					"text" : "s snd_remix_gain"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 819.0, 121.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 564.0, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.815686, 0.266667, 0.454902, 1.0 ],
					"elementcolor" : [ 0.815686, 0.266667, 0.454902, 1.0 ],
					"id" : "obj-51",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 819.0, 153.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 564.0, 41.0, 41.0, 140.0 ],
					"size" : 70.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 656.5, 336.0, 108.0, 22.0 ],
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
					"patching_rect" : [ 682.0, 304.0, 28.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 501.0, 191.0, 28.0, 24.0 ],
					"style" : "",
					"text" : "10",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-45",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 682.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 495.0, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-46",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 682.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 505.0, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 610.5, 360.25, 101.0, 22.0 ],
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
					"patching_rect" : [ 611.0, 304.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 453.222229, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "9",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 611.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 443.222229, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-42",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 611.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 453.222229, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 545.5, 384.5, 101.0, 22.0 ],
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
					"patching_rect" : [ 546.0, 304.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 400.444458, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "8",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 546.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 391.444458, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-37",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 546.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 401.444458, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 480.5, 408.75, 101.0, 22.0 ],
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
					"patching_rect" : [ 481.0, 304.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 348.666626, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "7",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 481.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 339.666626, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-33",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 481.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 349.666626, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 421.5, 433.0, 101.0, 22.0 ],
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
					"patching_rect" : [ 422.0, 304.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 296.888916, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "6",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 422.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 287.888916, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-29",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 422.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 297.888916, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 292.5, 338.0, 101.0, 22.0 ],
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
					"patching_rect" : [ 313.0, 304.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 245.111084, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "5",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 313.0, 122.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 236.111084, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-25",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 313.0, 154.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 246.111084, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 243.5, 362.5, 101.0, 22.0 ],
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
					"patching_rect" : [ 243.0, 306.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 194.333313, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "4",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 243.0, 124.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 184.333313, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-21",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 243.0, 156.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 194.333313, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 174.5, 387.0, 101.0, 22.0 ],
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
					"patching_rect" : [ 176.0, 306.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 141.555542, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "3",
					"textjustification" : 1
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
					"patching_rect" : [ 176.0, 124.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 132.555542, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-17",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 176.0, 156.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 142.555542, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 105.5, 411.5, 101.0, 22.0 ],
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
					"patching_rect" : [ 106.0, 306.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 89.777771, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "2",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 106.0, 124.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 80.777771, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-13",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 106.0, 156.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 90.777771, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 37.5, 436.0, 101.0, 22.0 ],
					"style" : "",
					"text" : "s 1-sb_new_gain"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"fontface" : 1,
					"fontsize" : 16.0,
					"id" : "obj-8",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 37.0, 306.0, 22.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 38.0, 191.0, 22.0, 24.0 ],
					"style" : "",
					"text" : "1",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 37.0, 124.0, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 29.0, 14.0, 40.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"elementcolor" : [ 0.878431, 0.815686, 0.721569, 1.0 ],
					"id" : "obj-2",
					"knobcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"maxclass" : "slider",
					"min" : -60.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 37.0, 156.0, 20.0, 140.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 39.0, 41.0, 20.0, 140.0 ],
					"size" : 100.0,
					"style" : ""
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"order" : 1,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"order" : 0,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"order" : 1,
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 0,
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"order" : 0,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"order" : 1,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"order" : 0,
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"order" : 1,
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"order" : 1,
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"order" : 0,
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"order" : 1,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"order" : 0,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"order" : 1,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"order" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"order" : 1,
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"order" : 0,
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"order" : 1,
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"order" : 0,
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"order" : 8,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"order" : 7,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"order" : 9,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"order" : 6,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"order" : 5,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"order" : 4,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"order" : 3,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"order" : 2,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"order" : 1,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-46", 0 ],
					"order" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"order" : 1,
					"source" : [ "obj-42", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"order" : 0,
					"source" : [ "obj-42", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"order" : 1,
					"source" : [ "obj-46", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 0 ],
					"order" : 0,
					"source" : [ "obj-46", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"order" : 1,
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-50", 0 ],
					"order" : 0,
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"source" : [ "obj-53", 0 ]
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
					"destination" : [ "obj-13", 0 ],
					"order" : 9,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"order" : 8,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"order" : 10,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"order" : 7,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"order" : 6,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"order" : 5,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"order" : 4,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"order" : 3,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"order" : 2,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-46", 0 ],
					"order" : 1,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"order" : 0,
					"source" : [ "obj-58", 0 ]
				}

			}
 ],
		"dependency_cache" : [  ],
		"autosave" : 0
	}

}
