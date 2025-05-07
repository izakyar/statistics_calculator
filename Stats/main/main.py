
import commands
import output
import string
import numpy as np



def main():
    while True:
        user_input = input("Stats> ")
        user_input = user_input.lower()
        user_input_list = user_input.split()

        if not user_input_list:
            continue

        match user_input_list[0]:
            case "echo":
                commands.echo(user_input_list[1]
                              .join(user_input_list[1:]))
            case "quit":
                commands.quit()
            case "list-start":
                try:
                    amt_of_lists, amt_of_elements, random_data = int(user_input_list[1]), int(user_input_list[2]), user_input_list[3]

                    if random_data.upper() == "TRUE":
                        random_data = True
                    elif random_data.upper() == "FALSE":
                        random_data = False
                    else:
                        ValueError("Random data value must be 'true' or 'false' (non-case sensitive)")

                    
                except Exception as e:
                    output.error(f"List start failed? Reason: {e}")
            case "list-edit":
                try:
                    if user_input_list[1] is list and user_input_list[2] is int and user_input_list[3] is int and user_input_list[4] is float:
                        commands.list_edit(user_input_list[1], user_input_list[2], user_input_list[3], user_input_list[4])
                        output.succsess("Successfully changed value.")
                        output.succsess(f"New value: {user_input_list[1][2]}")
                    else:
                        output.error("Failed To edit, check if all inputs are proper (you may need to convert your interger to a float.)")
                except Exception as e:
                    output.error(f"List edit failed? Reason: {e}")
            case "get-average", "get-mean", "get-avg":
                try:
                    if user_input_list[1] is list and user_input_list[2] is int:
                        avg = commands.get_mean(user_input_list[1], user_input_list[2])
                        output.solution(f"Mean of {user_input_list[1][2]} is {avg}")
                    else:
                        output.error("One of the values might be bad")
                except Exception as e:
                    output.error(f"Get mean failed? Reason: {e}")
            case _:
                output.error("Unknown command")


if __name__ == "__main__":
    main()