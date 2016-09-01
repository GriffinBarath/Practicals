def main():
    HEXADECIMAL_COLOUR_CODES = {"AntiqueWhite": "#faebd7", "Black": "#000000", "CornflowerBlue": "#6495ed",
                                "DarkGreen": "#006400",
                                "NavyBlue": "#000080", "RosyBrown": "#bc8f8f", "WhiteSmoke": "#f5f5f5",
                                "VioletRed": "#d02090",
                                "SteelBlue": "#4682b4", "SlateGray": "#708090"}

    for colour in HEXADECIMAL_COLOUR_CODES:
        print("{:15} is {:15}".format(colour, HEXADECIMAL_COLOUR_CODES[colour]))
    colourRequest = input("Enter colour name:")
    while colourRequest != "":
        if colourRequest in HEXADECIMAL_COLOUR_CODES:
            print(colourRequest, "is", HEXADECIMAL_COLOUR_CODES[colourRequest])
        else:
            print("Invalid colour entered!")
        colourRequest = input("Enter colour name:")


main()
