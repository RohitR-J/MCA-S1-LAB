'''
Create a list of colors from comma-separated color names entered by user. Display
 first and last colors. 
'''
color_str = input("Enter color names seperated by comma")
color_list = color_str.split(",")
first_clr = color_list[0]
last_clr = color_list[-1]
print(f"first color : '{first_clr}', last color : '{last_clr}'")
