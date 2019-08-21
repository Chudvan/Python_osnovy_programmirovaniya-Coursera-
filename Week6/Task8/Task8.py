def sortBase(inFile, outFile):
    class Pupil:
        name = ''
        surname = ''
        numberSchool = 0
        mark = 0
    pupils = []
    for line in inFile:
        curLine = line.split()
        pupil = Pupil()
        pupil.name = curLine[1]
        pupil.surname = curLine[0]
        pupil.numberSchool = int(curLine[2])
        pupil.mark = int(curLine[3])
        pupils.append(pupil)
    pupils.sort(key=lambda pupil: pupil.surname)
    for i in range(len(pupils)):
        print(pupils[i].surname, pupils[i].name, pupils[i].mark, file=outFile)


inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
sortBase(inFile, outFile)
