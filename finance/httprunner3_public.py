import uuid
import copy
from icecream import ic


def get_time_stamp(_var):
    return "{}@@@@@{}".format(uuid.uuid1().time, _var)


class ObjectDotAccessWrapper:
    def __init__(self, _data):
        self.data = _data
        if isinstance(_data, (dict, list, tuple)):
            self.__recurse_flat(self, _data)

    def __repr__(self):
        return str(self.data)

    def __recurse_flat(self, _object, _dict):
        for key in _dict:
            if isinstance(_dict[key], dict):
                _object_child = ObjectDotAccessWrapper(_dict[key])
                setattr(_object, key, _object_child)
                # ic("nested key", key)
                self.__recurse_flat(_object_child, _dict[key])
            elif isinstance(_dict[key], (list, tuple)):
                setattr(_object, key, _dict[key])
                for index, value in enumerate(_dict[key]):
                    if isinstance(value, (dict, list, tuple)):
                        _object_child = ObjectDotAccessWrapper(value)
                        # setattr(_object, f"{key}i{index}", _object_child)
                        _dict[key][index] = _object_child
                        # ic("nested key", key)
                        # self.__recurse_flat(_object_child, value)
                    # else:
                    #     setattr(_object, f"{key}i{index}", value)
            else:
                setattr(_object, key, _dict[key])
        return _object


if __name__ == "__main__":
    ic(eval('get_time_stamp(20)'))
    c = {"a": 3, "b": 5, "x": {"y": "xxx", "z": 1000},
         "y": [123, 234, {"x": 100, "y": "This is a test message", "ab": {"z": 10000}}]}
    b = [1, 2]
    a = ObjectDotAccessWrapper(c)
    ic(a)
    ic(a.b)
    ic(a.y)
    ic(a.y[1], a.y[2].ab.z)
    ic(a.y[2])
    ic(c)


