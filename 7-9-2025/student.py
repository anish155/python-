students={
    "name":["anish","kumar","raj","prabesh"],
    "marks":[89,88,78,69]
}

mark=students["marks"].copy()
highest=max(mark)
mark.remove(highest)

second_highest=max(mark)

index=students["marks"].index(second_highest)
name=students["name"][index]


print(f"the student who got the second highest mark is:{name}")
