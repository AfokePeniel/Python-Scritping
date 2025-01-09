def calculate_love_score(name1, name2):
    two_names = name1 + " " + name2
    T1 = 'T'
    T2 = 'R'
    T3 = 'U'
    T4 = 'E'
    L1 = 'L'
    L2 = 'O'
    L3 = 'V'
    L4 = 'E'
    C1 = two_names.lower().count(T1.lower())
    C2 = two_names.lower().count(T2.lower())
    C3 = two_names.lower().count(T3.lower())
    C4 = two_names.lower().count(T4.lower())
    S1 = two_names.lower().count(L1.lower())
    S2 = two_names.lower().count(L2.lower())
    S3 = two_names.lower().count(L3.lower())
    S4 = two_names.lower().count(L4.lower())
    love_score1 = C1 + C2 + C3 + C4 
    love_score2 = S1 + S2 + S3 + S4
    total_love_score = str(love_score1) + str(love_score2)
    print(f"The love score of {name1} and {name2} is : {total_love_score}")
            
calculate_love_score(name1="Kanye West", name2="Kim Kardashian")