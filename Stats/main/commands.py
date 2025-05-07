import output
import string
import numpy as np

def echo(msg: string) -> None:
    try:
        output.succsess(msg)
    except Exception as e:
        print(f"Echo failed? Reason: {e}")

def quit() -> None:
    print("Exiting.")
    exit()

def list_start(number_of_lists: int, element_count: int, random_data: bool, **kwargs) -> list:

    array_list = []

    for i in range(number_of_lists):
        if random_data:
            new_array = np.random.randint(0.00, 100.00, size=element_count)
            array_list.append(new_array)
        else:
            new_array = np.zeros(element_count, dtype=float)
            array_list.append(new_array)

    if array_list and random_data:
        output.succsess(f"Succsefully created {number_of_lists} with size {element_count}, with random data.")
    else:
        output.succsess(f"Succsefully created {number_of_lists} with size {element_count}, without random data.")

    return array_list;

def list_edit(Elist: list, array: int, element: int, val: float) -> None:
    try:
        if Elist and array <= len(Elist[array]):
            Elist[array][element] = val
        elif not Elist:
            output.error("List does not exist or was not provided, try list_start() first?")
        elif array > len(Elist[array]):
            output.error(f"Array does not exist in {Elist}, try a number between 0 and {len(Elist)}")
        else:
            output.error("Unknown Error.")
    except Exception as e:
        output.error(f"List edit failed? Reason: {e}")

def get_mean(List: list, array: int) -> float:
    try:
        if List and array <= len(List[array]):
            return np.mean(List[array])
        elif not List:
            output.error("Error, List does not exist. Try list_start() first")
            return None
        elif array > len(List[array]):
            output.error(f"Array does not exist in {List}, try a number between 0 and {len(List)}")
            return None
        else:
            output.error("Unknown Error.")
            return None
    except Exception as e:
        output.error(f"Get mean failed? Reason: {e}")

