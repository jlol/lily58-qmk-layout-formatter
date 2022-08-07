import re

class Layer:
    def __init__(self, layer_name: str, keys: [str]):
        self.layer_name = layer_name
        self.keys = keys


def process_input(all_input: str) -> [Layer]:
    layers = []

    keygroup_regexp = re.compile("\((.*?)\)+", re.DOTALL)
    key_regexp = re.compile("(\S+)\,", re.DOTALL)

    layer_names = re.findall("\[.*\]", all_input)
    keys_unfiltered = keygroup_regexp.findall(all_input)

    if len(keys_unfiltered) != len(layer_names):
        print("Somthing went wrong")
        return

    for l, kg in zip(layer_names, keys_unfiltered):
        name = l.replace('[', '').replace(']', '')
        key_array = (key_regexp.findall(kg))
        layers.append(Layer(name, key_array))

    return layers

