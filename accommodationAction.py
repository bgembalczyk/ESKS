def accommodationAction(studentsToAccommodate: list, dorms: dict) -> None:
    while studentsToAccommodate:
        tmpStudent = studentsToAccommodate[0]
        tmpSegment = dorms[tmpStudent.prefDorm].findPlace(tmpStudent)
        if not tmpSegment:
            for dorm in dorms:
                tmpSegment = dorms[dorm].findPlace(tmpStudent)
                if tmpSegment:
                    break
        if not tmpSegment:
            print("There's not enough places in dorms!!!")
            print(len(studentsToAccommodate))
            print(studentsToAccommodate)
            break
        tmpStudent.accommodate(tmpSegment)
        studentsToAccommodate.pop(0)
