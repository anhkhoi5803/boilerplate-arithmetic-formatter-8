def arithmetic_arranger(problems, result=False):
    arranged_problems = ""
    spaces = "    "
    top = []
    mid = []
    dashes = []
    bot = []

    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    for problem in problems:
        problem = problem.split()
        numA = problem[0]
        numB = problem[2]
        difA = len(numA) - len(numB)
        difB = len(numB) - len(numA)

        if problem[1] not in ['+', '-']:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        if len(numA) > 4 or len(numB) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        for char in numA:
            if char.isalpha():
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems

        for char in numB:
            if char.isalpha():
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems

        if difA >= difB:
            numA = '  ' + numA
            numB = problem[1] + ' ' + ' ' * difA + numB
        elif difB > difA:
            numA = '  ' + ' ' * difB + numA
            numB = problem[1] + ' ' + numB

        top.append(numA)
        mid.append(numB)
        dashes.append('-' * len(numB))
        arranged_Top = spaces.join(top)
        arranged_Mid = spaces.join(mid)
        arranged_Dashes = spaces.join(dashes)

        if result:
            if problem[1] == '+':

                ans = str(int(problem[0]) + int(problem[2]))
            else:
                ans = str(int(problem[0]) - int(problem[2]))

            if len(numB) >= len(ans):
                fill = len(numB) - len(ans)
            else:
                fill = len(ans) - len(numB)

            ans = ' ' * fill + ans
            bot.append(ans)
            arranged_Bot = spaces.join(bot)
            arranged_problems = arranged_Top + "\n" + arranged_Mid + "\n" + arranged_Dashes + "\n" + arranged_Bot
        else:
            arranged_problems = arranged_Top + "\n" + arranged_Mid + "\n" + arranged_Dashes

    # print(result)
    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
