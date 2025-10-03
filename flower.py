def print_flower_with_name(name):
    # Flower upper petals
    print("     @@@     @@@")
    print("   @@@@@@@ @@@@@@@")
    print("  @@@@@@@@@@@@@@@@@")
    print("   @@@@@@@@@@@@@@@")
    print("     @@@@@@@@@@@")
    
    # Flower center with name
    name_line = f"       {name}       "
    print(name_line.center(25, " "))

    # Flower stem
    print("         |||")
    print("         |||")
    print("         |||")
    print("         |||")
    print("         |||")
    print("        /|||\\")
    print("       //|||\\\\")
    print("      ///|||\\\\\\")
    print("         |||")
    print("         |||")

# Call the function
your_name = input("Enter your name: ")
print_flower_with_name(your_name)