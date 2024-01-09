def accommodationAction(studentsToAccommodate: list, dorms: dict) -> None:
    while studentsToAccommodate:
        tmpStudent = studentsToAccommodate[0]
        tmpSegment = dorms[tmpStudent.prefDorm].find_place(tmpStudent)
        if not tmpSegment:
            for dorm in dorms:
                tmpSegment = dorms[dorm].find_place(tmpStudent)
                if tmpSegment:
                    break
        if not tmpSegment:
            print("There's not enough places in dorms!!!")
            print(len(studentsToAccommodate))
            print(studentsToAccommodate)
            break
        tmpStudent.accommodate(tmpSegment)
        studentsToAccommodate.pop(0)
