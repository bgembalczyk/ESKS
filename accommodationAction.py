# def accommodationAction(studentsToAccommodate: list, dorms: dict) -> None:
#     while studentsToAccommodate:
#         tmpStudent = studentsToAccommodate[0]
#         tmpSegment = dorms[tmpStudent.prefDorm].find_place(tmpStudent)
#         if not tmpSegment:
#             for dorm_name in dorms:
#                 tmpSegment = dorms[dorm_name].find_place(tmpStudent)
#                 if tmpSegment:
#                     break
#         if not tmpSegment:
#             print("There's not enough places in dorms!!!")
#             print(len(studentsToAccommodate))
#             print(studentsToAccommodate)
#             break
#         tmpStudent.accommodate(tmpSegment)
#         studentsToAccommodate.pop(0)

def available_configurations(dorms):
    all_configs = []
    result = []
    for dorm in dorms:
        all_configs += dorm.segment_types(True)
    for dorm in dorms:
        for config in dorm.segment_types():
            result.append({"configuration": config, "count": all_configs.count(config)})
    return result
