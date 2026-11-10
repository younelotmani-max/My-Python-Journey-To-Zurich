tkhrbi9= "   @@@younes - junior ai developer at google zurich@@@   "
mzyan= " younes - junior ai developer at google zurich "
my_name="Younes"
my_city="Zurich"
print(tkhrbi9.strip().strip("@"))
print(mzyan.replace("junior" ,"senior").title())
print(len(mzyan))
print(mzyan.split())
print("=" * 90)
salaire=15000
tax=12.8
print(float(15000))
print(int(12.8))
print(15000//4)
print(3**4)
print("=" * 90)
goals=["bac","b2","Zurich","Google"]
goals.append("Deutch")
print(goals)
print(goals[1:4])
numbers=[1,4,8,90,542,97]
numbers.sort(reverse=True)
print(numbers)
goals.extend(numbers)
print(goals)
tuplee=(12,)
print(type(tuplee))
infos=("Google", "Switzerland", 2028)
print(infos)
ai_requirements={"python", "SQL", "python", "Ai"}
print(ai_requirements)
my_current_skills={"SQL","Ai"}
print(my_current_skills.intersection())
print(my_current_skills.difference())
my_current_skills.add("python")
print(ai_requirements.issuperset(my_current_skills))
final_dossier={
    "name":"Younes",
    "salaire":15000,
    "ai_infos":{
        "Ai_Tools",
        "Gemini",
        "Level",
        "Pro"
    }
}
print(final_dossier["ai_infos"])
final_dossier.update({"hired":True}) 
final_dossier.update({"department": "AI_Research"})
print(final_dossier)
copy_dossier=final_dossier.copy()
print(copy_dossier)
print(final_dossier.popitem())
final_dossier.pop("department", "AI_Research")
print(final_dossier)

