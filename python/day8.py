google_skills={"linux","Python", "Git", "SQL","Ai" }
my_skills={"Ai","Git","Python"}
other_skills={"Illustrator","Photoshop"}
print(google_skills.intersection(my_skills))
print(google_skills.symmetric_difference(my_skills))
print(google_skills.isdisjoint(other_skills))
my_skills.add("SQL")
print(my_skills)
my_skills.update({"linux","Docker"})
my_skills.discard("Docker")
print(my_skills)
print(my_skills.issuperset(google_skills))
print("=" * 50)
profile={
    "name":"Younes",
    "Office":"Zurich",
    "year":2028,
    "langs":{
        "English":"B2",
        "German":"B2"
    }
}
print(profile["name"])
print(profile["langs"])
print(profile.keys())
profile.update({"Statut":"Accepted"})
print(profile.setdefault("Role","Ai Engineer"))
backup_profile=profile.copy()
print(backup_profile)
print(profile.popitem())
profile.pop("Role", None)
print(profile)
print(backup_profile)

